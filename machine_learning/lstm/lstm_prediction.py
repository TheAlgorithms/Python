import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import LSTM,Dense

def clean_data(data_file):
	'''
	This function will read and clean data
	input: CSV file containing data
	output: Data which will be useful for training
	'''
	df = pd.read_csv(data_file, header=None)
	print(df.head())
	len_data = df.shape[:1][0]
	actual_data = df.iloc[:,1:2]
	actual_data = actual_data.values.reshape(len_data,1)
	scl = MinMaxScaler()
	actual_data = scl.fit_transform(actual_data)
	look_back = 10
	forward_days = 5
	periods = 20
	division = len_data - periods*look_back
	train_data = actual_data[:division]
	test_data = actual_data[division-look_back:]
	print(train_data,test_data)
	train_x,train_y=[],[]
	test_x,test_y=[],[]
	for i in range(0,len(train_data) - forward_days - look_back + 1,1):
		train_x.append(train_data[i:i + look_back])
		train_y.append(train_data[i + look_back:i + look_back + forward_days])

	for i in range(0,len(test_data) - forward_days - look_back + 1,1):
		test_x.append(test_data[i:i + look_back])
		test_y.append(test_data[i + look_back:i + look_back + forward_days])
	x_train = np.array(train_x)
	x_test = np.array(test_x)
	y_train = np.array([list(i.ravel()) for i in train_y])
	y_test = np.array([list(i.ravel()) for i in test_y])
	print(x_train.shape)
	print(x_test.shape)
	print(y_train.shape)
	print(y_test.shape)
	return x_train,y_train,x_test,y_test



if __name__ == '__main__':
	x_train,y_train,x_test,y_test = clean_data('google_data.csv')

	'''
	Create our lstm model
	'''
	look_back = 10
	forward_days = 5
	periods = 20

	model = Sequential()
	model.add(LSTM(128,input_shape=(look_back,1),return_sequences=True))
	model.add(LSTM(64,input_shape=(128,1)))
	model.add(Dense(forward_days))
	model.compile(loss='mean_squared_error', optimizer='adam')
	history = model.fit(
		x_train,y_train,epochs=150,verbose=1,shuffle=True,batch_size=4)
	pred = model.predict(x_test)
	print(pred[:2],y_test[:2])