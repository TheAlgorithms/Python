"""
Isolate the Decimal part of a Number
"""

def decimal_isolate(number, digitAmount):
  """
  Isolates the decimal part of a number.
  If digitAmount > 0 round to that decimal place, else print the entire decimal.
  >>> decimal_isolate(35.345, 1)
  0.3
  >>> decimal_isolate(89.345, 2)
  0.34
  >>> decimal_isolate(89.345, 3)
  0.345
  """
  if (digitAmount > 0):
    return round(number - int(number), digitAmount)
  return number - int(number)

if __name__ == "__main__":
  print(decimal_isolate(35.345, 1))
  print(decimal_isolate(35.345, 2))
  print(decimal_isolate(35.345, 3))
    
