def rgb_to_cmyk(r_input: int, g_input: int, b_input: int) -> tuple[int, int, int, int]:
    """
    Simple RGB to CMYK conversion. Returns percentages of CMYK paint.
    https://www.programmingalgorithms.com/algorithm/rgb-to-cmyk/

    Note: this is a very popular algorithm that converts colors linearly and gives
    only approximate results. Actual preparation for printing requires advanced color
    conversion considering the color profiles and parameters of the target device.

    >>> rgb_to_cmyk(255, 200, "a")
    Traceback (most recent call last):
        ...
    ValueError: Expected int, found (<class 'int'>, <class 'int'>, <class 'str'>)

    >>> rgb_to_cmyk(255, 255, 999)
    Traceback (most recent call last):
        ...
    ValueError: Expected int of the range 0..255

    >>> rgb_to_cmyk(255, 255, 255)  # white
    (0, 0, 0, 0)

    >>> rgb_to_cmyk(128, 128, 128)  # gray
    (0, 0, 0, 50)

    >>> rgb_to_cmyk(0, 0, 0)    # black
    (0, 0, 0, 100)

    >>> rgb_to_cmyk(255, 0, 0)  # red
    (0, 100, 100, 0)

    >>> rgb_to_cmyk(0, 255, 0)  # green
    (100, 0, 100, 0)

    >>> rgb_to_cmyk(0, 0, 255)    # blue
    (100, 100, 0, 0)
    """

    if (
        not isinstance(r_input, int)
        or not isinstance(g_input, int)
        or not isinstance(b_input, int)
    ):
        msg = f"Expected int, found {type(r_input), type(g_input), type(b_input)}"
        raise ValueError(msg)

    if not 0 <= r_input < 256 or not 0 <= g_input < 256 or not 0 <= b_input < 256:
        raise ValueError("Expected int of the range 0..255")

    # changing range from 0..255 to 0..1
    r = r_input / 255
    g = g_input / 255
    b = b_input / 255

    k = 1 - max(r, g, b)

    if k == 1:  # pure black
        return 0, 0, 0, 100

    c = round(100 * (1 - r - k) / (1 - k))
    m = round(100 * (1 - g - k) / (1 - k))
    y = round(100 * (1 - b - k) / (1 - k))
    k = round(100 * k)

    return c, m, y, k


if __name__ == "__main__":
    from doctest import testmod

    testmod()
