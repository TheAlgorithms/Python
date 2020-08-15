#2D Transformations are regularly used in Linear Algebra.

#I have added the codes for reflection, projection, scaling and rotation matrices.

import numpy as np
import math 

def scaling(scaling_factor):
	return(scaling_factor*(np.identity(2))) #This returns a scaling matrix

def rotation(angle):
	arr = np.empty([2, 2])

	arr[0][0] = math.cos(angle)
	arr[0][1] = -math.sin(angle)
	arr[1][0] = math.sin(angle)
	arr[1][1] = math.cos(angle)

	return arr #This returns a rotation matrix


def projection(angle):
	arr = np.empty([2, 2])

	arr[0][0] = math.cos(angle)*math.cos(angle)
	arr[0][1] = math.sin(angle)*math.cos(angle)
	arr[1][0] = math.sin(angle)*math.cos(angle)
	arr[1][1] = math.sin(angle)*math.sin(angle)

	return arr #This returns a rotation matrix


def reflection(angle):
	arr = np.empty([2, 2])

	arr[0][0] = (2*math.cos(angle)) -1
	arr[0][1] = 2*math.sin(angle)*math.cos(angle)
	arr[1][0] = 2*math.sin(angle)*math.cos(angle)
	arr[1][1] = (2*math.sin(angle)) -1

	return arr #This returns a reflection matrix
