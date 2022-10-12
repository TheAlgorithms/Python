#Given two cells of a chessboard. If they are painted in one color, print the word YES, and if in a different color - NO. The program receives the input of four numbers from 1 to 8, each specifying the column and row number, first two - for the first cell, and then the last two - for the second cell.

x1 = int(input())
x2 = int(input())
y1 = int(input())
y2 = int(input())
if (x1 + x2) % 2 == (y1 + y2) % 2 :
    print ("YES")
else :
    print ("NO")
