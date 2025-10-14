"""Amortization (level payment) utilities.

Computes the level annuity payment and a per-period amortization schedule.
Pure Python, no dependencies.

References
----------
https://en.wikipedia.org/wiki/Amortization_calculator
https://en.wikipedia.org/wiki/Amortization_schedule
"""


def level_payment(
    principal: float,
    annual_rate_pct: float,
    years: int,
    payments_per_year: int = 12,
) -> float:
    """Return the fixed payment for a fully amortizing loan.

    Parameters
    ----------
    principal : float
        Initial loan amount (> 0).
    annual_rate_pct : float
        Annual percentage rate, e.g., 6.0 for 6%.
    years : int
        Loan term in years (> 0).
    payments_per_year : int, default 12
        Number of payments per year (> 0).

    Returns
    -------
    float
        The level payment per period.

    Examples
    --------
    >>> round(level_payment(10_000, 6.0, 15, 12), 4)
    84.3857
    >>> round(level_payment(12_000, 0.0, 2, 12), 2)
    500.0
    """
    if principal <= 0:
        raise ValueError("principal must be > 0")
    if years <= 0 or payments_per_year <= 0:
        raise ValueError("years and payments_per_year must be > 0")

    r = (annual_rate_pct / 100.0) / payments_per_year
    n = years * payments_per_year
    if r == 0:
        return principal / n

    factor = (1 + r) ** n
    return principal * (r * factor) / (factor - 1)


def amortization_schedule(
    principal: float,
    annual_rate_pct: float,
    years: int,
    payments_per_year: int = 12,
    print_annual_summary: bool = False,
    eps: float = 1e-9,
) -> tuple[float, list[list[float]]]:
    """Generate a fully amortizing schedule.

    Each row is: [period, payment, interest, principal, balance]

    Parameters
    ----------
    principal : float
        Initial loan amount.
    annual_rate_pct : float
        Annual percentage rate (APR), e.g., 5.5 for 5.5%.
    years : int
        Loan term in years.
    payments_per_year : int, default 12
        Payments per year (e.g., 12 monthly, 4 quarterly, 26 biweekly).
    print_annual_summary : bool, default False
        If True, prints a one-line summary every 12 months.
    eps : float, default 1e-9
        Tolerance for floating-point comparisons.

    Returns
    -------
    (float, list[list[float]])
        Payment per period, and the amortization schedule.

    Examples
    --------
    >>> pmt, sched = amortization_schedule(10_000, 6.0, 15, 12)
    >>> round(pmt, 4)
    84.3857
    >>> round(sched[-1][4], 6)  # ending balance ~ 0
    0.0
    """
    pmt = level_payment(principal, annual_rate_pct, years, payments_per_year)
    r = (annual_rate_pct / 100.0) / payments_per_year
    n = years * payments_per_year

    balance = float(principal)
    schedule: list[list[float]] = []

    if print_annual_summary:
        print(
            (
                f"{'Year':<6}{'Months Pd':<12}{'Tenure Left':<13}"
                f"{'Payment/Period':<16}{'Outstanding':<14}"
            )
        )

    for period in range(1, n + 1):
        interest = balance * r
        principal_component = pmt - interest

        # Short-pay on the last period if the scheduled principal would over-shoot
        if principal_component > balance - eps:
            principal_component = balance
            payment_made = interest + principal_component
        else:
            payment_made = pmt

        # Clamp tiny negatives from FP noise
        if 0 > principal_component > -eps:
            principal_component = 0.0

        balance = max(0.0, balance - principal_component)
        schedule.append(
            [
                float(period),
                float(payment_made),
                float(interest),
                float(principal_component),
                float(balance),
            ]
        )

        # Works for any cadence (monthly/quarterly/biweekly/weekly)
        months_elapsed = round((period * 12) / payments_per_year)

        if print_annual_summary and (months_elapsed % 12 == 0 or balance <= eps):
            tenure_left = n - period
            print(
                (
                    f"{months_elapsed // 12:<6}{months_elapsed:<12}{tenure_left:<13}"
                    f"{pmt:<16.2f}{balance:<14.2f}"
                )
            )

        if balance <= eps:
            break

    # Normalize final tiny residual to exact zero for cleanliness
    if schedule and schedule[-1][4] <= eps:
        schedule[-1][4] = 0.0

    return round(pmt, 4), schedule
