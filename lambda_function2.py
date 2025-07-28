import json
import boto3
from datetime import datetime

S3_BUCKET = "event-app-frontend-rohan"         # Replace with your bucket name
FILE_KEY = "events.json"
SNS_TOPIC_ARN = "arn:aws:sns:ap-south-1:383043574805:EventAlertsTopic"  # Replace with your topic ARN

s3 = boto3.client('s3')
sns = boto3.client('sns')

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])
        title = body['title']
        description = body['description']
        timestamp = datetime.utcnow().isoformat()

        # Fetch existing events
        file_obj = s3.get_object(Bucket=S3_BUCKET, Key=FILE_KEY)
        events = json.loads(file_obj['Body'].read().decode())

        # Add new event
        new_event = {
            "title": title,
            "description": description,
            "timestamp": timestamp
        }
        events.append(new_event)

        # Save updated list
        s3.put_object(Bucket=S3_BUCKET, Key=FILE_KEY, Body=json.dumps(events))

        # Send notification
        sns.publish(
            TopicArn=SNS_TOPIC_ARN,
            Subject=f"New Event: {title}",
            Message=f"{title}\n\n{description}\n\nPosted at: {timestamp}"
        )

        return {
            "statusCode": 200,
            "body": json.dumps({"message": "Event created and alert sent!"})
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"message": f"Error: {str(e)}"})
        }
