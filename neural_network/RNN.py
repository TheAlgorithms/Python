import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.utils import np_utils

#Read the data, turn it into lower case
data = open("Othello.txt").read().lower()
#This get the set of characters used in the data and sorts them
chars = sorted(list(set(data)))
#Total number of characters used in the data
totalChars = len(data)
#Number of unique chars
numberOfUniqueChars = len(chars)

#This allows for characters to be represented by numbers
CharsForids = {char:Id for Id, char in enumerate(chars)}

#This is the opposite to the above
idsForChars = {Id:char for Id, char in enumerate(chars)}

#How many timesteps e.g how many characters we want to process in one go
numberOfCharsToLearn = 100

#Since our timestep sequence represetns a process for every 100 chars we omit
#the first 100 chars so the loop runs a 100 less or there will be index out of
#range
counter = totalChars - numberOfCharsToLearn

#Inpput data
charX = []
#output data
y = []
#This loops through all the characters in the data skipping the first 100
for i in range(0, counter, 1):
    #This one goes from 0-100 so it gets 100 values starting from 0 and stops
    #just before the 100th value
    theInputChars = data[i:i+numberOfCharsToLearn]
    #With no : you start with 0, and so you get the actual 100th value
    #Essentially, the output Chars is the next char in line for those 100 chars
    #in X
    theOutputChars = data[i + numberOfCharsToLearn]
    #Appends every 100 chars ids as a list into X
    charX.append([CharsForids[char] for char in theInputChars])
    #For every 100 values there is one y value which is the output
    y.append(CharsForids[theOutputChars])

#Len charX represents how many of those time steps we have
#Our features are set to 1 because in the output we are only predicting 1 char
#Finally numberOfCharsToLearn is how many character we process
X = np.reshape(charX, (len(charX), numberOfCharsToLearn, 1))

#This is done for normalization
X = X/float(numberOfUniqueChars)

#This sets it up for us so we can have a categorical(#feature) output format
y = np_utils.to_categorical(y)
print(y)


model = Sequential()
#Since we know the shape of our Data we can input the timestep and feature data
#The number of timestep sequence are dealt with in the fit function
model.add(LSTM(256, input_shape=(X.shape[1], X.shape[2])))
model.add(Dropout(0.2))
#number of features on the output
model.add(Dense(y.shape[1], activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam')
model.fit(X, y, epochs=5, batch_size=128)
model.save_weights("Othello.hdf5")
#model.load_weights("Othello.hdf5")

randomVal = np.random.randint(0, len(charX)-1)
randomStart = charX[randomVal]
for i in range(500):
    x = np.reshape(randomStart, (1, len(randomStart), 1))
    x = x/float(numberOfUniqueChars)
    pred = model.predict(x)
    index = np.argmax(pred)
    randomStart.append(index)
    randomStart = randomStart[1: len(randomStart)]
print("".join([idsForChars[value] for value in randomStart]))
