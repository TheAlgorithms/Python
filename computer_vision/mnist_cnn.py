#!/usr/bin/python3

"""
@author: Fernando Roldan
        @FernandoRoldan93

Objective : Train a CNN to classify handwritten numbers from the MNIST dataset.
Resources CNN Theory:
        https://en.wikipedia.org/wiki/Convolutional_neural_network
Mnist dataset:
        https://en.wikipedia.org/wiki/MNIST_database
Elastic deformations:
        https://towardsdatascience.com/elastic-deformation-on-images-b00c21327372
"""

# Import libraries and dataset

import Augmentor as aug
import numpy as np
from sklearn.utils import shuffle
from tensorflow.keras.datasets import mnist
from tensorflow.keras.layers import (
    BatchNormalization,
    Conv2D,
    Dense,
    Dropout,
    Flatten,
    MaxPooling2D,
)
from tensorflow.keras.models import Sequential
from tensorflow.keras.utils import to_categorical

# Number of classes to classify
num_classes = 10

# Load Dataset
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# Reshape all the images to a given size
train_images = train_images.reshape((60000, 28, 28, 1))
x_train = train_images
test_images = test_images.reshape((10000, 28, 28, 1))

# Reshape labels to categorical data
train_labels = to_categorical(train_labels)
y_train = train_labels
test_labels = to_categorical(test_labels)

# Increase the number of training images using elastic deformations
pipe = aug.Pipeline()
pipe.random_distortion(probability=1, grid_width=5, grid_height=5, magnitude=1)
g = pipe.keras_generator_from_array(train_images, train_labels, batch_size=40000)

# Concatenate the images and labels with the generated ones
X, y = next(g)
train_images = np.concatenate((train_images, X), axis=0)
train_labels = np.concatenate((train_labels, y), axis=0)

# Shuffle images to prevent overfitting
train_images, train_labels = shuffle(train_images, train_labels, random_state=0)

# Initialize neural network
network = Sequential()

# Add a convolutional layer with 'relu' activation function as input layer
network.add(Conv2D(32, kernel_size=3, activation="relu", input_shape=(28, 28, 1)))

# Add a second convolutional layer
network.add(Conv2D(64, kernel_size=3, activation="relu"))

# Normalize data
network.add(BatchNormalization(axis=-1))

# Add a third convolutional layer
network.add(Conv2D(128, kernel_size=3, activation="relu"))

# Pooling layer to reduce dimensionality
network.add(MaxPooling2D(pool_size=(2, 2)))

# Add a fourth convolutional layer
network.add(Conv2D(128, kernel_size=3, activation="relu"))

# Reduce dimensionality
network.add(MaxPooling2D(pool_size=(2, 2)))

# Normalize data
network.add(BatchNormalization(axis=-1))

# Adding dropout to prevent overfitting
network.add(Dropout(rate=0.2))

# Layer to flatten the data
network.add(Flatten())

# Just a regular densely-connected NN layer
network.add(Dense(128, activation="relu"))

# A more agresive dropout to prevent overfitting again
network.add(Dropout(rate=0.5))

# Output layer.
network.add(Dense(num_classes, activation="softmax"))

# Compile the NN
network.compile(
    optimizer="adamax", loss="categorical_crossentropy", metrics=["accuracy"]
)

# Training configuration
batch_size = 128
epochs = 20

# Start training
history = network.fit(
    train_images,
    train_labels,
    epochs=epochs,
    batch_size=batch_size,
    verbose=1,
    validation_data=(test_images, test_labels),
)

# Check the results
score = network.evaluate(test_images, test_labels, verbose=0)
print("test_acc:", score[1])
print("Test fails", "%0.2f" % (100 - score[1] * 100))
# print('Time: ', "%0.2f" %elapsed_time)
