''' 
Problem statement:
The goal of this program is to return Pascal's triangle up to number 29. Pascal's triangle is the sum of the two upper corners.



   1 1

  1 2 1

 1 3 3 1

Create a function that returns a row from Pascal's triangle. To find the row and column you can use n!/(k!*(n-k)!) where n is the row down and k is the column

Input: Integer

Output: String

Sample Input: 4 

Sample Output: "1 4 6 4 1"

'''
#my newbie solution:
def pascals_triangle(row):
    new_string = ""
    for i in range (0,row+1):
        new_string+=str(bin_coeff(row,i))+" "
    return new_string.rstrip()

    
def bin_coeff(row,col):
    result = 1
    if col > (row-col):
        col = row - col
    for i in range (0,col):
        result *=(row -i)
        result//=(i+1)
    return result
