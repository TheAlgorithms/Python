#https://en.wikipedia.org/wiki/Fizz_buzz#Programming

def fizz_buzz(number: int,out: str,iterations: int,fizz_number: int,buzz_number: int) -> None:
  """
  Plays FizzBuzz. Prints Fizz if number is a multiple of 3 and Buzz if its a multiple of 5
  Prints FizzBuzz if its a multiple of both 3 and 5 or 15. Else Prints The Number Itself.
  
  >>> fizz_buzz(1,"",7,3,5)
  1
  2
  Fizz
  4
  Buzz
  Fizz
  7
  >>> fizz_buzz(1,"",'a',3,5)
  Traceback (most recent call last):
    ...
  ValueError: iterations must be defined as integers
  >>> fizz_buzz(1,"",5,'a',5)
  Traceback (most recent call last):
    ...
  ValueError: fizz_number must be defined as an integer
  >>> fizz_buzz(1,"",5,3,'a')
  Traceback (most recent call last):
    ...
  ValueError: buzz_number must be defined as an integer
  >>> fizz_buzz(1,"",0,3,5)
  Traceback (most recent call last):
    ...
  ValueError: iterations must be done more than 0 times to play FizzBuzz
  >>> fizz_buzz('a',"",5,3,5)
  Traceback (most recent call last):
    ...
  ValueError: starting number must be and integer and be more than 0
  
  """
    
  if not type(iterations) == int:
    raise ValueError("iterations must be defined as integers")
  if not type(fizz_number) == int:
    raise ValueError("fizz_number must be defined as an integer")
  if not type(buzz_number) == int:
    raise ValueError("buzz_number must be defined as an integer")
  if not iterations >= 1:
    raise ValueError("iterations must be done more than 0 times to play FizzBuzz")
  if not type(number) == int or not number >= 1:
    raise ValueError("starting number must be and integer and be more than 0")  
    
  while number <= iterations:
    if number % fizz_number == 0:
      out += "Fizz"
    if number % buzz_number == 0:
      out += "Buzz"
    if out == "":
      out = str(number)
 
    print(out)
    number += 1
    out = ""

if __name__ == "__main__":
  import doctest
  doctest.testmod()
