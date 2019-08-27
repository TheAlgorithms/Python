from sklearn.datasets import load_iris
from sklearn import svm
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


def NuSVC(train_x, train_y, test_x):
    svc_NuSVC = svm.NuSVC()
    svc_NuSVC.fit(train_x, train_y)
    predicted_NuSVC = svc_NuSVC.predict(test_x)
    score_NuSVC = accuracy_score(test_y, predicted_NuSVC)
    # outputs the accuracy
    print("NuSVC score:{}%", score_NuSVC * 100)


def Linearsvc(train_x, train_y, test_x):
    svc_linear = svm.LinearSVC()
    svc_linear.fit(train_x, train_y)
    predicted_svc_linear = svc_linear.predict(test_x)
    score_svc_linear = accuracy_score(test_y, predicted_svc_linear)
    # outputs the accuracy
    print("Linearsvc score:{}%", score_svc_linear * 100)


def SVC(train_x, train_y, test_x):
    # svm.SVC(C=1.0, kernel='rbf', degree=3, gamma=0.0, coef0=0.0, shrinking=True, probability=False,tol=0.001, cache_size=200, class_weight=None, verbose=False, max_iter=-1, random_state=None)
    # various parameters like "kernal","gamma","C" can effectively tuned for a given machine learning model.
    SVC = svm.SVC()
    SVC.fit(train_x, train_y)
    predicted_SVC = SVC.predict(test_x)
    score_SVC = accuracy_score(test_y, predicted_SVC)
    # outputs the accuracy
    print("SVC score:{}%", score_SVC * 100)


# loading the iris dataset
iris = load_iris()
# splitting the dataset to test and train
train_x, test_x, train_y, test_y = train_test_split(
    iris["data"], iris["target"], random_state=4
)
print("Target names: \n {} ".format(iris.target_names))
print("\n Features: \n {}".format(iris.feature_names))

NuSVC(train_x, train_y, test_x)
Linearsvc(train_x, train_y, test_x)
SVC(train_x, train_y, test_x)
