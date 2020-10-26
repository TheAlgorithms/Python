'''
We will create an ANN to output the class of a wheat seed based on 7 numerical inputs,
there is a total of 3 classes on the wheat-seeds.csv dataset, and our ANN with fully
connected Dense layers, will predict the class of the inputs.
Data src: https://raw.githubusercontent.com/jbrownlee/Datasets/master/wheat-seeds.csv
Our ANN is made with the tensorflow 2.0 keras API.
Input example:
15.26,14.84,0.871,5.763,3.312,2.221,5.22
Output example:
1
Our model will predict the class, as its seen on the input and output example.
'''


#We read the libraries
import pandas as pd
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.callbacks import EarlyStopping
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler,LabelEncoder
from sklearn.metrics import confusion_matrix, classification_report
from tensorflow.keras.utils import to_categorical
import matplotlib.pyplot as plt

#We read the csv file
dataset = pd.read_csv('wheat-seeds.csv')
#We rename our columns and get X and Y 
dataset.columns = ['t1','t2','t3','t4','t5','t6','t7','class']
X = dataset.drop(['class'],axis=1)
Y = dataset['class']
#We encode Y
encoder = LabelEncoder()
encoder.fit(Y)
encoded_labels = encoder.transform(Y)
cat_y = to_categorical(encoded_labels,dtype='float64')
#We create the model
X_train, X_test, y_train, y_test = train_test_split(X, cat_y, test_size=0.2, random_state=10)
model = Sequential()
model.add(Dense(7,activation='relu'))
model.add(Dense(6,activation='relu'))
model.add(Dense(6,activation='relu'))
model.add(Dense(3,activation='softmax'))
model.compile(loss='categorical_crossentropy',optimizer='adam')
#We create an early stop call
early_stop = EarlyStopping(monitor='val_loss',mode='min',patience=20)
#We train the model for 50 epochs
model.fit(X_train,y_train,epochs=500,batch_size=32,callbacks=[early_stop],validation_data=(X_test,y_test))
#We plot the model's loss history
history = pd.DataFrame(model.history.history)
plt.style.use('dark_background')
history.plot()
plt.show()