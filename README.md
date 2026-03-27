# 🚀 AWS File Upload System (Event-Driven)

## 📌 Overview
This project demonstrates an event-driven architecture using AWS.

When a file (any type) is uploaded to an S3 bucket, it automatically triggers a Lambda function, which processes the file and sends an email notification using SNS.

---

## 🧩 Services Used
- Amazon S3
- AWS Lambda
- Amazon SNS
- Amazon CloudWatch (for logging and monitoring Lambda execution)

---

## ⚙️ Architecture
User Upload → S3 Bucket → Lambda Trigger → SNS → Email Notification

---

## 🧪 Features
- Automatic file processing
- Real-time email notification
- Serverless architecture

---

## 📷 Output
- Logs show uploaded file details
- Email notification sent on upload

---

## ⚠️ Challenges Faced
- Understanding how to connect S3 events with Lambda triggers  
- Difficulty in locating and attaching correct IAM permissions for SNS  
- Debugging why email notifications were not being received (SNS subscription confirmation issue)  
- Identifying correct SNS Topic ARN and integrating it into Lambda code  
- Initial confusion navigating AWS console (UI complexity for beginners)  

---

## 📚 Key Learnings
- Learned how event-driven architecture works in real cloud systems  
- Understood how AWS services interact automatically without manual intervention  
- Gained hands-on experience with IAM roles and permissions management  
- Learned to debug using CloudWatch logs effectively  
- Understood the importance of correct configuration (ARN, permissions, triggers)  
- Built confidence in working with multiple AWS services together  

---

## 🚀 Future Improvements
- Store metadata in DynamoDB  
- Filter file types  
- Add frontend UI  
