"""
    Convert color to HEX code
    RGB  -> red 0-255, green 0-255, blue 0-255
    CMYK -> cyan 0-100, magenta 0-100, yellow 0-100, black 0-100
    HSL  -> hue 0-359, saturation 0-100, lightness 0-100
    HSV  -> hue 0-359, saturation 0-100, value 0-100
"""

dec_hex_dict = {
    0: '0',
    1: '1',
    2: '2',
    3: '3',
    4: '4',
    5: '5',
    6: '6',
    7: '7',
    8: '8',
    9: '9',
    10: 'A',
    11: 'B',
    12: 'C',
    13: 'D',
    14: 'E',
    15: 'F'}




def dec_to_hex_color(val):
    hex = dec_hex_dict[int(val / 16)] + dec_hex_dict[val % 16]
    return hex




def rgb_acc_from_hue(hue, C, X):
    red_acc, green_acc, blue_acc = 0, 0, 0
    hue_state = int(hue / 60)

    if hue_state == 0:
        red_acc, green_acc, blue_acc = C, X, 0
    elif hue_state == 1:
        red_acc, green_acc, blue_acc = X, C, 0
    elif hue_state == 2:
        red_acc, green_acc, blue_acc = 0, C, X
    elif hue_state == 3:
        red_acc, green_acc, blue_acc = 0, X, C
    elif hue_state == 4:
        red_acc, green_acc, blue_acc = X, 0, C
    elif hue_state == 5:
        red_acc, green_acc, blue_acc = C, 0, X

    return red_acc, green_acc, blue_acc




def cmyk_to_rgb(cyan, magenta, yellow, black):
    black_percent = black / 100
    red   = round(255 * (1 - (cyan / 100)) * (1 - black_percent))
    green = round(255 * (1 - (magenta / 100)) * (1 - black_percent))
    blue  = round(255 * (1 - (yellow / 100)) * (1 - black_percent))
    return red, green, blue

def hsl_to_rgb(hue, saturation, lightness):
    hue = hue if hue < 360 else 0
    saturation_percent = saturation / 100
    lightness_percent = lightness / 100

    C = (1 - abs((2 * lightness_percent) - 1)) * saturation_percent
    X = C * (1 - abs(((hue / 60) % 2) - 1))
    m = lightness_percent - (C / 2)

    red_acc, green_acc, blue_acc = rgb_acc_from_hue(hue, C, X)

    red   = round((red_acc + m) * 255)
    green = round((green_acc + m) * 255)
    blue  = round((blue_acc + m) * 255)
    return red, green, blue

def hsv_to_rgb(hue, saturation, value):
    hue = hue if hue < 360 else 0
    saturation_percent = saturation / 100
    value_percent = value / 100

    C = value_percent * saturation_percent
    X = C * (1 - abs(((hue / 60) % 2) - 1))
    m = value_percent - C

    red_acc, green_acc, blue_acc = rgb_acc_from_hue(hue, C, X)

    red   = round((red_acc + m) * 255)
    green = round((green_acc + m) * 255)
    blue  = round((blue_acc + m) * 255)
    return red, green, blue




def rgb_to_hex_color_code(red, green, blue, with_hash=True):
    hex_color_code = dec_to_hex_color(red) + dec_to_hex_color(green) + dec_to_hex_color(blue)
    prefix = '#' if with_hash else ''
    return prefix + hex_color_code

def cmyk_to_hex_color_code(cyan, magenta, yellow, black, with_hash=True):
    red, green, blue = cmyk_to_rgb(cyan, magenta, yellow, black)
    return rgb_to_hex_color_code(red, green, blue, with_hash)

def hsl_to_hex_color_code(hue, saturation, lightness, with_hash=True):
    red, green, blue = hsl_to_rgb(hue, saturation, lightness)
    return rgb_to_hex_color_code(red, green, blue, with_hash)

def hsv_to_hex_color_code(hue, saturation, value, with_hash=True):
    red, green, blue = hsv_to_rgb(hue, saturation, value)
    return rgb_to_hex_color_code(red, green, blue, with_hash)