import smtplib, ssl
import os

def send_email(message):
    host = "smtp.gmail.com" 
    port = 465

    username = "231lukecurran@gmail.com"
    password = os.getenv("PASSWORD")
    reciever = "231lukecurran@gmail.com"

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, reciever, message)