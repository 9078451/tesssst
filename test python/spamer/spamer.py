import time
import requests
from discord import SyncWebhook, File, Webhook # Import SyncWebhook
import smtplib
import ssl
 
# on rentre les renseignements pris sur le site du fournisseur
smtp_address = 'smtp.gmail.com'
smtp_port = 465

# on rentre les informations de notre adresse e-mail
email_address = 'cam.vr.850@gmail.com'
email_password = 'ndnexbkqeivxcrqw'

# on rentre les informations sur le destinataire
  
email_receiver = 'cam.vr.850@gmail.com'
#v print 
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

im = input('Webhook-->')
re = input('MSG--->')
context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_address, smtp_port, context=context) as server:
  # connexion au compte
    server.login(email_address, email_password)
  # envoi du mail
    server.sendmail(email_address, email_receiver, "NVU du spame")
run = True

while run:
    Webhook = im
    time.sleep(1)
    p(re)
    time.sleep(1)
    requests.post(im, json={'content': re})