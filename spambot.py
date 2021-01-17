import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

msg = MIMEMultipart('related')

#data needs to be inserted
email = #data
password = #data
receiver = #data

msg['From'] = email
msg['To'] = ", ".join(receiver)

port = 465
sslcontext = ssl.create_default_context()

fp = open('#data', 'rb')
#takes the image from the PythonProject folder
msgImage = MIMEImage(fp.read())
msg.attach(msgImage)

#example for gmail
for i in range(0, 1000):
    connection = smtplib.SMTP_SSL("smtp.gmail.com", port, context=sslcontext)
    connection.login(email, password)
    connection.sendmail(email, receiver, msg.as_string())
    print("Sent!")
