import datetime
import pyautogui

def scope(xstart,ystart,xend,yend):
    return pyautogui.screenshot(region=[xstart,ystart,xend-xstart,yend-ystart])

def fullScreen():
    return pyautogui.screenshot()
