"""
problem 85 -  https://projecteuler.net/problem=85

By counting carefully it can be seen that a rectangular grid
measuring 3 by 2 contains eighteen rectangles

Although there exists no rectangular grid that contains
exactly two million rectangles,
find the area of the grid with the nearest solution.

for 3 by 2 rectangle
there can be 18 rectangles

"""

def solution():

    """

    i want to take the error in finding a rectangle
    with 2Million possible rectangle as minimum
    as possible so i have took min_diff 9000

    no of possible rectangle is n(n+1)/2 in each side
    so total possible triangle is n1(n1+1) * n2(n2+1) /4

    """

    min_diff=9000

    area=0
    L=2000000

    for x in range(2,102):
        for y in range(2,102):
            rec=((x**2 + x)*(y**2 + y))/4
            diff_rec=abs(rec-L)
            if diff_rec < min_diff:
                min_diff=diff_rec
                area=x*y
    return area



if __name__ == "__main__":
    print(f"{solution() = }")
