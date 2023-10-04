"""
Calculate price plus tax of a good or service given its price and a tax rate.
"""


def price_plus_tax(price: float, tax_rate: float) -> float:
    """
    >>> price_plus_tax(100, 0.25)
    125.0
    >>> price_plus_tax(125.50, 0.05)
    131.775
    """
    return price * (1 + tax_rate)


if __name__ == "__main__":
    print(f"{price_plus_tax(100, 0.25) = }")
    print(f"{price_plus_tax(125.50, 0.05) = }")
