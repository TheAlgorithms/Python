import enum

class Rainbow(enum.Enum):
   VIOLET = 1
   INDIGO = 2
   BLUE = 3
   GREEN = 4
   YELLOW = 5
   ORANGE = 6
   RED = 7
    
print('The 3rd Color of Rainbow is: ' + str(Rainbow(3)))
print('The number of orange color in rainbow is: ' + str(Rainbow['ORANGE'].value))

my_rainbow_green = Rainbow.GREEN

print('The selected color {} and Value {}'.format(my_rainbow_green.name, my_rainbow_green.value))
