from sklearn import svm
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split


# different functions implementing different types of SVM's
def NuSVC(train_x, train_y):
    svc_NuSVC = svm.NuSVC()
    svc_NuSVC.fit(train_x, train_y)
    return svc_NuSVC


def Linearsvc(train_x, train_y):
    svc_linear = svm.LinearSVC(tol=10e-2)
    svc_linear.fit(train_x, train_y)
    return svc_linear


def SVC(train_x, train_y):
    # svm.SVC(C=1.0, kernel='rbf', degree=3, gamma=0.0, coef0=0.0, shrinking=True,
    # probability=False,tol=0.001, cache_size=200, class_weight=None, verbose=False,
    # max_iter=1000, random_state=None)
    # various parameters like "kernel","gamma","C" can effectively tuned for a given
    # machine learning model.
    SVC = svm.SVC(gamma="auto")
    SVC.fit(train_x, train_y)
    return SVC


def test(X_new):
    """
    3 test cases to be passed
    an array containing the sepal length (cm), sepal width (cm), petal length (cm),
    petal width (cm) based on which  the target name will be predicted
    >>> test([1,2,1,4])
    'virginica'
    >>> test([5, 2, 4, 1])
    'versicolor'
    >>> test([6,3,4,1])
    'versicolor'
    """
    iris = load_iris()
    # splitting the dataset to test and train
    train_x, test_x, train_y, test_y = train_test_split(
        iris["data"], iris["target"], random_state=4
    )
    # any of the 3 types of SVM can be used
    # current_model=SVC(train_x, train_y)
    # current_model=NuSVC(train_x, train_y)
    current_model = Linearsvc(train_x, train_y)
    prediction = current_model.predict([X_new])
    return iris["target_names"][prediction][0]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
