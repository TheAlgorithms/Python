"""
Author : Rudransh Bhardwaj
Github : @rudransh61

"""

from turtle import * # importing the module required


speed('fastest') 

# turning the turtle to upwards
lt(90)

# the acute angle between
# the base and branch of the Y
angle = 30

# function to plot a Y
def y(sz:int, level:int):

	if level > 0:
		colormode(255)
		
		# into equal intervals for each level
		# setting the colour according to the current level
		pencolor(0, 255//level, 0)
		
		# drawing the base
		fd(sz)

		rt(angle)

		# recursive call for
		# the right subtree
		y(0.8 * sz, level-1)
		
		pencolor(0, 255//level, 0)
		
		lt( 2 * angle )

		# recursive call for
		# the left subtree
		y(0.8 * sz, level-1)
		
		pencolor(0, 255//level, 0)
		
		rt(angle)
		fd(-sz)
		
		
# sample tree of size 80 and level 7
y(80, 7)
