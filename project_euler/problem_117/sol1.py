"""
Project Euler Problem 117: https://projecteuler.net/problem=117

Using a combination of grey square tiles and oblong tiles chosen from:
red tiles (measuring two units), green tiles (measuring three units),
and blue tiles (measuring four units),
it is possible to tile a row measuring five units in length
in exactly fifteen different ways.

    |grey|grey|grey|grey|grey|       |red,red|grey|grey|grey|

    |grey|red,red|grey|grey|         |grey|grey|red,red|grey|

    |grey|grey|grey|red,red|         |red,red|red,red|grey|

    |red,red|grey|red,red|           |grey|red,red|red,red|

    |green,green,green|grey|grey|    |grey|green,green,green|grey|

    |grey|grey|green,green,green|    |red,red|green,green,green|

    |green,green,green|red,red|      |blue,blue,blue,blue|grey|

    |grey|blue,blue,blue,blue|

How many ways can a row measuring fifty units in length be tiled?

NOTE: This is related to Problem 116 (https://projecteuler.net/problem=116).
"""


def solution(length: int = 50) -> int:
    """
    Returns the number of ways can a row of the given length be tiled

    >>> solution(5)
    15
    """

    ways_number = [1] * (length + 1)

    for row_length in range(length + 1):
        for tile_length in range(2, 5):
            for tile_start in range(row_length - tile_length + 1):
                ways_number[row_length] += ways_number[
                    row_length - tile_start - tile_length
                ]

    return ways_number[length]


if __name__ == "__main__":
    print(f"{solution() = }")
