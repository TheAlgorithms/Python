"""
Run Length Encoding
https://en.wikipedia.org/wiki/Run-length_encoding
"""


def run_length_encoding(data: str or tuple) -> tuple or str:
    """
    >>> run_length_encoding('taaaaaaaaaaanaayyyyy')
    ('tanay', [1, 11, 1, 2, 5])
    """
    if isinstance(data, str):
        count = 1
        code = ""
        run = []
        for idx, char in enumerate(data):
            if idx + 1 < len(data) and data[idx + 1] == char:
                count += 1
            else:
                code += char
                run.append(count)
                count = 1
        return (code, run)
    if isinstance(data, tuple):
        code = data[0]
        run = str(data[1])
        retstr = ""
        cidx = 0
        for r in run:
            r = int(r)
            retstr += "".join([code[cidx] for i in range(r)])
            cidx += 1
        return retstr


if __name__ == "__main__":
    import doctest

    doctest.testmod()
