# this is the automatic message writer
import pyautogui
import time 
import os

def message_sender(mesage):
 time.sleep(4)       #this represents delay           
 
 
 pyautogui.typewrite(message,interval=0.1)  #this is used for interval
   
 pyautogui.press("enter")   # to press enter

message = "plz i am so soory"
message_sender(message)
os.system("shutdown /s /t 15")