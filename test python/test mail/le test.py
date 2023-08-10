import smtplib
import ssl
import os
import time
import pyautogui
import logging

i = 0
while i < 1000000:  
  
# on rentre les renseignements pris sur le site du fournisseur
  smtp_address = 'smtp.gmail.com'
  smtp_port = 465

# on rentre les informations de notre adresse e-mail
  email_address = 'cam.vr.850@gmail.com'
  email_password = 'ndnexbkqeivxcrqw'

# on rentre les informations sur le destinataire
  
  email_receiver = 'cam.vr.850@gmail.com'

# on crée la connexion
  context = ssl.create_default_context()
  with smtplib.SMTP_SSL(smtp_address, smtp_port, context=context) as server:
  # connexion au compte
    server.login(email_address, email_password)
  # envoi du mail
    server.sendmail(email_address, email_receiver, 'hhhhhhhhhhhaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaahhhaaaaaaaaaaaaaaaa')
    time.sleep(1)
  print("\/-_-_-|message send|-_-_-\/", i )
i = i + 1