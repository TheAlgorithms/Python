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
