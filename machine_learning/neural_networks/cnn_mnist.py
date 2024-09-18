"""
Convolutional Neural Network (CNN) for MNIST Classification

Goal: This script builds a deep CNN to classify the MNIST dataset using
    TensorFlow and Keras. It leverages convolutional layers for feature
    extraction and pooling layers for down-sampling, followed by fully
    connected layers for classification.

Objectives:
- Load and preprocess MNIST data (reshape for CNN input).
- Build a CNN with multiple convolutional, pooling, and batch normalization layers.
- Train the CNN, evaluate its accuracy, and display model performance.

"""

# import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical

# Load and preprocess the MNIST data
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Normalize the pixel values (0 to 1)
x_train = x_train.reshape(-1, 28, 28, 1).astype("float32") / 255
x_test = x_test.reshape(-1, 28, 28, 1).astype("float32") / 255

# Convert labels to one-hot encoding
y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)

# Building the CNN model
model = models.Sequential()

# 1st Convolutional Layer
model.add(layers.Conv2D(32, (3, 3), activation="relu", input_shape=(28, 28, 1)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.BatchNormalization())

# 2nd Convolutional Layer
model.add(layers.Conv2D(64, (3, 3), activation="relu"))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.BatchNormalization())

# 3rd Convolutional Layer
model.add(layers.Conv2D(128, (3, 3), activation="relu"))
model.add(layers.BatchNormalization())

# Flattening the data before fully connected layers
model.add(layers.Flatten())

# Fully Connected (Dense) Layer with Dropout for regularization
model.add(layers.Dense(128, activation="relu"))
model.add(layers.Dropout(0.5))

# Output Layer for classification
model.add(layers.Dense(10, activation="softmax"))

# Compile the model
model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])

# Display the model summary
model.summary()

# Train the model
history = model.fit(
    x_train, y_train, epochs=5, batch_size=32, validation_data=(x_test, y_test)
)

# Evaluate the model on test data
test_loss, test_acc = model.evaluate(x_test, y_test, verbose=2)
print(f"\nTest accuracy: {test_acc}")
