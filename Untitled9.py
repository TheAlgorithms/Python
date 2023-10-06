#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import tensorflow as tf
from tensorflow import keras
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score


# In[3]:


X, y = np.random.rand(1000, 10), np.random.randint(0, 2, size=(1000,))

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# In[4]:


# Standardize the data (z-score normalization)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


# In[9]:


# Define the MLP model using TensorFlow/Keras with additional hidden layers and regularization
model = keras.Sequential([
    keras.layers.Dense(128, activation='relu', input_shape=(X_train.shape[1],)),
    keras.layers.BatchNormalization(),  # Add batch normalization
    keras.layers.Dropout(0.5),  # Add dropout for regularization
    keras.layers.Dense(64, activation='relu'),
    keras.layers.BatchNormalization(),  # Add batch normalization
    keras.layers.Dropout(0.5),  # Add dropout for regularization
    keras.layers.Dense(32, activation='relu'),
    keras.layers.Dense(16, activation='relu'),
    keras.layers.Dense(1, activation='sigmoid')
])


# In[10]:


# Increase the learning rate
optimizer = keras.optimizers.Adam(learning_rate=0.01)  # Adjust the learning rate


# In[16]:


# Compile the model with the increased learning rate
model.compile(optimizer=optimizer,
              loss='binary_crossentropy',
              metrics=['accuracy'])

# Implement early stopping with patience
early_stopping = keras.callbacks.EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)

# Train the model with early stopping
model.fit(X_train, y_train, epochs=40, batch_size=32, verbose=2, validation_split=0.2, callbacks=[early_stopping])

# Make predictions
y_pred = model.predict(X_test)
y_pred_binary = (y_pred > 0.5).astype(int)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred_binary)
print("Accuracy:", accuracy)


# In[ ]:





# In[ ]:




