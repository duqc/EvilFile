#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      amanz
#
# Created:     02-11-2022
# Copyright:   (c) amanz 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from tkinter import *
import tkinter
import math
import time
import pyautogui
import keyboard
import random

x = 0
ROOT = Tk()
ROOT.attributes('-topmost',True)
ROOT.overrideredirect(1)
ROOT.wm_attributes('-transparentcolor', ROOT['bg'])


# Position image
LABEL = Label(ROOT, text="This is what hell is like", font=('Comic Sans MS', 30, 'bold italic'))


pyautogui.PAUSE = 0

LABEL.pack()
LOOP_ACTIVE = True
while LOOP_ACTIVE:
    x += 1

    pos = pyautogui.position()

    print (pos[0],pos[1])


    x1 = x
    r_w = (pos[0]-150) - math.sin(x1/32)*300
    r_w1 = int(r_w)

    r_h = (pos[1]-20) - (math.cos(x1/32)*(math.sin(x1/32)))*300
    r_h1 = int(r_h)

    ROOT.bind('<Escape>', lambda e: CloseLoop())

    if keyboard.is_pressed('esc'):
        break



    ROOT.geometry(str(600)+"x"+str(40)+"+"+str(r_w1)+"+"+str(r_h1))
    ROOT.update()

    pyautogui.moveRel(random.randint(-50,50),random.randint(-50,50))

    #DO NOT GET RID OF THIS LINE OF CODE PLEASE
    time.sleep(0.01)

ROOT.destroy()


