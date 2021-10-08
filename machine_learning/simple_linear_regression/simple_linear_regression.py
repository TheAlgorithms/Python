#Importing
import pandas as pd 
#Reading our data set
dataset= pd.read_csv("weather.csv")
#shaping the data
dataset.shape
print(dataset.columns)
#Importing for visualization
import matplotlib.pyplot as plt
dataset.plot(x="MaxTemp",y="MinTemp",style="*")
plt.title("Mintemp vs Maxtemp")
plt.show()
plt.xlabel("Maxtemp")
plt.ylabel("Mintemp")
plt.close()
#defining our MinTemp and MaxTemp
x=dataset["MinTemp"].values.reshape(-1,1)
y=dataset["MaxTemp"].values.reshape(-1,1)

from sklearn.model_selection import train_test_split
#x is input 
#y is output
#Here we are training our data set
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(x_train,y_train)#supervised with input(xtrain) and output(ytrain)
#printing our modules
print('a= ',regressor.intercept_)
print('b= ',regressor.coef_)

