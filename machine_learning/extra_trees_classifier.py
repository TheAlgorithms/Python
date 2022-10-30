import numpy as np
from matplotlib import pyplot as plt
from sklearn.datasets import load_iris
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.model_selection import train_test_split
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.metrics import recall_score, f1_score, precision_score, accuracy_score


def data_split(data) -> tuple:
    return data["data"], data["target"]

def extra_trees(features, target) -> ExtraTreesClassifier:
    classifier = ExtraTreesClassifier()
    classifier.fit(features, target)
    return classifier


def main() -> None:
    # Load Iris dataset
    iris = load_iris()
    features, targets = data_split(iris)
    x_train, x_test, y_train, y_test = train_test_split(features, targets, test_size=0.2)

    names = iris["target_names"]

    # Creating Extra Trees Classifier and fitting train sets
    ExtraTrees_Classifier = extra_trees(x_train, y_train)

    predict = ExtraTrees_Classifier.predict(x_test)

    #Showing Metrics
    print('Accuracy: ', accuracy_score(predict, y_test))
    print('F1-Score: ', f1_score(predict, y_test, average='macro'))
    print('Precision: ', precision_score(predict, y_test, average='macro'))
    print('Recall: ', recall_score(predict, y_test, average='macro'))

    #Display Confusion Matrix
    ConfusionMatrixDisplay.from_estimator(
        ExtraTrees_Classifier,
        x_test,
        y_test,
        display_labels=names,
        cmap="viridis"
    )

    
    plt.title("Confusion Matrix - Extra Trees Classifier - IRIS Dataset")
    plt.show()


    
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()
    