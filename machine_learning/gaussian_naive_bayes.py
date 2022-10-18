# Gaussian Naive Bayes Example
from matplotlib import pyplot as plt
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score, confusion_matrix # The plot_confusion_matrix method will be deprecated in the developed versions of Python 3.10.x according to the warning that it throws when this code is run.
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
import time
import seaborn as sns # For plotting a heatmap of the confusion matrix. This way will not throw any warning.


def main():

    """
    Gaussian Naive Bayes Example using sklearn function.
    Iris type dataset is used to demonstrate algorithm.
    """

    # Load Iris dataset
    iris = load_iris()

    # Split dataset into train and test data
    x = iris["data"]  # features
    y = iris["target"]
    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.3, random_state=1
    )

    # Gaussian Naive Bayes
    nb_model = GaussianNB()
    model_fit = nb_model.fit(x_train, y_train)
    y_pred = model_fit.predict(x_test)
    # Display Confusion Matrix
    Conf_Matrix = confusion_matrix(y_true=y_test, y_pred=y_pred)
    sns.heatmap(data = Conf_Matrix, annot = True, cmap = "Greys_r")
    plt.show()
    
    # Printing the seen confusion matrix on the console
    time.sleep(1.2)
    print("The confusion matrix is:\n", Conf_Matrix)
    
    time.sleep(1.8)
    # Declaring the overall accuracy of the model
    final_accuracy = 100*accuracy_score(y_true = y_test, y_pred = y_pred)
    print(f"The final accuracy of the model is: {round(final_accuracy, 2)}%")
 
if __name__ == "__main__":
    main()
