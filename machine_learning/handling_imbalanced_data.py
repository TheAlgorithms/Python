# This will show how to handle imbalanced dataset.

from sklearn.datasets import make_classification
from collections import Counter
from imblearn.under_sampling import NearMiss 
from imblearn.combine import SMOTETomek


def main_func():
    
    # Creating the dataset
    X, y = make_classification(n_classes = 2, class_sep = 2, weights = [0.1, 0.9], n_informative = 3, n_redundant = 1, flip_y = 0, n_features = 20, n_clusters_per_class = 1, n_samples = 1000, random_state = 10)

    print('Original dataset shape %s' % Counter(y))
    """
    It is clear from the data that it contains more datapoints class 1 
    as compared to class 0
    """

    # Perform Undersampling and oversampling on the data

    # Undersampling
    nm = NearMiss()
    X_res,y_res = nm.fit_sample(X,y)

    print(f"Original data shape : {Counter(y)}")
    print(f"Resampled data shape : {Counter(y_res)} ")

    # Oversampling
    smk = SMOTETomek(random_state = 42)
    X_res,y_res = smk.fit_sample(X,y)

    print(f"Original data shape : {Counter(y)}")
    print(f"Resampled data shape : {Counter(y_res)} ")
    
if __name__ == "__main__":
    main_func()
