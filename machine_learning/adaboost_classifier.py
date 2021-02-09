from sklearn.ensemble import AdaBoostClassifier
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.metrics import plot_confusion_matrix
from matplotlib import pyplot as plt


"""Adaboost classifier example using the breast_cancer dataset from sklearn"""


def adaboost():
    cancer_df = load_breast_cancer()
    print(cancer_df.keys())
    X, y = cancer_df.data, cancer_df.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

    abc = AdaBoostClassifier(base_estimator=None,
                             n_estimators=300, learning_rate=1, random_state=0)
    abc.fit(X_train, y_train)
    y_pred = abc.predict(X_test)
    # Display Confusion Matrix of Classifier
    plot_confusion_matrix(
        abc,
        X_test,
        y_test,
        display_labels=cancer_df["target_names"],
        cmap="Blues",
        normalize="true",
    )
    plt.title("Normalized Confusion Matrix - Cancer Dataset")
    plt.show()

    # to see the accuracy of the model
    print("Accuracy of adaboost is:", abc.score(X_test, y_test))


if __name__ == "__main__":
    adaboost()
