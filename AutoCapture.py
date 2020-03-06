import numpy as np
import pyautogui
import imutils
import cv2
import time
from PIL import Image


x = 1
Name = input('Enter book name : ')
time.sleep(5)
images = []
NumPages = int(input('Enter num of pages'))

for z in range(1,NumPages):
    time.sleep(1)
    image = pyautogui.screenshot(region=(650,130, 610, 840))
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    cv2.imwrite(f"{x}.png", image)
    x = x+1
    pyautogui.press('right')

im1 = Image.open('1.png')

for c in range(2,NumPages+1):
    im = Image.open(f'{c}.png')
    images.append(im.convert('RGB'))
im1.save(f'{Name}.pdf',save_all=True, append_images=images)




   