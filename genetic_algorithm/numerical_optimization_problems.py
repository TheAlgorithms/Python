# FUNCTIONS FOR NUMERICAL OPTIMIZATION PROBLEMS

# Reference: https://www.semanticscholar.org/paper/A-powerful-and-efficient-algorithm-for-numerical-Karabo%C4%9Fa-Basturk/4cb5dd388ea707bd421226d8c1ef61e7f56982e2
# See Section 3.1

import math

# Griewank: [-600, 600]
def griewank(x):
	total, prod=0, 1
	for i in range(len(x)):
		total += x[i]**2 / 4000
		prod *= math.cos(x[i]/math.sqrt(i+1))
	return 1+total-prod

# Rastrigin: [-15, 15]
def rastrigin(x):
	total=0
	for i in range(len(x)):
		total += x[i]**2 - 10*math.cos(2*math.pi*x[i]) + 10
	return total

# Ackley: [-32.768, 32.768]
def ackley(x):
	sum1=sum(x[i]**2 for i in range(len(x)))
	sum2=sum([math.cos(2*math.pi*x[i]) for i in range(len(x))])
	return -20*math.exp(-0.2*math.sqrt(sum1/len(x)))-math.exp(sum2/len(x))+20+math.e

# Rosenbrock: [-15, 15]
def rosenbrock(x):
	total=0
	for i in range(len(x)-1):
		total+=100 * (x[i+1]-x[i]**2)**2 + (x[i]-1)**2
	return total

# Schwefel: [-500, 500]
def schwefel(x):
	total=0
	for i in range(len(x)):
		total += -x[i]*math.sin(math.sqrt(abs(x[i])))
	return 418.9829*len(x)+total