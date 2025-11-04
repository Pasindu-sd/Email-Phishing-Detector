# Email Phishing Detector

A simple Python tool to detect phishing attempts in emails.

### Features
- Checks email subjects for urgency tactics
- Analyzes email body for suspicious content  
- Verifies sender information
- Detects common phishing patterns
- Calculates risk score

### How to Use
1. Run the program: `detector.py`
2. Choose to check manual email or test samples
3. Enter email details when prompted
4. Get instant phishing analysis

### What It Detects
- Urgent language ("ACT NOW!")
- Requests for personal information
- Suspicious links and domains
- Poor grammar and scam phrases
- Free email providers used for business

---
### Example 1:
```
Enter email subject: Urgent! Verify your password now
Enter email message: Dear user, your account will be suspended immediately! 

 Subject: Urgent! Verify your password now
Message: Dear user, your account will be suspended immediately!  

 - Urgent Word: urgent
```
---
### Example 2:
```
Enter email subject: Urgent! Verify your password now
Enter email message: Hi team, here is the meeting link: https://meet.google.com/abc-xyz

 Subject: Urgent! Verify your password now
Message: Hi team, here is the meeting link: https://meet.google.com/abc-xyz 

Found URLs in message:
   - https://meet.google.com/abc-xyz

Potential Issues Found:
 - Urgent Word: urgent
 - 1 URL(s) detected in message
```
