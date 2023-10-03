from keras.layers import Input, Dense
from keras.models import Model

# Define the size of the encoded representation (smaller dimension compared to input)
encoding_dim = 32  # Change this according to your requirements

# Input placeholder
input_img = Input(shape=(784,))  # Assuming input data is of shape 784 (for MNIST images)

# Encoded representation of the input
encoded = Dense(encoding_dim, activation='relu')(input_img)

# Decoded representation (reconstruction of the input)
decoded = Dense(784, activation='sigmoid')(encoded)

# Autoencoder model, mapping input to its reconstruction
autoencoder = Model(input_img, decoded)

# Separate encoder model (for encoding input)
encoder = Model(input_img, encoded)

# Placeholder for encoded input
encoded_input = Input(shape=(encoding_dim,))

# Decoder layer for the encoded input
decoder_layer = autoencoder.layers[-1]

# Decoder model (mapping encoded input to the reconstruction)
decoder = Model(encoded_input, decoder_layer(encoded_input))

# Compile the autoencoder model
autoencoder.compile(optimizer='adam', loss='binary_crossentropy')

# Now, you can train the autoencoder using your data
# For example, if you have MNIST data:
# (x_train, _), (x_test, _) = mnist.load_data()
# x_train = x_train.astype('float32') / 255.
# x_test = x_test.astype('float32') / 255.
# x_train = x_train.reshape((len(x_train), np.prod(x_train.shape[1:])))
# x_test = x_test.reshape((len(x_test), np.prod(x_test.shape[1:])))

# Train the autoencoder
# autoencoder.fit(x_train, x_train, epochs=50, batch_size=256, shuffle=True, validation_data=(x_test, x_test))

# After training, you can use the encoder and decoder models to encode/decode data.
# encoded_imgs = encoder.predict(x_test)
# decoded_imgs = decoder.predict(encoded_imgs)
