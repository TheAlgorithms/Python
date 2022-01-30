import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics


def engineer_features():
    """
    Loads the data set and engineers features of it
    """
    # https://scikit-learn.org/stable/datasets/toy_dataset.html#iris-plants-dataset
    iris = load_iris()

    # pick features to use to predict
    all_x = iris['data']
    all_y = iris['target']

    versicolor_label = 1
    virginica_label = 2

    # engineer these features to be in the right format
    sel_idx_1 = np.where(all_y == versicolor_label)[0]
    sel_idx_2 = np.where(all_y == virginica_label)[0]

    sel_idx = np.r_[sel_idx_1, sel_idx_2]

    sel_x = all_x[sel_idx, :]
    sel_y = all_y[sel_idx]

    feature1_idx = 2
    feature2_idx = 3

    proc_x = sel_x[:, [feature1_idx, feature2_idx]]
    proc_y = sel_y

    # split the data into training and testing data
    train_x, test_x, train_y, test_y = train_test_split(
        proc_x, proc_y, train_size=0.8, test_size=0.2)

    return train_x, test_x, train_y, test_y


def train_SVM(train_x, test_x, train_y, test_y):
    """
    Trains the model using Linear Regression
    """
    # https://en.wikipedia.org/wiki/Support-vector_machine
    # train the model using SVC
    model = SVC(kernel='linear')
    model.fit(train_x, train_y)

    # use test set to make predicitons
    pred_y_test_svm = model.predict(test_x)

    # check test predictions
    acc_score = metrics.accuracy_score(test_y, pred_y_test_svm)
    print('SVM Model accuracy: {:.2f}%'.format(acc_score * 100))

    # use training data to predict
    pred_y_train_svm = model.predict(train_x)

    # check training predicitons
    acc_score = metrics.accuracy_score(train_y, pred_y_train_svm)
    print('SVM Training accuracy: {:.2f}%'.format(acc_score * 100))


def train_KNN(train_x, test_x, train_y, test_y):
    """
    Trains the model using K Nearest Neighbors
    """
    # https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm
    knn = KNeighborsClassifier(n_neighbors=1)
    knn.fit(train_x, train_y)

    # use test set to make predicitons
    pred_y_test_knn = knn.predict(test_x)

    # check test predictions
    acc_score = metrics.accuracy_score(test_y, pred_y_test_knn)
    print('KNN Model accuracy: {:.2f}%'.format(acc_score * 100))

    # use training data to predict
    pred_y_train_knn = knn.predict(train_x)

    # check training predicitons
    acc_score = metrics.accuracy_score(train_y, pred_y_train_knn)
    print('KNN Training accuracy: {:.2f}%'.format(acc_score * 100))


if __name__ == "__main__":
    train_x, test_x, train_y, test_y = engineer_features()
    train_SVM(train_x, test_x, train_y, test_y)
    train_KNN(train_x, test_x, train_y, test_y)
