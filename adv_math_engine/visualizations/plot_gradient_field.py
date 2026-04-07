from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np


def main() -> None:
    x = np.linspace(-2, 2, 25)
    y = np.linspace(-2, 2, 25)
    xx, yy = np.meshgrid(x, y)

    # f(x, y) = x^2 + y^2 -> ∇f = (2x, 2y)
    u = 2 * xx
    v = 2 * yy

    plt.figure(figsize=(6, 5))
    plt.quiver(xx, yy, u, v)
    plt.title("Gradient Field of f(x,y)=x²+y²")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.tight_layout()
    plt.savefig("adv_math_engine/visualizations/gradient_field.png", dpi=160)


if __name__ == "__main__":
    main()
