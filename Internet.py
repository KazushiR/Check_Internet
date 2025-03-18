import smtplib, os
from dotenv import load_dotenv, dotenv_values

#this short script is run on a cront job. It sends emails every 5 minutes and 
# the check_file_for_internet.py checks to see if it recieves the messages sent by this script every 10 minutes from an external server.

load_dotenv()

message = os.getenv("message_1")
sender = os.getenv("sender")
recipients = os.getenv("recipients")
password = os.getenv("password_1")

def send_email( message, sender,recipients, password):
    with smtplib.SMTP("smtp.gmail.com", 587) as s:
        s.starttls()
        s.login(sender, password)
        s.sendmail(sender, recipients, message)
        s.quit()
        print("It worked!")

send_email( message, sender, recipients, password)