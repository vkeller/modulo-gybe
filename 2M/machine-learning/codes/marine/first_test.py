## ===========================
## ===========================
## Code from : https://medium.com/@zeniaharis1/building-an-ai-image-classification-model-using-python-and-convolutional-neural-networks-07bf9c732f9c
## ===========================
## ===========================


import sys 
# sys is a module that gives me access to a lot of variables and functions

from keras.src.datasets import (cifar10) 
# This will import cifar10 (dataset) from keras to my code. 
# CIFAR-10 is a popular data set of 60,000 small 32x32 images

from tensorflow.keras import (datasets, layers, models) 
# This will import datasets like CIFAR-10, MINST.
# Layers are used to build neural network layers (e.g., convolutional layers, pooling layers).
# Models are used to construct, compile, and train neural network models. 

print(sys.executable)
# This prints the path being used by the python interpreter, it'll show up when I run the code!

import cv2 as cv
# Imports OpenCV (labeled as cv), 
# OpenCV is a library for image and video processing tasks, like reading and showing images.

import numpy as np
# Imports NumPy, a library for numerical computations in Python. 
# Often used for handling data arrays.

import matplotlib.pyplot as plt
# Imports Matplotlib's pyplot module as 'plt', 
# This is used for data visualization, 
# like plotting images, graphs, and training performance metrics.

from tensorflow.keras.preprocessing.image import ImageDataGenerator
# The image data generator helps augment training data by rotating, shifting, or flipping images to prevent overfitting
# Imports ImageDataGenerator from TensorFlow’s Keras. 
# This tool generates batches of image data with real-time data augmentation. 
# This is helpful in increasing the size and variety of training data.

(training_images, training_labels), (testing_images, testing_labels) = cifar10.load_data()
# Loading the CIFAR-10 dataset

training_images, testing_images = training_images / 255.0, testing_images / 255.0
# Normalize the pixel values to be between 0 and 1

datagen = ImageDataGenerator(
    rotation_range=15,
    width_shift_range=0.1,
    height_shift_range=0.1,
    horizontal_flip=True
)

datagen.fit(training_images)
# Fit the data generator to our training images  
# For certain augmentations, like normalization, the generator needs to understand the properties of the dataset

class_names = ['Plane', 'Car', 'Bird', 'Cat', 'Deer', 'Dog', 'Frog', 'Horse', 'Ship', 'Truck']
# Each category is the name of a class (or category) in the CIFAR-10 dataset. 
# CIFAR-10 has 10 classes, and each class corresponds to an index.

for i in range(16):
# This starts a loop to show the first 16 images from the 'training_images' dataset.
# The range 16 means the loop will iterate 16 times (i.e., i goes from 0 to 15).

    plt.subplot(4, 4, i+1)
# This makes a 4x4 grid used to display 16 images in a 4x4 layout.

    plt.xticks([])
    plt.yticks([])
# This removes the x-axis and y-axis tick marks, giving a cleaner look to the image.

    plt.imshow(training_images[i], cmap=plt.cm.binary)
# This converts the images to grayscale for display

    plt.xlabel(class_names[training_labels[i][0]])
# This sets the x-axis label below each image to the class name corresponding to training_labels[i][0]. 
# For example, if training_labels[i][0] is 3, it will display "Cat" because class_names[3] is "Cat".

plt.show()
# This just shows the result

training_images = training_images[:50000]
training_labels = training_labels[:50000]
testing_images = testing_images[:10000]
testing_labels = testing_labels[:10000]

model = models.Sequential()
# This starts a model which lets you stack layers in sequence.

model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)))
model.add(layers.MaxPooling2D((2, 2)))

model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))

model.add(layers.Conv2D(64, (3, 3), activation='relu'))

model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))

model.add(layers.Dense(10, activation='softmax'))


model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
# This prepares the model for training by specifying the optimizer, loss function, and metrics.

model.fit(training_images, training_labels, epochs=10, validation_data=(testing_images, testing_labels))
# This is the function used to train the model on the data.

loss, accuracy = model.evaluate(testing_images, testing_labels)

print(f"loss: {loss}")
print(f"Accuracy: {accuracy}")
# this will just print the measurements in the terminal

