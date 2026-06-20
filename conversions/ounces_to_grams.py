"""
Convert ounces to grams.

This conversion uses the avoirdupois ounce:
1 ounce = 28.3495 grams
"""


def ounces_to_grams(ounces: float) -> float:
    """
    Convert ounces to grams.

    :param ounces: Weight in ounces
    :return: Weight in grams
    """
    if ounces < 0:
        raise ValueError("Weight cannot be negative")

    return ounces * 28.3495


if __name__ == "__main__":
    ounces = float(input("Enter weight in ounces: "))
    grams = ounces_to_grams(ounces)
    print(f"{ounces} ounces is equal to {grams:.2f} grams")
