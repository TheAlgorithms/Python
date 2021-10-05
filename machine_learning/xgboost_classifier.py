# illustrating working of XGBoost Classifier using Iris dataset

# importing necessary libraries
import pandas as pd 
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

# a function which trains a XGBClassifier model
def train_xgbclassifier(x_train, y_train):
    xgb_classifier = XGBClassifier(n_estimators = 100, random_state = 40)
    xgb_classifier.fit(x_train, y_train)
    return xgb_classifier

# main function to illustrate working of XGBClassifier
def main() -> none:
    # loading the dataset
    url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
    names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
    iris_dataset = pd.read_csv(url, names = names)
    
    X = iris_dataset.iloc[:, 0:4]       # features           
    Y = iris_dataset.iloc[:, 4]         # predictors

    # splitting X and Y into train and test sets
    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size = 0.2, random_state = 40)

    # building a XGBClassifier model
    model =  train_xgblassifier(x_train, y_train)

    # making predictions on test set
    y_pred = model.predict(x_test)

    # using some common evaluation metrics to evaluate the model performance
    # accuracy score
    print("\nAccuracy = ", accuracy_score(y_test, y_pred)*100, " %")
    # classification report
    print("\nClassification report:\n")
    print(classification_report(y_test, y_pred))
    # confusion matrix
    print("\nConfusion Matrix:\n")
    print(confusion_matrix(y_test, y_pred))
    import doctest
    doctest.testmod(name = 'main', verbose = True)

if __name__ == '__main__':
    main()
