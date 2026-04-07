"""CLI for adv_math_engine series approximations.

Example:
python main.py --function "sin(x)" --series taylor --order 5 --x 0.5 --center 0.0
"""

from __future__ import annotations

import argparse

import numpy as np

from adv_math_engine.series_expansion import maclaurin_series, taylor_series

FUNCTION_MAP = {
    "sin(x)": ("sin", np.sin),
    "cos(x)": ("cos", np.cos),
    "exp(x)": ("exp", np.exp),
    "log(1+x)": ("log1p", np.log1p),
}


def main() -> None:
    parser = argparse.ArgumentParser(description="Series approximation CLI")
    parser.add_argument("--function", required=True, choices=tuple(FUNCTION_MAP.keys()))
    parser.add_argument("--series", required=True, choices=("taylor", "maclaurin"))
    parser.add_argument("--order", required=True, type=int)
    parser.add_argument("--x", required=True, type=float)
    parser.add_argument("--center", type=float, default=0.0)
    args = parser.parse_args()

    function_name, actual_fn = FUNCTION_MAP[args.function]
    if args.series == "maclaurin":
        approximation = float(maclaurin_series(args.x, args.order, function_name=function_name))
    else:
        approximation = float(taylor_series(args.x, args.order, center=args.center, function_name=function_name))

    actual = float(actual_fn(args.x))
    abs_error = abs(actual - approximation)

    print(f"Function: {args.function}")
    print(f"Series: {args.series} (order={args.order}, center={args.center})")
    print(f"x = {args.x}")
    print(f"Approximation = {approximation:.12f}")
    print(f"Actual        = {actual:.12f}")
    print(f"Abs Error     = {abs_error:.3e}")


if __name__ == "__main__":
    main()
