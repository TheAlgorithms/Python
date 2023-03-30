import pandas as pd
from sklearn.model_selection import train_test_split

# Read data from csv file
df = pd.read_csv('placement.csv')

#diffrentiate x and y
x = df.iloc[:,0].values
y = df.iloc[:,1].values

# split the value using train test split

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2)

#Since 'slope' and 'bias' can be calculated from gradient descent
#  formula instead i tried a diffrent approach
#which uses Ordinary Least Squares (OLS) Formula which is for :
#weight(m) = sumation of all (x-x(mean))*(y-y(mean))/(x-x(mean))^2
#since y = mx + b
#so b = y(mean) - weight(m).x(mean)

class LinearRegression:
    def __init__(self) -> None:
        self.m = 0
        self.b = 0
    def fit(self,x_train,y_train):
        num = 0
        den = 0
        for i in range(x_train.shape[0]):
            num = num + (x_train[i]-x_train.mean())*(y_train[i]-y_train.mean())
            den = den + (x_train[i]-x_train.mean())*(x_train[i]-x_train.mean())
        self.m = num/den
        self.b = y_train.mean() - self.m * x_train.mean()
    def predict(self,x_test):
        result = self.m*x_test + self.b
        return result
lr = LinearRegression()
lr.fit(x_train,y_train)
print(lr.predict(x_test))
