import datetime
import pywhatkit as kit
import time
import keyboard
import os



class Bot:
    def send_message(self, destination, message):
        tm = datetime.datetime.now().time()
        kit.sendwhatmsg("+7" + destination, message, tm.hour, tm.minute + 1, 35)
        time.sleep(2)
        keyboard.press_and_release('ctrl + w')
        os.system("taskkill /im chrome.exe /f")