from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np

from adv_math_engine.series_expansion import maclaurin_series


def main() -> None:
    x = np.linspace(-2, 2, 300)
    y_actual = np.sin(x)

    plt.figure(figsize=(7, 5))
    plt.plot(x, y_actual, label="sin(x)", linewidth=2)
    for order in (1, 3, 5, 7):
        y_approx = maclaurin_series(x, order=order, function_name="sin")
        plt.plot(x, y_approx, label=f"Order {order}")

    plt.title("Maclaurin Approximation of sin(x)")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.tight_layout()
    plt.savefig("adv_math_engine/visualizations/series_approximation.png", dpi=160)


if __name__ == "__main__":
    main()
