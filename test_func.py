import os
import ctypes
import pygame

def getDisplaySize():
    user32 = ctypes.windll.user32
    screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
    return screensize

print(getDisplaySize())