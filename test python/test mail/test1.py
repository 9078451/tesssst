import json 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

msg = MIMEMultipart()
message = "This is an email"

password = "Canard28"
msg['From'] = "cam.vr@yahoo.com"
msg['To'] = "cam.vr.850@gmail.com"
msg['Subject'] = "Title of email"

msg.attach(MIMEText(message, 'plain'))
server = smtplib.SMTP('smtp.mail.yahoo.com:465')
server.starttls()
server.login(msg['From'], password)
server.sendmail(msg['From'], msg['To'], msg.as_string())
server.quit()
