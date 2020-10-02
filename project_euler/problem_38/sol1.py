'''
Problem:
Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?

'''
def is_pandigital():
  '''
  The function finds the largest pandigital number by looping from 1 to 1000, and concatinating the multiples untill a 9 digit number is achieved. It then using an if condition to check if the length of num1 is 9 without repititive digits and without the occurence of 0 in it.
  
  If these conditions hold true, it assigns num1 to the largest variable.

  This largest variable is the answer of problem 38.
  '''
  largest = 0 #this variable will be the largest 1 to 9 pandigital 9-digit number
  for i in range(1,1000):
    num1 = "" #a string is used and not int as we'll later be concatinating it to generate a 9 digital number.

    num2 = 1 

    while len(num1) < 9:
      num1 += str(i*num2) #concatinating the multiples until num1 has 9 digits.
      num2 += 1

    if len(num1) == 9 and len(set(num1)) == 9 and 0 not in num1:

      if int(num1) > largest:
        largest = int(num1)
  
  return largest

if __name__ == "__main__":
    print(f"The largest pandigital number is {is_pandigital()}")
