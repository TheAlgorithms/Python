"""
* Author: Cicero Tiago Carneiro Valentim (https://github.com/cicerotcv)
* Description: Convert hexadecimal (#FF2000) color to RGB (rgb(255, 32, 0)).

References:
https://www.w3schools.com/colors/colors_rgb.asp
https://www.w3schools.com/colors/colors_hexadecimal.asp
"""


def hex_to_rgb(hex_color: str) -> str:
    """
    Converts a hexadecimal color code to RGB values.

    Args:
        hex_color (str): A hexadecimal color code, e.g., "#RGB" or "#RRGGBB".

    Returns:
        str: A string representation of a rgb value "rgb(r, g, b)" containing
        three integers.

    Raises:
        ValueError: If the input hex_color is not a valid hexadecimal color code.

    Examples:
    >>> hex_to_rgb("#FF0000")
    'rgb(255, 0, 0)'

    >>> hex_to_rgb("#00FF00")
    'rgb(0, 255, 0)'

    >>> hex_to_rgb("#123")
    'rgb(17, 34, 51)'

    >>> hex_to_rgb("#000000")
    'rgb(0, 0, 0)'

    >>> hex_to_rgb("#FFFFFF")
    'rgb(255, 255, 255)'

    >>> hex_to_rgb("#0088FF")
    'rgb(0, 136, 255)'

    >>> hex_to_rgb("#0032ccAA")
    Traceback (most recent call last):
    ...
    ValueError: Invalid hex color code

    >>> hex_to_rgb("#0032")
    Traceback (most recent call last):
    ...
    ValueError: Invalid hex color code

    Note:
        - The function supports both 6-digit and 3-digit hex color codes.
    """

    hex_color = hex_color.lstrip("#")

    # Check if the input is a valid hex color code
    if not (len(hex_color) == 6 or len(hex_color) == 3):
        raise ValueError("Invalid hex color code")

    # Expand 3-digit hex codes to 6 digits (e.g., "#123" to "#112233")
    if len(hex_color) == 3:
        hex_color = "".join([char * 2 for char in hex_color])

    # Parse the hex values to integers
    red = int(hex_color[0:2], 16)
    green = int(hex_color[2:4], 16)
    blue = int(hex_color[4:6], 16)

    return f"rgb({red}, {green}, {blue})"


if __name__ == "__main__":
    import doctest

    doctest.testmod()
