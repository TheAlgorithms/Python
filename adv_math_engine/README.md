# adv_math_engine

Production-grade module for:
- Vector algebra
- Vector calculus
- Taylor / Maclaurin series expansion

## Structure

```text
adv_math_engine/
  ├── vector_algebra.py
  ├── vector_calculus.py
  ├── series_expansion.py
  ├── utils.py
  ├── benchmarks/
  ├── visualizations/
  ├── examples/
  └── tests/
```

## CLI

```bash
python main.py --function "sin(x)" --series taylor --order 5 --x 0.5 --center 0.0
```

## Visualizations

Run:

```bash
python adv_math_engine/visualizations/plot_gradient_field.py
python adv_math_engine/visualizations/plot_series_approximation.py
```

Outputs:
- `adv_math_engine/visualizations/gradient_field.png`
- `adv_math_engine/visualizations/series_approximation.png`

## Benchmarks

```bash
python adv_math_engine/benchmarks/benchmark_diff.py
```

See `adv_math_engine/benchmarks/results.md`.

## Coverage

Suggested command:

```bash
pytest adv_math_engine/tests --cov=adv_math_engine --cov-report=term-missing
```

See `adv_math_engine/tests/coverage_report.txt`.
