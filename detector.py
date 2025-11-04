import re

def check_email(subject, message):
   print(f"\n Subject: {subject}")
   print(f"Message: {message} \n")
   problem = []
   
   urgent_words = ["urgent", "immediately", "alert", "verify now"]
   for word in urgent_words:
      if word in subject.lower():
         problem.append(f"Urgent Word: {word}")
   
   if 'password' in message.lower():
      problem.append("Asking for password")
      
   if '.tk' in message or '.ml' in message:
      problem.append("Suspicious website link")
      
   if 'won' in message.lower() and 'price' in message.lower():
      problem.append("'You won a prize' - common scam")
      
   # Extract all URLs from the message
   urls = re.findall(r'https?://[^\s]+', message)
   if urls:
        print("Found URLs in message:")
        for u in urls:
            print("   -", u)
        # Optionally flag them for review
        problem.append(f"{len(urls)} URL(s) detected in message")
   
   if problem:
      for prob in problem:
         print(f" - {prob}")
   else:
      print("Email looks safe!")
      
   return problem


if __name__ == "__main__":
   email_subject = input("Enter email subject: ")
   email_message = input("Enter email message: ")

   check_email(email_subject, email_message)