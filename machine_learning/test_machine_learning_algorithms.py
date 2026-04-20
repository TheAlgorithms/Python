import numpy as np
import pandas as pd
import pytest

from machine_learning.gradient_descent import batch_gradient_descent_step
from machine_learning.k_means_clust import kmeans, report_generator
from machine_learning.linear_regression import run_steep_gradient_descent


def test_kmeans_converges_on_toy_dataset() -> None:
    data = np.array([[0.0, 0.0], [0.0, 1.0], [5.0, 5.0]])
    heterogeneity: list[float] = []
    centroids, labels = kmeans(
        data,
        k=2,
        initial_centroids=np.array([[0.0, 0.0], [5.0, 5.0]]),
        maxiter=10,
        record_heterogeneity=heterogeneity,
    )

    assert labels.tolist() == [0, 0, 1]
    assert heterogeneity == [pytest.approx(0.5)]
    assert np.allclose(centroids, np.array([[0.0, 0.5], [5.0, 5.0]]))


def test_report_generator_marks_requested_features() -> None:
    predicted = pd.DataFrame({"spend": [0.0, 50.0, 100.0], "Cluster": [0, 0, 1]})
    report = report_generator(predicted, clustering_variables=["spend"])

    cluster_sizes = report.loc[report["Features"] == "# of Customers", [0, 1]].iloc[0]
    assert cluster_sizes[0] == pytest.approx(2)
    assert cluster_sizes[1] == pytest.approx(1)
    assert bool(report.loc[report["Features"] == "spend", "Mark"].iloc[0])


def test_batch_gradient_descent_step_updates_parameters() -> None:
    dataset = (((1.0, 0.0, 0.0), 1.0), ((0.0, 1.0, 0.0), 1.0))
    updated = batch_gradient_descent_step([0.0, 0.0, 0.0, 0.0], 0.1, dataset)

    assert updated == pytest.approx([0.1, 0.05, 0.05, 0.0])


def test_run_steep_gradient_descent_matches_expected_step() -> None:
    data_x = np.array([[1.0, 0.0], [1.0, 1.0], [1.0, 2.0]])
    data_y = np.array([1.0, 4.0, 7.0])
    theta = np.zeros(2)

    new_theta = run_steep_gradient_descent(data_x, data_y, len(data_x), 0.05, theta)
    assert np.allclose(new_theta, np.array([0.2, 0.3]))
