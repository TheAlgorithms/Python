'''
Breast cancer detection given some features.
'''

#import required modules
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans
from sklearn.metrics import confusion_matrix

# Load breast_cancer  file
breast_cancer = load_breast_cancer()
breast_cancer.keys()

#Split Train and Test set
X_train, X_test, y_train, y_test = train_test_split(
    breast_cancer["data"], breast_cancer["target"], test_size=0.15, random_state=4
)

#kmeans
#n_clusters=2 because we have to predict 1 or 0(has breast cancer or not) so two clusters
kmeans = KMeans(n_clusters=2, random_state=0).fit(X_train)

#predict on test data
prediction = kmeans.predict(X_test)

print('The predicted values are: ', prediction)

#Confusion Matrix
print('Confusion Matrix: ',confusion_matrix(y_test, prediction))


