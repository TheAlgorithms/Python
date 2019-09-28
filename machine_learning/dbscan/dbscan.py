import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import make_moons


def distFunc(Q, P):
    """
        Calculates the Euclidean distance
        between pointd P and Q
    """
    a = pow((Q[0] - P[0]), 2)
    b = pow((Q[1] - P[1]), 2)
    return pow((a + b), 0.5)


def rangeQuery(DB, Q, eps):
    """
        Finds all points in the DB that
        are within a distance of eps from Q
    """
    Neighbors = []
    for P in DB:
        if distFunc(Q, P) <= eps:
            Neighbors.append(P)
    return Neighbors


def plot_cluster(DB, clusters, ax):
    """
        Extracts all the points in the DB and puts them together
        as seperate clusters and finally plots them
    """
    temp = []
    noise = []
    for i in clusters:
        stack = []
        for k, v in DB.items():
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


def DBSCAN(DB, eps, min_pts):
    """
        Implementation of the DBSCAN algorithm
    """
    clusters = []
    C = 0
    for P in DB:
        if DB[P]["label"] != "undefined":
            continue
        neighbors = rangeQuery(DB, P, eps)
        if len(neighbors) < min_pts:
            DB[P]["label"] = "noise"
            continue
        C += 1
        clusters.append(C)
        DB[P]["label"] = C
        neighbors.remove(P)  # remove itself
        seed_set = neighbors.copy()
        while seed_set != []:
            Q = seed_set.pop(0)
            if DB[Q]["label"] == "noise":
                DB[Q]["label"] = C
            if DB[Q]["label"] != "undefined":
                continue
            DB[Q]["label"] = C
            neighbors_n = rangeQuery(DB, Q, eps)
            if len(neighbors_n) >= min_pts:
                seed_set = seed_set + neighbors_n  ## seed_set U neighbors_n
    return DB, clusters


if __name__ == "__main__":

    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(7, 5))

    X, label = make_moons(n_samples=200, noise=0.1, random_state=19)

    axes[0].plot(X[:, 0], X[:, 1], "ro")

    points = {(point[0], point[1]): {"label": "undefined"} for point in X}

    eps = 0.25

    min_pts = 12

    DB, clusters = DBSCAN(points, eps, min_pts)

    plot_cluster(DB, clusters, axes[1])

    plt.show()
