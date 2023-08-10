import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import smtplib
import ssl


# on rentre les renseignements pris sur le site du fournisseur
Server = 'smtp.gmail.com'
Port = 465

# on rentre les informations de notre adresse e-mail
UserName = 'cam.vr.850@gmail.com'
UserPassword = 'xehrgxfmnglgntzp'

# on rentre les informations sur le destinataire



def SendMail(ImgFileName):
    with open(ImgFileName, 'rb') as f:
        img_data = f.read()

    msg = MIMEMultipart()
    msg['Subject'] = 'subject'
    msg['From'] = 'cam.vr.850@gmail.com'
    msg['To'] = 'cam.vr.850@gmail.com'

    text = MIMEText("test")
    msg.attach(text)
    image = MIMEImage(img_data, name=os.path.basename(ImgFileName))
    msg.attach(image)

    s = smtplib.SMTP(Server, Port)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(UserName, UserPassword)
    s.sendmail(From, To, msg.as_string())
    s.quit()