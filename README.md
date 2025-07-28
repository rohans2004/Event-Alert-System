# 🚨 Event Alert System on AWS

This is a real-time event alert system built using AWS serverless services where users can subscribe via email and get instant alerts when a new event (like natural disasters, announcements, etc.) is created by the admin.

## 🔧 Tech Stack

- **Frontend:** HTML, CSS, JavaScript (Hosted on S3)
- **Backend:** AWS Lambda (Python)
- **API Gateway:** To trigger Lambda securely
- **Amazon SNS:** For sending alert emails
- **Amazon S3:** Hosting website + storing events.json

---

## 📁 Project Structure

/event-alert-system
│
├── index.html # Main HTML page hosted on S3
├── script.js # Handles form logic and API calls
├── style.css # Styling for UI
├── events.json # Stored in S3; keeps latest event info
│
├── lambda_subscribe.py # Lambda function for subscribing emails to SNS
└── lambda_create_event.py # Lambda function for creating new events + updating S3 + publishing SNS


---

## ⚙️ Functionality

1. **User Flow:**
   - Open the website hosted via S3
   - Enter email and click "Subscribe"
   - Receive confirmation email from SNS
   - Confirm to be added as a subscriber

2. **Admin Flow:**
   - Enter new event name + description
   - Click "Create Event"
   - `events.json` in S3 updates automatically
   - All SNS subscribers receive the alert

---

## 🛠️ AWS Services Used

- **Amazon S3:** 
  - Hosts frontend files
  - Stores `events.json`
  
- **AWS Lambda:**
  - `SubscribeHandler`: Adds email to SNS Topic
  - `CreateEventHandler`: Publishes new event + updates `events.json`

- **API Gateway:** 
  - Connects frontend JS to backend Lambda functions via HTTPS routes

- **SNS (Simple Notification Service):** 
  - Sends emails to all subscribed users when a new event is added

---

## 🚀 How to Deploy

1. Upload frontend files to an S3 bucket with static website hosting enabled.
2. Create and deploy two Lambda functions (`SubscribeHandler`, `CreateEventHandler`).
3. Create an SNS topic and update the ARN in your Lambda.
4. Set up API Gateway with `POST /subscribe` and `POST /create` routes.
5. Enable CORS for both routes in API Gateway.
6. Link everything using correct permissions and integration.
7. Test using the hosted frontend!

---


## 🙌 Made with guidance of Ashutosh Sir


