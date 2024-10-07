"""
Given a grid, where you start from the top left position [0, 0],
you want to find how many paths you can take to get to the bottom right position.

start here  ->   0  0  0  0
                 1  1  0  0
                 0  0  0  1
                 0  1  0  0  <- finish here
how many 'distinct' paths can you take to get to the finish?
Using a recursive depth-first search algorithm below, you are able to
find the number of distinct unique paths (count).

'*' will demonstrate a path
In the example above, there are two distinct paths:
1.                2.
    *  *  *  0      *  *  *  *
    1  1  *  0      1  1  *  *
    0  0  *  1      0  0  *  1
    0  1  *  *      0  1  *  *
"""

intervals = [(4, 5), (0, 2), (2, 7), (1, 3), (0, 4)]
intervals.sort(key=lambda x: x[1])
count = 0
end = 0
answer = []

for interval in intervals:
    if end <= interval[0]:
        end = interval[1]
        count += 1
        answer.append(interval)

if __name__ == "__main__":
    import doctest

    doctest.testmod()
