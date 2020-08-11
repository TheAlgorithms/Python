"""Implementation of GradientBoostingRegressor in sklearn using the 
   boston dataset which is very popular for regression problem to 
   predict house price.
"""
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_boston
from sklearn.metrics import mean_squared_error,r2_score
from sklearn.ensemble import GradientBoostingRegressor, RandomForestRegressor
from sklearn.model_selection import train_test_split

def main():
    # loading the dataset from the sklearn package
    df = load_boston()
    print(df.keys())
    # now let construct a data frame with data and target variables
    df_boston = pd.DataFrame(df.data,columns =df.feature_names)
    # let add the target to the dataframe
    df_boston['Price']= df.target
    # let us print the first five rows using the head function
    print(df_boston.head())
    print(df_boston.describe().T) # to see summary statistics of the dataset
    # Feature selection means for independent and dependent variables
    X = df_boston.iloc[:,:-1]
    y = df_boston.iloc[:,-1] # target variable
    # we are going to split the data with 75% train and 25% test sets.
    X_train,X_test,y_train,y_test = train_test_split(X,y,random_state = 0, test_size = .25)
    # now let set the parameters of the model
    params = {'n_estimators': 500, 'max_depth': 5, 'min_samples_split': 4,
          'learning_rate': 0.01, 'loss': 'ls'}
    model = GradientBoostingRegressor(**params)
    # training the model
    model.fit(X_train,y_train)
    """ let have a look on the train and test score to see how good the model fit the data"""
    score = model.score(X_train,y_train).round(3)
    print("Training score of GradientBoosting is :",score)
    print("the test score of GradienBoosting is :",model.score(X_test,y_test).round(3))
    # Let us evaluation the model by finding the errors 
    y_pred = model.predict(X_test)

    # The mean squared error
    print("Mean squared error: %.2f"% mean_squared_error(y_test, y_pred))
    # Explained variance score: 1 is perfect prediction
    print('Test Variance score: %.2f' % r2_score(y_test, y_pred))
    
    # So let's run the model against the test data
    fig, ax = plt.subplots()
    ax.scatter(y_test, y_pred, edgecolors=(0, 0, 0))
    ax.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--', lw=4)
    ax.set_xlabel('Actual')
    ax.set_ylabel('Predicted')
    ax.set_title("Truth vs Predicted")
    # this show function will display the plotting 
    plt.show()
    

if __name__ =='__main__':
    main()


# In[ ]:




