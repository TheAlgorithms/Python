import tensorflow as tf
from tensorflow.keras import layers, models
import numpy as np

# Load the MNIST dataset from Keras
mnist = tf.keras.datasets.mnist
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# Normalize the images from 0-255 to 0-1 by dividing by 255
X_train, X_test = X_train / 255.0, X_test / 255.0

# Print TensorFlow and Keras information
print(f"TensorFlow Version: {tf.__version__}")
print(f"Keras Layers Module: {layers.__name__}")
print(f"Keras Models Module: {models.__name__}")

# Build a simple Sequential model
model = models.Sequential()

# Flatten the 28x28 images into vectors of length 784
model.add(layers.Flatten(input_shape=(28, 28)))

# First hidden layer with 128 neurons and ReLU activation
model.add(layers.Dense(128, activation='relu'))

# Dropout layer to prevent overfitting (randomly drops 20% of neurons)
model.add(layers.Dropout(0.2))

# Second hidden layer with 64 neurons and ReLU activation
model.add(layers.Dense(64, activation='relu'))

# Output layer with 10 neurons (one for each digit class 0-9), softmax for probabilities
model.add(layers.Dense(10, activation='softmax'))

# Compile the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train the model on the MNIST training data
model.fit(X_train, y_train, epochs=5, batch_size=32)

# Evaluate the model on the test set
test_loss, test_acc = model.evaluate(X_test, y_test, verbose=2)
print(f'\nTest accuracy: {test_acc}')

# Make a prediction on a random test image
random_index = np.random.randint(0, len(X_test))
random_image = np.expand_dims(X_test[random_index], axis=0)
prediction = model.predict(random_image)
predicted_digit = np.argmax(prediction)

# Print the predicted result and actual label
print(f'Predicted digit: {predicted_digit}, Actual digit: {y_test[random_index]}')

