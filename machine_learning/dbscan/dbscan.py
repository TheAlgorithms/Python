import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import make_moons
import warnings


def euclidean_distance(q, p):
    """
        Calculates the Euclidean distance
        between points q and p

        Distance can only be calculated between numeric values
        >>> euclidean_distance([1,'a'],[1,2])
        Traceback (most recent call last):
        ...
        ValueError: Non-numeric input detected

        The dimentions of both the points must be the same
        >>> euclidean_distance([1,1,1],[1,2])
        Traceback (most recent call last):
        ...
        ValueError: expected dimensions to be 2-d, instead got p:3 and q:2

        Supports only two dimentional points
        >>> euclidean_distance([1,1,1],[1,2])
        Traceback (most recent call last):
        ...
        ValueError: expected dimensions to be 2-d, instead got p:3 and q:2

        Input should be in the format [x,y] or (x,y)
        >>> euclidean_distance(1,2)
        Traceback (most recent call last):
        ...
        TypeError: inputs must be iterable, either list [x,y] or tuple (x,y)
    """
    if not hasattr(q, "__iter__") or not hasattr(p, "__iter__"):
        raise TypeError("inputs must be iterable, either list [x,y] or tuple (x,y)")

    if isinstance(q, str) or isinstance(p, str):
        raise TypeError("inputs cannot be str")

    if len(q) != 2 or len(p) != 2:
        raise ValueError(
            "expected dimensions to be 2-d, instead got p:{} and q:{}".format(
                len(q), len(p)
            )
        )

    for num in q + p:
        try:
            num = int(num)
        except:
            raise ValueError("Non-numeric input detected")

    a = pow((q[0] - p[0]), 2)
    b = pow((q[1] - p[1]), 2)
    return pow((a + b), 0.5)


def find_neighbors(db, q, eps):
    """
        Finds all points in the db that
        are within a distance of eps from Q

        eps value should be a number
        >>> find_neighbors({ (1,2):{'label':'undefined'}, (2,3):{'label':'undefined'}}, (2,5),'a')
        Traceback (most recent call last):
        ...
        ValueError: eps should be either int or float

        Q must be a 2-d point as list or tuple
        >>> find_neighbors({ (1,2):{'label':'undefined'}, (2,3):{'label':'undefined'}}, 2, 0.5)
        Traceback (most recent call last):
        ...
        TypeError: Q must a 2-dimentional point in the format (x,y) or [x,y]

        Points must be in correct format
        >>> find_neighbors([], (2,2) ,0.4)
        Traceback (most recent call last):
        ...
        TypeError: db must be a dict of points in the format {(x,y):{'label':'boolean/undefined'}}
    """

    if not isinstance(eps, (int, float)):
        raise ValueError("eps should be either int or float")

    if not hasattr(q, "__iter__"):
        raise TypeError("Q must a 2-dimentional point in the format (x,y) or [x,y]")

    if not isinstance(db, dict):
        raise TypeError(
            "db must be a dict of points in the format {(x,y):{'label':'boolean/undefined'}}"
        )

    return [p for p in db if euclidean_distance(q, p) <= eps]


def plot_cluster(db, clusters, ax):
    """
        Extracts all the points in the db and puts them together
        as seperate clusters and finally plots them

        db cannot be empty
        >>> fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(7, 5))
        >>> plot_cluster({},[1,2], axes[1] )
        Traceback (most recent call last):
        ...
        Exception: db is empty. No points to cluster

        clusters cannot be empty
        >>> fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(7, 5))
        >>> plot_cluster({ (1,2):{'label':'undefined'}, (2,3):{'label':'undefined'}},[],axes[1] )
        Traceback (most recent call last):
        ...
        Exception: nothing to cluster. Empty clusters

        clusters cannot be empty
        >>> fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(7, 5))
        >>> plot_cluster({ (1,2):{'label':'undefined'}, (2,3):{'label':'undefined'}},[],axes[1] )
        Traceback (most recent call last):
        ...
        Exception: nothing to cluster. Empty clusters

        ax must be a plotable
        >>> plot_cluster({ (1,2):{'label':'1'}, (2,3):{'label':'2'}},[1,2], [] )
        Traceback (most recent call last):
        ...
        TypeError: ax must be an slot in a matplotlib figure
    """
    if len(db) == 0:
        raise Exception("db is empty. No points to cluster")

    if len(clusters) == 0:
        raise Exception("nothing to cluster. Empty clusters")

    if not hasattr(ax, "plot"):
        raise TypeError("ax must be an slot in a matplotlib figure")

    temp = []
    noise = []
    for i in clusters:
        stack = []
        for k, v in db.items():
            if v["label"] == i:
                stack.append(k)
            elif v["label"] == "noise":
                noise.append(k)
        temp.append(stack)

    color = iter(plt.cm.rainbow(np.linspace(0, 1, len(clusters))))
    for i in range(0, len(temp)):
        c = next(color)
        x = [l[0] for l in temp[i]]
        y = [l[1] for l in temp[i]]
        ax.plot(x, y, "ro", c=c)

    x = [l[0] for l in noise]
    y = [l[1] for l in noise]
    ax.plot(x, y, "ro", c="0")


def dbscan(db, eps, min_pts):
    """
        Implementation of the DBSCAN algorithm

        Points must be in correct format
        >>> dbscan([], (2,2) ,0.4)
        Traceback (most recent call last):
        ...
        TypeError: db must be a dict of points in the format {(x,y):{'label':'boolean/undefined'}}

        eps value should be a number
        >>> dbscan({ (1,2):{'label':'undefined'}, (2,3):{'label':'undefined'}},'a',20 )
        Traceback (most recent call last):
        ...
        ValueError: eps should be either int or float

        min_pts value should be an integer
        >>> dbscan({ (1,2):{'label':'undefined'}, (2,3):{'label':'undefined'}},0.4,20.0 )
        Traceback (most recent call last):
        ...
        ValueError: min_pts should be int

        db cannot be empty
        >>> dbscan({},0.4,20.0 )
        Traceback (most recent call last):
        ...
        Exception: db is empty, nothing to cluster

        min_pts cannot be negative
        >>> dbscan({ (1,2):{'label':'undefined'}, (2,3):{'label':'undefined'}}, 0.4, -20)
        Traceback (most recent call last):
        ...
        ValueError: min_pts or eps cannot be negative

        eps cannot be negative
        >>> dbscan({ (1,2):{'label':'undefined'}, (2,3):{'label':'undefined'}},-0.4, 20)
        Traceback (most recent call last):
        ...
        ValueError: min_pts or eps cannot be negative

    """
    if not isinstance(db, dict):
        raise TypeError(
            "db must be a dict of points in the format {(x,y):{'label':'boolean/undefined'}}"
        )

    if len(db) == 0:
        raise Exception("db is empty, nothing to cluster")

    if not isinstance(eps, (int, float)):
        raise ValueError("eps should be either int or float")

    if not isinstance(min_pts, int):
        raise ValueError("min_pts should be int")

    if min_pts < 0 or eps < 0:
        raise ValueError("min_pts or eps cannot be negative")

    if min_pts == 0:
        warnings.warn("min_pts is 0. Are you sure you want this ?")

    if eps == 0:
        warnings.warn("eps is 0. Are you sure you want this ?")

    clusters = []
    c = 0
    for p in db:
        if db[p]["label"] != "undefined":
            continue
        neighbors = find_neighbors(db, p, eps)
        if len(neighbors) < min_pts:
            db[p]["label"] = "noise"
            continue
        c += 1
        clusters.append(c)
        db[p]["label"] = c
        neighbors.remove(p)
        seed_set = neighbors.copy()
        while seed_set != []:
            q = seed_set.pop(0)
            if db[q]["label"] == "noise":
                db[q]["label"] = c
            if db[q]["label"] != "undefined":
                continue
            db[q]["label"] = c
            neighbors_n = find_neighbors(db, q, eps)
            if len(neighbors_n) >= min_pts:
                seed_set = seed_set + neighbors_n
    return db, clusters


if __name__ == "__main__":

    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(7, 5))

    x, label = make_moons(n_samples=200, noise=0.1, random_state=19)

    axes[0].plot(x[:, 0], x[:, 1], "ro")

    points = {(point[0], point[1]): {"label": "undefined"} for point in x}

    eps = 0.25

    min_pts = 12

    db, clusters = dbscan(points, eps, min_pts)

    plot_cluster(db, clusters, axes[1])

    plt.show()
