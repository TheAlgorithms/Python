"""
Calculate price plus tax of a good or service given
- Price
- Tax rate
"""


def price_plus_tax(price: float, tax_rate: float) -> float:
    """
    >>> price_plus_tax(100, 0.25)
    125.0
    >>> price_plus_tax(125.50, 0.05)
    131.775
    """
    # If the price is negative, it will raise a warning
    if price <= 0:
        raise Exception("The price must be >= 0")
    # If the tax rate is negative or zero, it will raise a warning
    if tax_rate <= 0:
        raise Exception("The tax rate must be > 0")

    return price * (1 + tax_rate)


if __name__ == "__main__":
    print(f"{price_plus_tax(100, 0.25) = }")
    print(f"{price_plus_tax(125.50, 0.05) = }")
