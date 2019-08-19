# -*- coding: utf-8 -*-
"""

@author: melkarmo_ideapad
"""

import numpy as np
from PIL import ImageGrab
import cv2
import time
import win32api as wapi
import os

# Création des données d'apprentissage

keyList = ["\b"]
for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ 123456789,.'£$/\\":
    keyList.append(char)

def key_check():
    keys = []
    for key in keyList:
        if wapi.GetAsyncKeyState(ord(key)):
            keys.append(key)
    return keys

def keys_to_output(keys):
    #[A, W, D]
    output = [0, 0, 0]
    
    if 'A' in keys:
        output[0] = 1
    elif 'D' in keys:
        output[2] = 1
    else:
        output[1] = 1
        
    return output

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

file_name = 'training_data_v5.npy'

if os.path.isfile(file_name):
    print('File exists, loading previous data!')
    training_data = list(np.load(file_name))
else:
    print('File does not exist, starting fresh!')
    training_data = []


def main(): 
    
    print(len(training_data))
    
    for i in list(range(4))[::-1]:
        print(i+1)
        time.sleep(1)
        
#    last_time = time.time()
    
    paused = False
    go = True
    
    while(go):
        
        if not paused:
            
            screen = np.array(ImageGrab.grab(bbox=(10,50,700,640)))
            screen = process_img(screen)
            screen = cv2.resize(screen, (80,60))
        
            keys = key_check()
            output = keys_to_output(keys)
            training_data.append([screen,output])
        
#            print('Frame took {} seconds'.format(time.time()-last_time))
#            last_time = time.time()
        
            if len(training_data) % 100 == 0:
                    print(len(training_data))
                    np.save(file_name,training_data)
        
#            cv2.imshow('window', screen)
#            if cv2.waitKey(25) & 0xFF == ord('q'):
#                cv2.destroyAllWindows()
#                break
        
        keys = key_check()
        
        if 'P' in keys:
            if paused:
                paused = False
                print("depaused")
                time.sleep(1)
            else:
                paused = True
                print("paused")
                time.sleep(1)
                
        if 'G' in keys:
            go = False
            time.sleep(1)

main()
