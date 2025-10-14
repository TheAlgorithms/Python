"""
Wiki: https://en.wikipedia.org/wiki/Amortization_calculator
"""


def level_payment(principal, annual_rate_pct, years, payments_per_year=12):
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
    principal,
    annual_rate_pct,
    years,
    payments_per_year=12,
    print_annual_summary=False,
    eps=1e-9,
):
    pmt = level_payment(principal, annual_rate_pct, years, payments_per_year)
    r = (annual_rate_pct / 100.0) / payments_per_year
    n = years * payments_per_year

    balance = float(principal)
    schedule = []

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

        # shortpay on the last period if the scheduled principal would overshoot
        if principal_component > balance - eps:
            principal_component = balance
            payment_made = interest + principal_component
        else:
            payment_made = pmt

        if (
            principal_component < 0 and principal_component > -eps
        ):  # clamp tiny negatives
            principal_component = 0.0

        balance = max(0.0, balance - principal_component)
        schedule.append([period, payment_made, interest, principal_component, balance])

        # streamline for all time periods (monthly/quarterly/biweekly/weekly)
        months_elapsed = round((period * 12) / payments_per_year)

        if print_annual_summary and (months_elapsed % 12 == 0 or balance <= eps):
            tenure_left_periods = n - period
            print(
                (
                    f"{months_elapsed // 12:<6}{months_elapsed:<12}{tenure_left_periods:<13}"
                    f"{pmt:<16.2f}{balance:<14.2f}"
                )
            )

        if balance <= eps:
            break

    # normalize any tiny residual
    if schedule and schedule[-1][4] <= eps:
        schedule[-1][4] = 0.0

    return round(pmt, 4), schedule
