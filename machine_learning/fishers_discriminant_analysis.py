"""
Binary Fishers Linear Discriminant.

Given an input data x of dimension D
Binary labels T

The objective is to perform fisher's discriminant analysis and obtain predictions.

Sub-Objectives are :
1. Process x (to be a matrix), Process t (to be one-hot) {also referred to as y}
2. Get X, T by class. (as in all X for class1, all X for class2 so on.)
3. Obtain matrices Sw, Sb
4. Obtain Fisher's Criterion
5. Perform Prediction on sample data.


Note that the fisher's discriminant,
w is proportional to Sw-1*(m2-m1) and there will exist infinitely many w as solutions.
Hence we will take w = Sw-1*(m2-m1) as the solution.

Sw-1 (read as Sw inverse).



X is a two dimension data point.
There are two classes 1 and 2.

"""

import numpy as np
from numpy.linalg import inv


def get_XT():
    """
    Placeholder code to generate the training data, X, Y.
    (Y is also referred to as T in the code / docs).
    """
    X = [
        [0, 0],
        [1, 0],
        [2, 0],
        [0, 1],
        [1, 1],
        [2, 1],
        [3, 1],
        [4, 1],
        [5, 1],
        [100, 1],
        [0, 2],
        [1, 2],
        [2, 2],
        [3, 2],
        [4, 2],
        [5, 2],
        [100, 2],
        [3, 3],
        [4, 3],
        [5, 3],
        [100, 3],
    ]

    X = np.array(X)

    T = np.zeros((21, 2))
    labels = (X[:, 1] > 2) + 0
    for t in range(T.shape[0]):
        T[t, labels[t]] = 1

    return X, T


def get_X_by_T(X, T):
    X, T = get_XT()

    # We could use better numpy operations, but for
    # learning purposes the code needn't be over-complex.
    # We have two classes.

    X_1 = []
    X_2 = []

    for ix, t in enumerate(T):
        if t[0] == 1:
            X_1.append(X[ix])
        else:
            X_2.append(X[ix])

    X_1 = np.array(X_1)
    X_2 = np.array(X_2)

    return X_1, X_2


def main():
    print("\n\nStep 1: Get X, T training data.")
    X, T = get_XT()

    print(
        """\n\nStep 2: Get X by classes in T, i.e. all X points of
        class 1 as X_1, all points of class 2 as X_2."""
    )
    X_1, X_2 = get_X_by_T(X, T)

    print(
        """\n\nStep 3: Get means of X by class. i.e. m1_mat
        and m2_mat as means of data X_1 and X_2 respectively."""
    )

    m1_mat = np.mean(X_1, axis=0).reshape(2, 1)
    m2_mat = np.mean(X_2, axis=0).reshape(2, 1)
    print("Mean 1 :", np.transpose(m1_mat))
    print("Mean 2 :", np.transpose(m2_mat))

    print("\n\nStep 4: Calculate Between Class s_B")
    s_B = np.matmul((m1_mat - m2_mat), np.transpose(m1_mat - m2_mat))
    print(s_B)

    print("\n\nStep 5: Calculate Within Class Sw")

    s1w = np.zeros((2, 2))

    for xn in X_1:
        ff = xn.reshape(2, 1) - m1_mat.reshape(2, 1)
        ans = np.matmul(ff, np.transpose(ff))
        s1w += ans

    s2w = np.zeros((2, 2))

    for xn in X_2:
        ff = xn.reshape(2, 1) - m2_mat.reshape(2, 1)
        ans = np.matmul(ff, np.transpose(ff))
        s2w += ans

    sw = s1w + s2w
    print(sw)

    print("\n\nStep 6: Calculate dimension w")

    w = np.matmul(inv(sw), m1_mat - m2_mat)
    print(w)

    print("\n\nStep 7: Calculate Fisher's Criterion J(w)")
    num = np.matmul(np.matmul(np.transpose(w), s_B), w)
    den = np.matmul(np.matmul(np.transpose(w), sw), w)
    Jw = num / den

    print(Jw)

    print("\n\nStep 8: Perform Prediction on last data point in the training set.")
    point = X[0].reshape(2, 1)
    true_label = T[0]
    print("Point      :", np.transpose(point))
    print("True Label :", np.argmax(np.transpose(true_label)) + 1)
    # Remember numpy is indexed from 0, but our labels are 1 and 2. (not 0 and 1).

    prediction_y = np.matmul(np.transpose(w), point).reshape(
        1,
    )
    prediction = (prediction_y >= 0) + 0
    # Neat trick to convert bool to int.

    print("Prediction Label :", prediction)


if __name__ == "__main__":
    main()
