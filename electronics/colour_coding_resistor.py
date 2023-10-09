from typing import List


def decode_resistor_colors(colors: List[str]) -> float:
    """
    Calculate the resistance value of a resistor based on its color bands.

    Args:
        colors (List[str]): List of color codes in the order they appear on
            the resistor.

    Returns:
        float: The resistance value in ohms.

    Raises:
        ValueError: If the input list does not have at least three color bands.

    Color Codes:
        - Black: 0
        - Brown: 1
        - Red: 2
        - Orange: 3
        - Yellow: 4
        - Green: 5
        - Blue: 6
        - Violet: 7
        - Gray: 8
        - White: 9
        - Gold: Multiply by 0.1
        - Silver: Multiply by 0.01
    """
    if len(colors) < 3:
        raise ValueError("A resistor must have at least three color bands.")

    color_values = {
        "black": 0,
        "brown": 1,
        "red": 2,
        "orange": 3,
        "yellow": 4,
        "green": 5,
        "blue": 6,
        "violet": 7,
        "gray": 8,
        "white": 9,
        "gold": 0.1,
        "silver": 0.01,
    }

    first_band_value = color_values.get(colors[0].lower(), None)
    second_band_value = color_values.get(colors[1].lower(), None)
    multiplier_value = color_values.get(colors[2].lower(), None)

    if None in (first_band_value, second_band_value, multiplier_value):
        raise ValueError("Invalid color code. Check the spelling and colors.")

    resistance = (first_band_value * 10 + second_band_value) * multiplier_value

    return resistance


if __name__ == "__main__":
    import doctest

    doctest.testmod()
