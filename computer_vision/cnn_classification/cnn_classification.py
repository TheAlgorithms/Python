
"""
Convolutional Neural Network

Objective : To train a CNN model detect if TB is present in Lung X-ray or not.

Resources : https://en.wikipedia.org/wiki/Convolutional_neural_network

Download dataset from :
https://lhncbc.nlm.nih.gov/LHC-publications/pubs/TuberculosisChestXrayImageDataSets.html

"""

# Part 1 - Building the CNN

# Importing the Keras libraries and packages
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator

import numpy as np


# Initialising the CNN
classifier = Sequential()

# Step 1 - Convolution
classifier.add(Conv2D(32, (3, 3), input_shape=(64, 64, 3), activation="relu"))

# Step 2 - Pooling
classifier.add(MaxPooling2D(pool_size=(2, 2)))

# Adding a second convolutional layer
classifier.add(Conv2D(32, (3, 3), activation="relu"))
classifier.add(MaxPooling2D(pool_size=(2, 2)))

# Step 3 - Flattening
classifier.add(Flatten())

# Step 4 - Full connection
classifier.add(Dense(units=128, activation="relu"))
classifier.add(Dense(units=1, activation="sigmoid"))

# Compiling the CNN
classifier.compile(optimizer="adam",
                   loss="binary_crossentropy", metrics=["accuracy"])

# Part 2 - Fitting the CNN to the images


# Load Trained model weights

# from keras.models import load_model
# regressor=load_model('cnn.h5')

train_datagen = ImageDataGenerator(
    rescale=1.0 / 255, shear_range=0.2, zoom_range=0.2, horizontal_flip=True
)

test_datagen = ImageDataGenerator(rescale=1.0 / 255)

training_set = train_datagen.flow_from_directory(
    "dataset/training_set", target_size=(64, 64), batch_size=32,
    class_mode="binary"
)

test_set = test_datagen.flow_from_directory(
    "dataset/test_set", target_size=(64, 64), batch_size=32,
    class_mode="binary"
)

classifier.fit_generator(
    training_set, steps_per_epoch=5, epochs=30, validation_data=test_set
)

classifier.save("cnn.h5")

# Part 3 - Making new predictions


test_image = image.load_img("dataset/single_prediction/image.png",
                            target_size=(64, 64))
test_image = image.load_img(image, target_size=(64, 64))
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis=0)
result = classifier.predict(test_image)
training_set.class_indices
if result[0][0] == 0:
    prediction = "Normal"
if result[0][0] == 1:
    prediction = "Abnormality detected"
