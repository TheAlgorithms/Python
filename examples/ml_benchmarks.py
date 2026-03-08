"""Small benchmark harness for restored machine learning modules.

This script measures fit/predict timings for pure-Python educational
implementations and, when available, compares against scikit-learn baselines.
"""

from __future__ import annotations

import sys
from pathlib import Path

if __package__ is None or __package__ == "":
    sys.path.append(str(Path(__file__).resolve().parents[1]))

import random
import time
from collections.abc import Callable
from dataclasses import dataclass
from statistics import mean
from typing import Any

from machine_learning.gaussian_naive_bayes import GaussianNaiveBayes
from machine_learning.gradient_boosting_regressor import GradientBoostingRegressor
from machine_learning.random_forest_classifier import RandomForestClassifier
from machine_learning.random_forest_regressor import RandomForestRegressor


@dataclass(frozen=True)
class TimingResult:
    """Stores fit/predict duration in seconds."""

    fit_seconds: float
    predict_seconds: float


def _time_call(callable_obj: Callable[[], Any]) -> float:
    start = time.perf_counter()
    callable_obj()
    return time.perf_counter() - start


def _make_classification_data(
    n_samples: int = 400,
) -> tuple[list[list[float]], list[int]]:
    rng = random.Random(42)
    features: list[list[float]] = []
    labels: list[int] = []
    for _ in range(n_samples):
        x1 = rng.uniform(-2.0, 2.0)
        x2 = rng.uniform(-2.0, 2.0)
        features.append([x1, x2])
        labels.append(1 if x1 + x2 > 0 else 0)
    return features, labels


def _make_regression_data(
    n_samples: int = 400,
) -> tuple[list[list[float]], list[float]]:
    rng = random.Random(42)
    features: list[list[float]] = []
    targets: list[float] = []
    for _ in range(n_samples):
        x = rng.uniform(-5.0, 5.0)
        features.append([x])
        targets.append(3.0 * x + rng.uniform(-0.5, 0.5))
    return features, targets


def benchmark_pure_python_models() -> dict[str, TimingResult]:
    """Benchmark local educational implementations."""
    x_cls, y_cls = _make_classification_data()
    x_reg, y_reg = _make_regression_data()

    cls_model = RandomForestClassifier(num_trees=25, random_seed=42)
    cls_fit = _time_call(lambda: cls_model.fit(x_cls, y_cls))
    cls_predict = _time_call(lambda: cls_model.predict(x_cls[:100]))

    reg_model = RandomForestRegressor(num_trees=25, random_seed=42)
    reg_fit = _time_call(lambda: reg_model.fit(x_reg, y_reg))
    reg_predict = _time_call(lambda: reg_model.predict(x_reg[:100]))

    gbr_model = GradientBoostingRegressor(num_estimators=50, learning_rate=0.05)
    gbr_fit = _time_call(lambda: gbr_model.fit(x_reg, y_reg))
    gbr_predict = _time_call(lambda: gbr_model.predict(x_reg[:100]))

    gnb_model = GaussianNaiveBayes()
    gnb_fit = _time_call(lambda: gnb_model.fit(x_cls, y_cls))
    gnb_predict = _time_call(lambda: gnb_model.predict(x_cls[:100]))

    return {
        "RandomForestClassifier (pure)": TimingResult(cls_fit, cls_predict),
        "RandomForestRegressor (pure)": TimingResult(reg_fit, reg_predict),
        "GradientBoostingRegressor (pure)": TimingResult(gbr_fit, gbr_predict),
        "GaussianNaiveBayes (pure)": TimingResult(gnb_fit, gnb_predict),
    }


def benchmark_sklearn_if_available() -> dict[str, TimingResult]:
    """Benchmark sklearn models when sklearn is installed.

    Returns an empty dict when sklearn is unavailable.
    """
    try:
        from sklearn.ensemble import GradientBoostingRegressor as SklearnGBR
        from sklearn.ensemble import RandomForestClassifier as SklearnRFC
        from sklearn.ensemble import RandomForestRegressor as SklearnRFR
        from sklearn.naive_bayes import GaussianNB as SklearnGNB
    except ModuleNotFoundError:
        return {}

    x_cls, y_cls = _make_classification_data()
    x_reg, y_reg = _make_regression_data()

    rfc = SklearnRFC(n_estimators=100, random_state=42)
    rfc_fit = _time_call(lambda: rfc.fit(x_cls, y_cls))
    rfc_predict = _time_call(lambda: rfc.predict(x_cls[:100]))

    rfr = SklearnRFR(n_estimators=100, random_state=42)
    rfr_fit = _time_call(lambda: rfr.fit(x_reg, y_reg))
    rfr_predict = _time_call(lambda: rfr.predict(x_reg[:100]))

    gbr = SklearnGBR(n_estimators=100, learning_rate=0.05, random_state=42)
    gbr_fit = _time_call(lambda: gbr.fit(x_reg, y_reg))
    gbr_predict = _time_call(lambda: gbr.predict(x_reg[:100]))

    gnb = SklearnGNB()
    gnb_fit = _time_call(lambda: gnb.fit(x_cls, y_cls))
    gnb_predict = _time_call(lambda: gnb.predict(x_cls[:100]))

    return {
        "RandomForestClassifier (sklearn)": TimingResult(rfc_fit, rfc_predict),
        "RandomForestRegressor (sklearn)": TimingResult(rfr_fit, rfr_predict),
        "GradientBoostingRegressor (sklearn)": TimingResult(gbr_fit, gbr_predict),
        "GaussianNB (sklearn)": TimingResult(gnb_fit, gnb_predict),
    }


def _print_results(results: dict[str, TimingResult]) -> None:
    for name, result in results.items():
        print(
            f"{name:36} fit={result.fit_seconds:.6f}s "
            f"predict={result.predict_seconds:.6f}s"
        )


def main() -> None:
    pure_results = benchmark_pure_python_models()
    print("Pure-Python models:")
    _print_results(pure_results)

    if sklearn_results := benchmark_sklearn_if_available():
        print("\nscikit-learn models:")
        _print_results(sklearn_results)
    else:
        print("\nscikit-learn not available; skipping sklearn comparison.")

    avg_fit = mean(result.fit_seconds for result in pure_results.values())
    avg_predict = mean(result.predict_seconds for result in pure_results.values())
    print(f"\nAverage pure fit time: {avg_fit:.6f}s")
    print(f"Average pure predict time: {avg_predict:.6f}s")


if __name__ == "__main__":
    main()
