# AlexNet4Traffic

This project is a Python implementation of a deep learning AI able to steer a car through traffic in the game Traffic: Road Racing - Asphalt Street Cars Racer 2. https://www.microsoft.com/fr-mq/p/traffic-road-racing-asphalt-street-cars-racer-2/9nblggh11033

## Requirements

Traffic: Road Racing - Asphalt Street Cars Racer 2, downloadable for free in the Microsoft Store

Python 3
OpenCV
PyAutoGUI
Tensorflow
TFLearn

## Design

### Data structure

The data structure used in the inputs/outputs of our algorithm is a natural choice regarding the nature of the game :
* the input is processed images of the game which contains all the information about the cars' positions in traffic.
* the output is a directional key which steers the car (out of 3 : left, forward, right)

### Data processing

Two sorts of data processing have been applied to the training data :

* Since the car is most of the time going straight on the road, a big portion of our training data outputs is the forward directional key. script.py evens the 3 possible outputs in our training dataset to avoid the algorithm to converge into a a trivial straight steering algorithm.
* A delay is applied to the training dataset in order to better match the output key pressed to the input image by countering the delay that occurs while saving the training data.

### Neural network design

## Get started

## Thanks 

sentdex, alexnet
