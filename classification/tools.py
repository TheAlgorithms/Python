from matplotlib.image import imread
import matplotlib.pyplot as plt
from math import sqrt
import math
import random
import numpy
import operator
from scipy.spatial.distance import cdist
from scipy.linalg import norm
import datetime


def Histogram(path):
    image = imread(path)
    if len(image.shape) != 2:
        def gray(rgb): return numpy.dot(rgb[..., :3], [0.2989, 0.5870, 0.1140])
        gray = gray(image)
        image = gray
    hist, bins = numpy.histogram(image.ravel(), 256, [0, 256])
    return adapt(hist)
