'''
Problem Statement:
By counting carefully it can be seen that a rectangular 
grid measuring 3 by 2 contains eighteen rectangles:


Although there exists no rectangular grid that contains 
exactly two million rectangles, find the area of the grid with the nearest solution.

<<<<<<< HEAD
Approach:

=======
Approach:
>>>>>>> c4ecb74d98da02522cf42cc01e88301a58c61edb
Counting the number of rectangles for an x by y grid is given by the formula:

{(x^2 + x) * (y^2 + y)}/{4}

All we need to do is simply find an x and y that yield nearly 2,000,000 rectangles and calculate the area (xy).


'''

Rec = min_diff = 2000000

for x in range(2,101):
    for y in range(x,101):
        diff = abs(x*(x + 1) * y*(y + 1) / 4 - Rec)
        
        if diff  < min_diff:
            area  = x * y 
            min_diff = diff
print(area)
