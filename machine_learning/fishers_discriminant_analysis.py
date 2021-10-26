"""
Binary Fishers Linear Discriminant.
https://en.wikipedia.org/wiki/Linear_discriminant_analysis#Fisher's_linear_discriminant

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

import numpy as np  # type: ignore
from numpy.linalg import inv  # type: ignore


def get_xt() -> tuple:
    """
    Placeholder code to generate the training data, X, Y.
    (Y is also referred to as T in the code / docs).

    >>> get_xt()
    (array([[  0,   0],
           [  1,   0],
           [  2,   0],
           [  0,   1],
           [  1,   1],
           [  2,   1],
           [  3,   1],
           [  4,   1],
           [  5,   1],
           [100,   1],
           [  0,   2],
           [  1,   2],
           [  2,   2],
           [  3,   2],
           [  4,   2],
           [  5,   2],
           [100,   2],
           [  3,   3],
           [  4,   3],
           [  5,   3],
           [100,   3]]), array([[1., 0.],
           [1., 0.],
           [1., 0.],
           [1., 0.],
           [1., 0.],
           [1., 0.],
           [1., 0.],
           [1., 0.],
           [1., 0.],
           [1., 0.],
           [1., 0.],
           [1., 0.],
           [1., 0.],
           [1., 0.],
           [1., 0.],
           [1., 0.],
           [1., 0.],
           [0., 1.],
           [0., 1.],
           [0., 1.],
           [0., 1.]]))
    """
    x_input = [
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

    x_input = np.array(x_input)

    t_input = np.zeros((21, 2))
    labels = (x_input[:, 1] > 2) + 0  # type: ignore[call-overload]
    for t in range(t_input.shape[0]):
        t_input[t, labels[t]] = 1

    result = (x_input, t_input)
    print(type(result))
    return result


def get_x_by_t(x_input: np.ndarray, t_input: np.ndarray) -> tuple:
    """
    >>> get_x_by_t([[1,1],[2,2]], [[1,0],[0,1]])
    (array([[1, 1]]), array([[2, 2]]))
    """

    # We could use better numpy operations, but for
    # learning purposes the code needn't be over-complex.
    # We have two classes.

    x_1 = []
    x_2 = []

    for ix, t in enumerate(t_input):
        if t[0] == 1:
            x_1.append(x_input[ix])
        else:
            x_2.append(x_input[ix])

    x_1 = np.array(x_1)
    x_2 = np.array(x_2)

    return (x_1, x_2)


def main() -> None:
    """
    >>> main()
    <BLANKLINE>
    <BLANKLINE>
    Step 1: Get X, T training data.
    <BLANKLINE>
    <BLANKLINE>
    Step 2: Get X by classes in T, i.e. all X points of
            class 1 as x_1, all points of class 2 as x_2.
    <BLANKLINE>
    <BLANKLINE>
    Step 3: Get means of X by class. i.e. m1_mat
            and m2_mat as means of data x_1 and x_2 respectively.
    Mean 1 : [[13.70588235  1.23529412]]
    Mean 2 : [[28.  3.]]
    <BLANKLINE>
    <BLANKLINE>
    Step 4: Calculate Between Class s_b
    [[204.32179931  25.22491349]
     [ 25.22491349   3.11418685]]
    <BLANKLINE>
    <BLANKLINE>
    Step 5: Calculate Within Class Sw
    [[2.38355294e+04 5.71764706e+01]
     [5.71764706e+01 9.05882353e+00]]
    <BLANKLINE>
    <BLANKLINE>
    Step 6: Calculate dimension w
    [[-1.34436264e-04]
     [-1.93956675e-01]]
    <BLANKLINE>
    <BLANKLINE>
    Step 7: Calculate Fisher's Criterion J(w)
    [[0.34419813]]
    <BLANKLINE>
    <BLANKLINE>
    Step 8: Perform Prediction on last data point in the training set.
    Point      : [[0 0]]
    True Label : 1
    Prediction Label : [1]
    """
    print("\n\nStep 1: Get X, T training data.")
    x_input, t_input = get_xt()

    print(
        """\n\nStep 2: Get X by classes in T, i.e. all X points of
        class 1 as x_1, all points of class 2 as x_2."""
    )
    x_1, x_2 = get_x_by_t(x_input, t_input)

    print(
        """\n\nStep 3: Get means of X by class. i.e. m1_mat
        and m2_mat as means of data x_1 and x_2 respectively."""
    )

    m1_mat = np.mean(x_1, axis=0).reshape(2, 1)
    m2_mat = np.mean(x_2, axis=0).reshape(2, 1)
    print("Mean 1 :", np.transpose(m1_mat))
    print("Mean 2 :", np.transpose(m2_mat))

    print("\n\nStep 4: Calculate Between Class s_b")
    s_b = np.matmul((m1_mat - m2_mat), np.transpose(m1_mat - m2_mat))
    print(s_b)

    print("\n\nStep 5: Calculate Within Class Sw")

    s1w = np.zeros((2, 2))

    for xn in x_1:
        ff = xn.reshape(2, 1) - m1_mat.reshape(2, 1)
        ans = np.matmul(ff, np.transpose(ff))
        s1w += ans

    s2w = np.zeros((2, 2))

    for xn in x_2:
        ff = xn.reshape(2, 1) - m2_mat.reshape(2, 1)
        ans = np.matmul(ff, np.transpose(ff))
        s2w += ans

    sw = s1w + s2w
    print(sw)

    print("\n\nStep 6: Calculate dimension w")

    w = np.matmul(inv(sw), m1_mat - m2_mat)
    print(w)

    print("\n\nStep 7: Calculate Fisher's Criterion J(w)")
    num = np.matmul(np.matmul(np.transpose(w), s_b), w)
    den = np.matmul(np.matmul(np.transpose(w), sw), w)
    j_w = num / den

    print(j_w)

    print("\n\nStep 8: Perform Prediction on last data point in the training set.")
    point = x_input[0].reshape(2, 1)
    true_label = t_input[0]
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
    import doctest

    # main()

    doctest.testmod(name="main", verbose=True)
