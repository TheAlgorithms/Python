'''
This program finds the approximate integration value/area under the curve of
a specified function within specified limits using Monte Carlo integration method.

Further, a graph of the individal areas under the curve considered for the calculation
is also plotted. (PLOT SECTION -> Optional implementation)
'''

# importing the modules
from scipy import random
import numpy as np
import matplotlib.pyplot as plt

# limits of integration (specify limits)
# example limits
a = 0
b = np.pi # gets the value of pi

N = 1000 # Number of individual ares to be considered

# function to calculate the sin of a particular value of x
# define your function
def f(x):
	return np.sin(x) # example function

# list to store all the values for plotting
plt_vals = []

#array of zeros of length N
ar = np.zeros(N)

# we iterate through all the values to generate
# multiple results and show whose intensity is
# the most.
for i in range(N):

	# iterating over each Value of ar and filling it
	# with a random value between the limits a and b
    for i in range (len(ar)):
        ar[i] = random.uniform(a,b)

	# variable to store sum of the functions of different
	# values of x
    integral = 0.0

	# iterates and sums up values of different functions
	# of x
    for i in ar:
        integral += f(i)

	# we get the answer by the formula derived adobe
    ans = (b-a)/float(N)*integral
	# appends the solution to a list for plotting the graph
    plt_vals.append(ans)
    #print(ans)


#--------PLOT SECTION (OPTIONAL)----------#

# details of the plot to be generated
# sets the title of the plot
plt.title("Distributions of areas calculated")

# 3 parameters (array on which histogram needs
plt.hist (plt_vals, bins=30, ec="black")

# to be made, bins, separators colour between the
# beams)
# sets the label of the x-axis of the plot
plt.xlabel("Areas")
plt.show() # shows the plot

#-----END OF PLOT SECTION (OPTIONAL)------#



# the final area under the curve(integration) value is considered as the average
# of all the individual areas calculated
print("\nThe value calculated by monte carlo integration is {}.".format(sum(plt_vals)/N))
