import json
import boto3

SNS_TOPIC_ARN = "arn:aws:sns:ap-south-1:383043574805:EventAlertsTopic"  # Replace with your ARN

sns = boto3.client('sns')

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])
        email = body['email']
        
        sns.subscribe(
            TopicArn=SNS_TOPIC_ARN,
            Protocol='email',
            Endpoint=email
        )
        sns.publish(
           TopicArn=SNS_TOPIC_ARN,
           Message=f"New subscription request: {email}",
           Subject="New Subscriber"
        )
        
        return {
            "statusCode": 200,
            "body": json.dumps({"message": "Subscription request sent! Please check your email."})
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"message": f"Failed to subscribe: {str(e)}"})
        }
        return {
        'statusCode': 200,
        'headers': {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Allow-Methods': 'OPTIONS,POST'
         },
        'body': json.dumps({'message': 'Successfully subscribed!'})
        }
