from email.mime.text import MIMEText
import smtplib
import ssl
import json

with open("details.json", "r"):
    data = json.load(open("details.json"))
password = data["password"]
sender_email = data["sender_email"]
receiver_email = input("Enter receiver email: ")
subject = data["subject"]
body = data["body"]

message = MIMEText(body, "plain")
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

context = ssl.create_default_context()
print("sending email")
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())
print("email sent")
