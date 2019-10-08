from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier

# Load iris file
iris = load_iris()
iris.keys()
"""
proper format to use KNN
class sklearn.neighbors.KNeighborsClassifier(n_neighbors=5, weights=’uniform’, algorithm=’auto’, leaf_size=30, p=2, metric=’minkowski’, metric_params=None, n_jobs=None, **kwargs)
n_neighbors : int, optional (default = 5)
Number of neighbors to use by default for kneighbors queries.

weights : str or callable, optional (default = ‘uniform’)
weight function used in prediction. Possible values:

‘uniform’ : uniform weights. All points in each neighborhood are weighted equally.
‘distance’ : weight points by the inverse of their distance. in this case, closer neighbors of a query point will have a greater influence than neighbors which are further away.
[callable] : a user-defined function which accepts an array of distances, and returns an array of the same shape containing the weights.
algorithm : {‘auto’, ‘ball_tree’, ‘kd_tree’, ‘brute’}, optional
Algorithm used to compute the nearest neighbors:

‘ball_tree’ will use BallTree
‘kd_tree’ will use KDTree
‘brute’ will use a brute-force search.
‘auto’ will attempt to decide the most appropriate algorithm based on the values passed to fit method.
Note: fitting on sparse input will override the setting of this parameter, using brute force.

leaf_size : int, optional (default = 30)
Leaf size passed to BallTree or KDTree. This can affect the speed of the construction and query, as well as the memory required to store the tree. The optimal value depends on the nature of the problem.

p : integer, optional (default = 2)
Power parameter for the Minkowski metric. When p = 1, this is equivalent to using manhattan_distance (l1), and euclidean_distance (l2) for p = 2. For arbitrary p, minkowski_distance (l_p) is used.

metric : string or callable, default ‘minkowski’
the distance metric to use for the tree. The default metric is minkowski, and with p=2 is equivalent to the standard Euclidean metric. See the documentation of the DistanceMetric class for a list of available metrics.

metric_params : dict, optional (default = None)
Additional keyword arguments for the metric function.

n_jobs : int or None, optional (default=None)
The number of parallel jobs to run for neighbors search. None means 1 unless in a joblib.parallel_backend context. -1 means using all processors. See Glossary for more details. Doesn’t affect fit method.
"""
print("Target names: \n {} ".format(iris.target_names))
print("\n Features: \n {}".format(iris.feature_names))

# Train set e Test set
X_train, X_test, y_train, y_test = train_test_split(
    iris["data"], iris["target"], random_state=4
)

# KNN

knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train, y_train)

# new array to test
X_new = [[1, 2, 1, 4], [2, 3, 4, 5]]

prediction = knn.predict(X_new)

print(
    "\nNew array: \n {}"
    "\n\nTarget Names Prediction: \n {}".format(X_new, iris["target_names"][prediction])
)
