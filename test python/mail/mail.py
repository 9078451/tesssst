import smtplib
import ssl
import os
import time
import pyautogui
import logging

#mathis.decoster@gmail.com
#nuze.ytb@gmail.com


#logging.basicConfig(level=logging.CRITICAL,
#                    filename="mail\lbc\crash.txt",
#                    filemode="a",
#                    format='%(asctime)s - %(levelname)s - %(message)s')
#logging.critical("--------------------------------")
#logging.critical("|       oups sa a  crash       |")
#logging.critical("--------------------------------")


#---------------------------------------------------------------------------

logging.basicConfig(level=logging.DEBUG,
                    filename="mail\lbc\debug.txt",
                    filemode="a",
                    format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug("--------------------------------")
logging.debug("|         message debug        |")
logging.debug("--------------------------------")

i = 0
while i < 1000000:  
  
# on rentre les renseignements pris sur le site du fournisseur
  smtp_address = 'smtp.gmail.com'
  smtp_port = 465

# on rentre les informations de notre adresse e-mail
  email_address = 'cam.vr.850@gmail.com'
  email_password = 'tdzmlnkirwlsrpua'

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
    logging.debug("MSG send")
    logging.debug("----------------------------------------------------------")
  print("\/-_-_-|message send|-_-_-\/")
i = i + 1