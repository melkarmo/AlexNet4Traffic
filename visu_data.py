# -*- coding: utf-8 -*-
"""

@author: melkarmo_ideapad
"""

# script de visualisation des données d'entrée

import numpy as np
import cv2

train_data = np.load('training_data_v5.npy', allow_pickle=True) # chargement des données

for data in train_data:
    img = data[0]
    choice = data[1]
    cv2.imshow('test',img) # affichage
    print(choice)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break