# AlexNet4Traffic

This project is a Python implementation of a deep learning AI able to steer a car through traffic in the game [Traffic: Road Racing - Asphalt Street Cars Racer 2](https://www.microsoft.com/fr-mq/p/traffic-road-racing-asphalt-street-cars-racer-2/9nblggh11033).

![Sans titre3](https://user-images.githubusercontent.com/35910546/63232567-434bce80-c229-11e9-9cb0-5145c781b0cc.png)

## Requirements

* **Traffic: Road Racing - Asphalt Street Cars Racer 2** *(downloadable for free at the [Microsoft Store](https://www.microsoft.com/fr-mq/p/traffic-road-racing-asphalt-street-cars-racer-2/9nblggh11033))*
* Python 3
* OpenCV
* PyAutoGUI
* Tensorflow
* TFLearn

## Design

### Data structure

The data structure used in the inputs/outputs of our algorithm is a natural choice regarding the nature of the game :
* the input is processed images of the game which contains all the information about the cars' positions in traffic
* the output is a directional key which steers the car (out of 3 : left, forward, right)

<p align="center">
  <img src="https://user-images.githubusercontent.com/35910546/63232568-434bce80-c229-11e9-815b-b0ac51fb457e.png" width="400">
</p>

### Data processing

Two sorts of data processing have been applied to the training data :
* Since the car is most of the time going straight on the road, a big portion of our training data outputs is the forward directional key. `raffinage_data.py` evens the 3 possible outputs in our training dataset to avoid the algorithm to converge into a a trivial straight steering algorithm
* A delay is applied to the training dataset in order to better match the output key pressed to the input image by countering the delay that occurs while saving the training data

### Neural network design

Since our inputs are images, a naturel choice was the use of a convolutional neural network. The architecture used is [AlexNet](https://en.wikipedia.org/wiki/AlexNet) (5 convolutional layer + 3 fully connected layers) for its effectiveness and easiness to implement using TensorFlow.

![Sans titre2](https://user-images.githubusercontent.com/35910546/63232569-434bce80-c229-11e9-8b33-f0348d1207d8.png)

## Get started

1. Start the Traffic game
2. Run `enreg_fenetre.py` to correctly position manually the game's windows in the OpenCV screenshot zone
3. Run `create_training_data.py` to begin recording training data while playing the game
4. Run `decale_data.py` to apply the delay to the training data for anticipation matters
5. Run `raffinage_data.py` to delete the excess of straight-driving training data
6. Run `train_model.py` to initialize the model and begin its training using the processed data
7. Run `test_model.py` to test the model on the game


## Thanks 

This project was inspired by [sentdex](https://www.youtube.com/user/sentdex)'s [Python plays GTA V](https://www.youtube.com/playlist?list=PLQVvvaa0QuDeETZEOy4VdocT7TOjfSA8a) series on youtube, keep up your amazing work :+1:  
Big thanks to Alex Krizhevsky for the AlexNet architecture :clap:
