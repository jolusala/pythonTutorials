from email.message import EmailMessage
from multiprocessing import context
import ssl
import smtplib



email_Sender = "jose.luissalacast@gmail.com"
email_password = ""

email_receiver = "bikkofudri@vusra.com"

subject = "Dont forget to subscribe"
body = "When you watch a video, please give a like"

em = EmailMessage()
em['From'] = email_Sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
    smtp.login(email_Sender,email_password)
    smtp.sendmail(email_Sender,email_receiver,em.as_string())
