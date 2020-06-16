"""
    Implementation of sequential minimal optimization (SMO) for support vector machines
    (SVM).

    Sequential minimal optimization (SMO) is an algorithm for solving the quadratic
    programming (QP) problem that arises during the training of support vector
    machines.
    It was invented by John Platt in 1998.

Input:
    0: type: numpy.ndarray.
    1: first column of ndarray must be tags of samples, must be 1 or -1.
    2: rows of ndarray represent samples.

Usage:
    Command:
        python3 sequential_minimum_optimization.py
    Code:
        from sequential_minimum_optimization import SmoSVM, Kernel

        kernel = Kernel(kernel='poly', degree=3., coef0=1., gamma=0.5)
        init_alphas = np.zeros(train.shape[0])
        SVM = SmoSVM(train=train, alpha_list=init_alphas, kernel_func=kernel, cost=0.4,
                     b=0.0, tolerance=0.001)
        SVM.fit()
        predict = SVM.predict(test_samples)

Reference:
    https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/smo-book.pdf
    https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/tr-98-14.pdf
    http://web.cs.iastate.edu/~honavar/smo-svm.pdf
"""


import os
import sys
import urllib.request

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.datasets import make_blobs, make_circles
from sklearn.preprocessing import StandardScaler

CANCER_DATASET_URL = (
    "http://archive.ics.uci.edu/ml/machine-learning-databases/"
    "breast-cancer-wisconsin/wdbc.data"
)


class SmoSVM:
    def __init__(
        self,
        train,
        kernel_func,
        alpha_list=None,
        cost=0.4,
        b=0.0,
        tolerance=0.001,
        auto_norm=True,
    ):
        self._init = True
        self._auto_norm = auto_norm
        self._c = np.float64(cost)
        self._b = np.float64(b)
        self._tol = np.float64(tolerance) if tolerance > 0.0001 else np.float64(0.001)

        self.tags = train[:, 0]
        self.samples = self._norm(train[:, 1:]) if self._auto_norm else train[:, 1:]
        self.alphas = alpha_list if alpha_list is not None else np.zeros(train.shape[0])
        self.Kernel = kernel_func

        self._eps = 0.001
        self._all_samples = list(range(self.length))
        self._K_matrix = self._calculate_k_matrix()
        self._error = np.zeros(self.length)
        self._unbound = []

        self.choose_alpha = self._choose_alphas()

    # Calculate alphas using SMO algorithm
    def fit(self):
        K = self._k
        state = None
        while True:

            # 1: Find alpha1, alpha2
            try:
                i1, i2 = self.choose_alpha.send(state)
                state = None
            except StopIteration:
                print("Optimization done!\nEvery sample satisfy the KKT condition!")
                break

            # 2: calculate new alpha2 and new alpha1
            y1, y2 = self.tags[i1], self.tags[i2]
            a1, a2 = self.alphas[i1].copy(), self.alphas[i2].copy()
            e1, e2 = self._e(i1), self._e(i2)
            args = (i1, i2, a1, a2, e1, e2, y1, y2)
            a1_new, a2_new = self._get_new_alpha(*args)
            if not a1_new and not a2_new:
                state = False
                continue
            self.alphas[i1], self.alphas[i2] = a1_new, a2_new

            # 3: update threshold(b)
            b1_new = np.float64(
                -e1
                - y1 * K(i1, i1) * (a1_new - a1)
                - y2 * K(i2, i1) * (a2_new - a2)
                + self._b
            )
            b2_new = np.float64(
                -e2
                - y2 * K(i2, i2) * (a2_new - a2)
                - y1 * K(i1, i2) * (a1_new - a1)
                + self._b
            )
            if 0.0 < a1_new < self._c:
                b = b1_new
            if 0.0 < a2_new < self._c:
                b = b2_new
            if not (np.float64(0) < a2_new < self._c) and not (
                np.float64(0) < a1_new < self._c
            ):
                b = (b1_new + b2_new) / 2.0
            b_old = self._b
            self._b = b

            # 4:  update error value,here we only calculate those non-bound samples'
            #     error
            self._unbound = [i for i in self._all_samples if self._is_unbound(i)]
            for s in self.unbound:
                if s == i1 or s == i2:
                    continue
                self._error[s] += (
                    y1 * (a1_new - a1) * K(i1, s)
                    + y2 * (a2_new - a2) * K(i2, s)
                    + (self._b - b_old)
                )

            # if i1 or i2 is non-bound,update there error value to zero
            if self._is_unbound(i1):
                self._error[i1] = 0
            if self._is_unbound(i2):
                self._error[i2] = 0

    # Predict test samles
    def predict(self, test_samples, classify=True):

        if test_samples.shape[1] > self.samples.shape[1]:
            raise ValueError(
                "Test samples' feature length does not equal to that of train samples"
            )

        if self._auto_norm:
            test_samples = self._norm(test_samples)

        results = []
        for test_sample in test_samples:
            result = self._predict(test_sample)
            if classify:
                results.append(1 if result > 0 else -1)
            else:
                results.append(result)
        return np.array(results)

    # Check if alpha violate KKT condition
    def _check_obey_kkt(self, index):
        alphas = self.alphas
        tol = self._tol
        r = self._e(index) * self.tags[index]
        c = self._c

        return (r < -tol and alphas[index] < c) or (r > tol and alphas[index] > 0.0)

    # Get value calculated from kernel function
    def _k(self, i1, i2):
        # for test samples,use Kernel function
        if isinstance(i2, np.ndarray):
            return self.Kernel(self.samples[i1], i2)
        # for train samples,Kernel values have been saved in matrix
        else:
            return self._K_matrix[i1, i2]

    # Get sample's error
    def _e(self, index):
        """
        Two cases:
            1:Sample[index] is non-bound,Fetch error from list: _error
            2:sample[index] is bound,Use predicted value deduct true value: g(xi) - yi

        """
        # get from error data
        if self._is_unbound(index):
            return self._error[index]
        # get by g(xi) - yi
        else:
            gx = np.dot(self.alphas * self.tags, self._K_matrix[:, index]) + self._b
            yi = self.tags[index]
            return gx - yi

    # Calculate Kernel matrix of all possible i1,i2 ,saving time
    def _calculate_k_matrix(self):
        k_matrix = np.zeros([self.length, self.length])
        for i in self._all_samples:
            for j in self._all_samples:
                k_matrix[i, j] = np.float64(
                    self.Kernel(self.samples[i, :], self.samples[j, :])
                )
        return k_matrix

    # Predict test sample's tag
    def _predict(self, sample):
        k = self._k
        predicted_value = (
            np.sum(
                [
                    self.alphas[i1] * self.tags[i1] * k(i1, sample)
                    for i1 in self._all_samples
                ]
            )
            + self._b
        )
        return predicted_value

    # Choose alpha1 and alpha2
    def _choose_alphas(self):
        locis = yield from self._choose_a1()
        if not locis:
            return
        return locis

    def _choose_a1(self):
        """
        Choose first alpha ;steps:
           1:First loop over all sample
           2:Second loop over all non-bound samples till all non-bound samples does not
               voilate kkt condition.
           3:Repeat this two process endlessly,till all samples does not voilate kkt
               condition samples after first loop.
        """
        while True:
            all_not_obey = True
            # all sample
            print("scanning all sample!")
            for i1 in [i for i in self._all_samples if self._check_obey_kkt(i)]:
                all_not_obey = False
                yield from self._choose_a2(i1)

            # non-bound sample
            print("scanning non-bound sample!")
            while True:
                not_obey = True
                for i1 in [
                    i
                    for i in self._all_samples
                    if self._check_obey_kkt(i) and self._is_unbound(i)
                ]:
                    not_obey = False
                    yield from self._choose_a2(i1)
                if not_obey:
                    print("all non-bound samples fit the KKT condition!")
                    break
            if all_not_obey:
                print("all samples fit the KKT condition! Optimization done!")
                break
        return False

    def _choose_a2(self, i1):
        """
        Choose the second alpha by using heuristic algorithm ;steps:
           1: Choose alpha2 which gets the maximum step size (|E1 - E2|).
           2: Start in a random point,loop over all non-bound samples till alpha1 and
               alpha2 are optimized.
           3: Start in a random point,loop over all samples till alpha1 and alpha2 are
               optimized.
        """
        self._unbound = [i for i in self._all_samples if self._is_unbound(i)]

        if len(self.unbound) > 0:
            tmp_error = self._error.copy().tolist()
            tmp_error_dict = {
                index: value
                for index, value in enumerate(tmp_error)
                if self._is_unbound(index)
            }
            if self._e(i1) >= 0:
                i2 = min(tmp_error_dict, key=lambda index: tmp_error_dict[index])
            else:
                i2 = max(tmp_error_dict, key=lambda index: tmp_error_dict[index])
            cmd = yield i1, i2
            if cmd is None:
                return

        for i2 in np.roll(self.unbound, np.random.choice(self.length)):
            cmd = yield i1, i2
            if cmd is None:
                return

        for i2 in np.roll(self._all_samples, np.random.choice(self.length)):
            cmd = yield i1, i2
            if cmd is None:
                return

    # Get the new alpha2 and new alpha1
    def _get_new_alpha(self, i1, i2, a1, a2, e1, e2, y1, y2):
        K = self._k
        if i1 == i2:
            return None, None

        # calculate L and H  which bound the new alpha2
        s = y1 * y2
        if s == -1:
            L, H = max(0.0, a2 - a1), min(self._c, self._c + a2 - a1)
        else:
            L, H = max(0.0, a2 + a1 - self._c), min(self._c, a2 + a1)
        if L == H:
            return None, None

        # calculate eta
        k11 = K(i1, i1)
        k22 = K(i2, i2)
        k12 = K(i1, i2)
        eta = k11 + k22 - 2.0 * k12

        # select the new alpha2 which could get the minimal objectives
        if eta > 0.0:
            a2_new_unc = a2 + (y2 * (e1 - e2)) / eta
            # a2_new has a boundary
            if a2_new_unc >= H:
                a2_new = H
            elif a2_new_unc <= L:
                a2_new = L
            else:
                a2_new = a2_new_unc
        else:
            b = self._b
            l1 = a1 + s * (a2 - L)
            h1 = a1 + s * (a2 - H)

            # way 1
            f1 = y1 * (e1 + b) - a1 * K(i1, i1) - s * a2 * K(i1, i2)
            f2 = y2 * (e2 + b) - a2 * K(i2, i2) - s * a1 * K(i1, i2)
            ol = (
                l1 * f1
                + L * f2
                + 1 / 2 * l1 ** 2 * K(i1, i1)
                + 1 / 2 * L ** 2 * K(i2, i2)
                + s * L * l1 * K(i1, i2)
            )
            oh = (
                h1 * f1
                + H * f2
                + 1 / 2 * h1 ** 2 * K(i1, i1)
                + 1 / 2 * H ** 2 * K(i2, i2)
                + s * H * h1 * K(i1, i2)
            )
            """
            # way 2
            Use objective function check which alpha2 new could get the minimal
            objectives
            """
            if ol < (oh - self._eps):
                a2_new = L
            elif ol > oh + self._eps:
                a2_new = H
            else:
                a2_new = a2

        # a1_new has a boundary too
        a1_new = a1 + s * (a2 - a2_new)
        if a1_new < 0:
            a2_new += s * a1_new
            a1_new = 0
        if a1_new > self._c:
            a2_new += s * (a1_new - self._c)
            a1_new = self._c

        return a1_new, a2_new

    # Normalise data using min_max way
    def _norm(self, data):
        if self._init:
            self._min = np.min(data, axis=0)
            self._max = np.max(data, axis=0)
            self._init = False
            return (data - self._min) / (self._max - self._min)
        else:
            return (data - self._min) / (self._max - self._min)

    def _is_unbound(self, index):
        if 0.0 < self.alphas[index] < self._c:
            return True
        else:
            return False

    def _is_support(self, index):
        if self.alphas[index] > 0:
            return True
        else:
            return False

    @property
    def unbound(self):
        return self._unbound

    @property
    def support(self):
        return [i for i in range(self.length) if self._is_support(i)]

    @property
    def length(self):
        return self.samples.shape[0]


class Kernel:
    def __init__(self, kernel, degree=1.0, coef0=0.0, gamma=1.0):
        self.degree = np.float64(degree)
        self.coef0 = np.float64(coef0)
        self.gamma = np.float64(gamma)
        self._kernel_name = kernel
        self._kernel = self._get_kernel(kernel_name=kernel)
        self._check()

    def _polynomial(self, v1, v2):
        return (self.gamma * np.inner(v1, v2) + self.coef0) ** self.degree

    def _linear(self, v1, v2):
        return np.inner(v1, v2) + self.coef0

    def _rbf(self, v1, v2):
        return np.exp(-1 * (self.gamma * np.linalg.norm(v1 - v2) ** 2))

    def _check(self):
        if self._kernel == self._rbf:
            if self.gamma < 0:
                raise ValueError("gamma value must greater than 0")

    def _get_kernel(self, kernel_name):
        maps = {"linear": self._linear, "poly": self._polynomial, "rbf": self._rbf}
        return maps[kernel_name]

    def __call__(self, v1, v2):
        return self._kernel(v1, v2)

    def __repr__(self):
        return self._kernel_name


def count_time(func):
    def call_func(*args, **kwargs):
        import time

        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        print(f"smo algorithm cost {end_time - start_time} seconds")

    return call_func


@count_time
def test_cancel_data():
    print("Hello!\nStart test svm by smo algorithm!")
    # 0: download dataset and load into pandas' dataframe
    if not os.path.exists(r"cancel_data.csv"):
        request = urllib.request.Request(
            CANCER_DATASET_URL,
            headers={"User-Agent": "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"},
        )
        response = urllib.request.urlopen(request)
        content = response.read().decode("utf-8")
        with open(r"cancel_data.csv", "w") as f:
            f.write(content)

    data = pd.read_csv(r"cancel_data.csv", header=None)

    # 1: pre-processing data
    del data[data.columns.tolist()[0]]
    data = data.dropna(axis=0)
    data = data.replace({"M": np.float64(1), "B": np.float64(-1)})
    samples = np.array(data)[:, :]

    # 2: dividing data into train_data data and test_data data
    train_data, test_data = samples[:328, :], samples[328:, :]
    test_tags, test_samples = test_data[:, 0], test_data[:, 1:]

    # 3: choose kernel function,and set initial alphas to zero(optional)
    mykernel = Kernel(kernel="rbf", degree=5, coef0=1, gamma=0.5)
    al = np.zeros(train_data.shape[0])

    # 4: calculating best alphas using SMO algorithm and predict test_data samples
    mysvm = SmoSVM(
        train=train_data,
        kernel_func=mykernel,
        alpha_list=al,
        cost=0.4,
        b=0.0,
        tolerance=0.001,
    )
    mysvm.fit()
    predict = mysvm.predict(test_samples)

    # 5: check accuracy
    score = 0
    test_num = test_tags.shape[0]
    for i in range(test_tags.shape[0]):
        if test_tags[i] == predict[i]:
            score += 1
    print(f"\nall: {test_num}\nright: {score}\nfalse: {test_num - score}")
    print(f"Rough Accuracy: {score / test_tags.shape[0]}")


def test_demonstration():
    # change stdout
    print("\nStart plot,please wait!!!")
    sys.stdout = open(os.devnull, "w")

    ax1 = plt.subplot2grid((2, 2), (0, 0))
    ax2 = plt.subplot2grid((2, 2), (0, 1))
    ax3 = plt.subplot2grid((2, 2), (1, 0))
    ax4 = plt.subplot2grid((2, 2), (1, 1))
    ax1.set_title("linear svm,cost:0.1")
    test_linear_kernel(ax1, cost=0.1)
    ax2.set_title("linear svm,cost:500")
    test_linear_kernel(ax2, cost=500)
    ax3.set_title("rbf kernel svm,cost:0.1")
    test_rbf_kernel(ax3, cost=0.1)
    ax4.set_title("rbf kernel svm,cost:500")
    test_rbf_kernel(ax4, cost=500)

    sys.stdout = sys.__stdout__
    print("Plot done!!!")


def test_linear_kernel(ax, cost):
    train_x, train_y = make_blobs(
        n_samples=500, centers=2, n_features=2, random_state=1
    )
    train_y[train_y == 0] = -1
    scaler = StandardScaler()
    train_x_scaled = scaler.fit_transform(train_x, train_y)
    train_data = np.hstack((train_y.reshape(500, 1), train_x_scaled))
    mykernel = Kernel(kernel="linear", degree=5, coef0=1, gamma=0.5)
    mysvm = SmoSVM(
        train=train_data,
        kernel_func=mykernel,
        cost=cost,
        tolerance=0.001,
        auto_norm=False,
    )
    mysvm.fit()
    plot_partition_boundary(mysvm, train_data, ax=ax)


def test_rbf_kernel(ax, cost):
    train_x, train_y = make_circles(
        n_samples=500, noise=0.1, factor=0.1, random_state=1
    )
    train_y[train_y == 0] = -1
    scaler = StandardScaler()
    train_x_scaled = scaler.fit_transform(train_x, train_y)
    train_data = np.hstack((train_y.reshape(500, 1), train_x_scaled))
    mykernel = Kernel(kernel="rbf", degree=5, coef0=1, gamma=0.5)
    mysvm = SmoSVM(
        train=train_data,
        kernel_func=mykernel,
        cost=cost,
        tolerance=0.001,
        auto_norm=False,
    )
    mysvm.fit()
    plot_partition_boundary(mysvm, train_data, ax=ax)


def plot_partition_boundary(
    model, train_data, ax, resolution=100, colors=("b", "k", "r")
):
    """
    We can not get the optimum w of our kernel svm model which is different from linear
    svm.  For this reason, we generate randomly distributed points with high desity and
    prediced values of these points are calculated by using our tained model. Then we
    could use this prediced values to draw contour map.
    And this contour map can represent svm's partition boundary.
    """
    train_data_x = train_data[:, 1]
    train_data_y = train_data[:, 2]
    train_data_tags = train_data[:, 0]
    xrange = np.linspace(train_data_x.min(), train_data_x.max(), resolution)
    yrange = np.linspace(train_data_y.min(), train_data_y.max(), resolution)
    test_samples = np.array([(x, y) for x in xrange for y in yrange]).reshape(
        resolution * resolution, 2
    )

    test_tags = model.predict(test_samples, classify=False)
    grid = test_tags.reshape((len(xrange), len(yrange)))

    # Plot contour map which represents the partition boundary
    ax.contour(
        xrange,
        yrange,
        np.mat(grid).T,
        levels=(-1, 0, 1),
        linestyles=("--", "-", "--"),
        linewidths=(1, 1, 1),
        colors=colors,
    )
    # Plot all train samples
    ax.scatter(
        train_data_x,
        train_data_y,
        c=train_data_tags,
        cmap=plt.cm.Dark2,
        lw=0,
        alpha=0.5,
    )

    # Plot support vectors
    support = model.support
    ax.scatter(
        train_data_x[support],
        train_data_y[support],
        c=train_data_tags[support],
        cmap=plt.cm.Dark2,
    )


if __name__ == "__main__":
    test_cancel_data()
    test_demonstration()
    plt.show()
