# -*- coding: utf-8 -*-
"""

@author: melkarmo_ideapad
"""

# script pour visualiser la fenêtre de capture

import numpy as np
from PIL import ImageGrab
import cv2
import time
import pyautogui

def region_utile (img, bords):
    mask = np.zeros_like(img)
    cv2.fillPoly(mask, bords, 255)
    masked = cv2.bitwise_and(img, mask)
    return masked

def process_img(original_image):
    processed_img = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
#    processed_img = cv2.Canny(processed_img, threshold1=200, threshold2=300)
#    processed_img = cv2.GaussianBlur(processed_img, (3,3), 0 )
    bords = np.array([[0,640],[0,350], [275,0], [410,0], [700,350], [700,640]], np.int32)
    processed_img = region_utile(processed_img, [bords])
    return processed_img

def test_key_a():
    for i in list(range(6))[::-1]:
        print(i+1)
        time.sleep(1)
    pyautogui.keyDown('a')
    time.sleep(4)
    pyautogui.keyUp('a')

def main(): 
    last_time = time.time()
    while(True):
        screen =  np.array(ImageGrab.grab(bbox=(10,50,700,640)))
        new_screen = process_img(screen)
        print('loop took {} seconds'.format(time.time()-last_time))
        last_time = time.time()
        cv2.imshow('window', new_screen)
        #cv2.imshow('window',cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

main()
#test_key_a()