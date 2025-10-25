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