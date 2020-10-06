def rgb_to_hex(red: int, green: int, blue: int) -> str:
    """
    Convert the given RGB value to its hexadecimal equivalent

    >>> rgb_to_hex(255, 0, 0)
    '#ff0000'
    >>> rgb_to_hex(87, 181, 112)
    '#57b570'
    >>> rgb_to_hex(255, 255, 255)
    '#ffffff'
    >>> rgb_to_hex(0, 0, 0)
    '#000000'
    >>> rgb_to_hex(258, 44, 33)
    Traceback (most recent call last):
    ...
    ValueError: One or more of the values is not within range (0-255)
    """
    if max(red, green, blue) > 255 or min(red, green, blue) < 0:
        raise ValueError("One or more of the values is not within range (0-255)")
    return "#{:02x}{:02x}{:02x}".format(red, green, blue)


def hex_to_rgb(hex_color: str) -> tuple:
    """
    Convert the given hex color to an RGB tuple

    >>> hex_to_rgb('#ff0000')
    (255, 0, 0)
    >>> hex_to_rgb('#57b570')
    (87, 181, 112)
    >>> hex_to_rgb('#ffffff')
    (255, 255, 255)
    >>> hex_to_rgb('#000000')
    (0, 0, 0)
    >>> hex_to_rgb('#abcdabcdabcd')
    Traceback (most recent call last):
    ...
    ValueError: The hex value is invalid (not a valid color)
    >>> hex_to_rgb('#ababdq')
    Traceback (most recent call last):
    ...
    ValueError: The hex value is invalid (not a valid color)
    """

    hex_color = hex_color.lstrip("#")
    if len(hex_color) != 6:
        raise ValueError("The hex value is invalid (not a valid color)")

    try:
        rgb_values = [int(hex_color[i:i+2], 16) for i in (0, 2, 4)]
    except ValueError: raise ValueError("The hex value is invalid (not a valid color)")

    return tuple(rgb_values)

if __name__ == "__main__":
    from doctest import testmod
    testmod()
