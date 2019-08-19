# -*- coding: utf-8 -*-
"""

@author: melkarmo_ideapad
"""



from alexnet import alexnet
import numpy as np
from PIL import ImageGrab
import cv2
import time
import pyautogui
import win32api as wapi
import tensorflow as tf

# script de test du modèle

keyList = ["\b"]
for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ 123456789,.'£$/\\":
    keyList.append(char)

def key_check():
    keys = []
    for key in keyList:
        if wapi.GetAsyncKeyState(ord(key)):
            keys.append(key)
    return keys

def region_utile (img, bords):
    mask = np.zeros_like(img)
    cv2.fillPoly(mask, bords, 255)
    masked = cv2.bitwise_and(img, mask)
    return masked

def process_img(original_image):
    processed_img = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    bords = np.array([[0,640],[0,350], [275,0], [410,0], [700,350], [700,640]], np.int32)
    processed_img = region_utile(processed_img, [bords])
    return processed_img

WIDTH = 80
HEIGHT = 60
LR = 1e-3
EPOCHS = 8
MODEL_NAME = 'traffic-self-drive-{}-{}-{}-epochs-v5.model'.format(LR, 'alexnet',EPOCHS)

t_time = 0.35

def max_indice(l):
    res = 0
    for i in range(1, len(l)):
        if l[i]>l[res]:
            res = i
    return res
        
def straight():
    pyautogui.keyDown('w')
    pyautogui.keyUp('a')
    pyautogui.keyUp('d')

def left():
    pyautogui.keyDown('w')
    pyautogui.keyDown('a')
    #pyautogui.keyUp('w')
    pyautogui.keyUp('d')
    #pyautogui.keyUp('a')
    time.sleep(t_time)
    pyautogui.keyUp('a')

def right():
    pyautogui.keyDown('w')
    pyautogui.keyDown('d')
    pyautogui.keyUp('a')
    #pyautogui.keyUp('w')
    #pyautogui.keyUp('d')
    time.sleep(t_time)
    pyautogui.keyUp('d')

tf.reset_default_graph()    
model = alexnet(WIDTH, HEIGHT, LR)
model.load(MODEL_NAME)

def main():
#    last_time = time.time()
    for i in list(range(4))[::-1]:
        print(i+1)
        time.sleep(1)

    paused = False
    go = True
    
    while(go):
        
        if not paused:
            screen =  np.array(ImageGrab.grab(bbox=(10,50,700,640)))
#            print('loop took {} seconds'.format(time.time()-last_time))
#            last_time = time.time()
            screen = process_img(screen)
            screen = cv2.resize(screen, (80,60))

            prediction = model.predict([screen.reshape(80,60,1)])[0]
            moves = list(np.around(prediction))
            print(moves, prediction)

            turn_thresh = 0.5
            fwd_thresh = 0.5

            if prediction[1] > fwd_thresh:
                straight()
            elif prediction[0] > turn_thresh:
                left()
            elif prediction[2] > turn_thresh:
                right()
            else:
                straight()
            
#            if moves == [0,1,0]:
#                straight()
#            elif moves == [1,0,0]:
#                left()
#            elif moves == [0,0,1]:
#                right()
#            else:
#                straight()
                
#            ind = max_indice(prediction)
#            
#            if ind == 1:
#                straight()
#            elif ind == 0:
#                left()
#            elif ind == 2:
#                right()
#            else:
#                straight()
            
        keys = key_check()

        if 'P' in keys:
            if paused:
                paused = False
                time.sleep(1)
            else:
                paused = True
                pyautogui.keyUp('a')
                pyautogui.keyUp('w')
                pyautogui.keyUp('d')
                time.sleep(1)
                
        if 'G' in keys:
            go = False
            time.sleep(1)
            

main()       
