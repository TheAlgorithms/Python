""" We are going to predict the adj close price of microsoft stock price."""
#Install the dependencies pip install quandl 
import quandl
import numpy as np 
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import r2_score, mean_squared_error
import matplotlib.pyplot as plt
# Get the stock data
df = quandl.get("WIKI/MSFT")
# Take a look at the data
print(df.head())
import plotly.express as px 
fig = px.scatter(df, x="High", y="Low")
fig.show()
# Get the Adjusted Close Price 
df = df[['Adj. Close']] 
# Take a look at the new data 
print(df.head())
# A variable for predicting 'n' days out into the future
forecast_out = 30 #'n=30' days
#Create another column (the target ) shifted 'n' units up
df['Prediction'] = df[['Adj. Close']].shift(-forecast_out)
#print the new data set
print(df.tail())
# Convert the dataframe to a numpy array
X = np.array(df.drop(['Prediction'],1))
#Remove the last '30' rows
X = X[:-forecast_out]
print(X)
### Create the dependent data set (y)  #####
# Convert the dataframe to a numpy array 
y = np.array(df['Prediction'])
# Get all of the y values except the last '30' rows
y = y[:-forecast_out]
print(y)
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
#these are the parametes that we are given to the gradient boosting regressor
params = { 
    'loss':'ls',
    'learning_rate':0.1,
    'n_estimators':500,
    'min_samples_split':2,
    'min_weight_fraction_leaf':0.0,
    'max_depth':3,

}
model = GradientBoostingRegressor(**params)
model.fit(x_train,y_train)
model.score(x_train,y_train).round(3)
model.score(x_test,y_test).round(3)
y_pred = model.predict(x_test)
print('The mean squared error is: ', mean_squared_error(y_test,y_pred))
print('The variance is: ', r2_score(y_test,y_pred))

# So let's run the model against the test data
from sklearn.model_selection import cross_val_predict

fig, ax = plt.subplots()
ax.scatter(y_test, y_pred, edgecolors=(0, 0, 0))
ax.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--', lw=4)
ax.set_xlabel('Actual')
ax.set_ylabel('Predicted')
ax.set_title("Ground Truth vs Predicted")
plt.show()
# deviance is a goodness-of-fit statistic for a statistical model; it is often used for statistical hypothesis testing.
#It is a generalization of the idea of using the sum of squares 
#of residuals in ordinary least squares to cases where model-fitting is achieved by maximum likelihood. 
test_score = np.zeros((params['n_estimators'],), dtype=np.float64)
for i, y_pred in enumerate(model.staged_predict(x_test)):
    test_score[i] = model.loss_(y_test, y_pred)

fig = plt.figure(figsize=(10, 6))
plt.subplot(1, 1, 1)
plt.title('Deviance')
plt.plot(np.arange(params['n_estimators']) + 1, model.train_score_, 'b-',
         label='Training Set Deviance')
plt.plot(np.arange(params['n_estimators']) + 1, test_score, 'r-',
         label='Test Set Deviance')
plt.legend(loc='upper right')
plt.xlabel('Boosting Iterations')
plt.ylabel('Deviance')
fig.tight_layout()
plt.show()





