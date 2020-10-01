# XGboost Classifier Example
from matplotlib import pyplot as plt
from sklearn.datasets import load_iris
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier

def main():

    """
    XGBoost Classifier from https://xgboost.readthedocs.io/en/latest/
    Iris type dataset is used to demonstrate algorithm.
    """

    # Load Iris dataset
    iris = load_iris()

    # Split dataset into train and test data
    X = iris["data"]  # features
    Y = iris["target"]
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=42)
    
    model = XGBClassifier(silent=True,
                      booster = 'gbtree',
                      n_estimators=50, 
                      max_depth=10,
                      verbosity=0
                     )
    
    eval_set = [(X_test, y_test)]
    eval_metric = ["mlogloss"]
    
    model.fit(X_train, y_train,
              early_stopping_rounds=5, 
              eval_metric=eval_metric, 
              eval_set=eval_set)
    
    y_pred = model.predict(X_test)
    
    print(classification_report(y_test, y_pred))


if __name__ == "__main__":
    main()
