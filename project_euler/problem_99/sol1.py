'''
https://projecteuler.net/problem=99

Problem Statement:

    Comparing two numbers written in index form like 2^11 and 3^7 is not difficult,
    as any calculator would confirm that 2^11 = 2048 < 3^7 = 2187.

    However, confirming that 632382^518061 > 519432^525806 would be much more difficult,
    as both numbers contain over three million digits.

    Using base_exp.txt (right click and 'Save Link/Target As...'),
    a 22K text file containing one thousand lines with a base/exponent pair on each line,
    determine which line number has the greatest numerical value.


'''

import csv
import math


def findLargestExponential(s):
    ''' function to recive a file and  determine
        which line number has the greatest numerical value.

    '''

    maxx=0
    with open(s,'rt')as f:
      data = csv.reader(f)
      for row in data:
          c=(math.log(int(row[0]),10)*int(row[1]))
          if maxx <= c:
              maxx=c
              l=row[0]
              r=row[1]
    return(str(l)+' '+str(r))

if __name__ == '__main__':
    print(findLargestExponential('p099_base_exp.txt'))
