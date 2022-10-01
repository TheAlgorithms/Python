#https://en.wikipedia.org/wiki/Fizz_buzz#Programming
number = 1
out = ""
iterations = 100

while number <= iterations:
  if number % 3 == 0:
      out += "Fizz"
  if number % 5 == 0: out +="Buzz"
  if out == "": out = number
  print(out)
  number += 1
