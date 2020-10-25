# coding=utf-8
"""
This program read the part of text before comment char ('#') with selective_reading()

>>> selective_reading("hello #world")
'hello'
"""
def selective_reading(line):
    """
    will capture only before #

    >>> selective_reading("Hello #world")
    'Hello'
    >>> selective_reading("Hell#o world")
    'Hell'
    >>> selective_reading("#Hello world")
    ''
    >>> selective_reading("Hello world")
    'Hello world'
    >>> selective_reading("Hello world #")
    'Hello world'
    """

    line = line.partition('#')[0] # split the line into elements before "#" and after "#" 
    line = line.rstrip() # remove the after "#"
    return line
        
if __name__ == "__main__":
    import doctest
    doctest.testmod()
