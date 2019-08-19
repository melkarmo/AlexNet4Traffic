# -*- coding: utf-8 -*-
"""

@author: melkarmo_ideapad
"""

# script permettant de décaler les images et les actions d'entrée afin d'anticiper le mouvement du véhicule

import numpy as np

train_data = np.load('training_data_v5.npy')

new_data = []

for i in range(train_data.shape[0]-1):
    img = train_data[i][0]
    choice = train_data[i+1][1]
    new_data.append([img,choice])
        
np.save('training_data_v5_decale.npy', new_data)