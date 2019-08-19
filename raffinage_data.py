# -*- coding: utf-8 -*-
"""

@author: melkarmo_ideapad
"""

# script permettant d'éliminer les données redondantes

import numpy as np
#import cv2
from random import shuffle

train_data = np.load('training_data_v5_decale.npy')

lefts = []
rights = []
forwards = []

shuffle(train_data)

for data in train_data:
    img = data[0]
    choice = data[1]
    
    if choice == [1,0,0]:
        lefts.append([img,choice])
    elif choice == [0,1,0]:
        forwards.append([img,choice])
    elif choice == [0,0,1]:
        rights.append([img,choice])
    else:
        print('no matches')
        
#    cv2.imshow('test',img)
#    print(choice)
#    if cv2.waitKey(25) & 0xFF == ord('q'):
#        cv2.destroyAllWindows()
#        break

forwards = forwards[:len(lefts)][:len(rights)]
lefts = lefts[:len(forwards)]
rights = rights[:len(forwards)]

final_data = forwards + lefts + rights
shuffle(final_data)

np.save('training_data_v5_decale_shuffled.npy', final_data)