import smtplib
from email.mime.text import MIMEText

body = "THIS IS A  TEST EMAIL. HOW ARE YOU?"

msg = MIMEText(body)
msg['From']= "myapp2601@gmail.com"
msg['To'] = "manjeetharyani1008@gmail.com"

msg['Subject'] = "Hello"

server = smtplib.SMTP('smtp.gmail.com',587)

server.starttls()

server.login("xyz@gmail.com","yourpassword")

server.send_message(Msg)

print("Mail sent")

server.quit()