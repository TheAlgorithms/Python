# Normal Distribution QuickSort

QuickSort Algorithm where the pivot element is chosen randomly between first and last elements of the array, and the array elements are taken from Standard Normal Distribution.

## Array elements

The array elements are taken from a Standard Normal Distribution, having mean = 0 and standard deviation = 1.

### The code

```python

>>> import numpy as np
>>> from tempfile import TemporaryFile
>>> outfile = TemporaryFile()
>>> p = 100 # 100 elements are to be sorted
>>> mu, sigma = 0, 1 # mean and standard deviation
>>> X = np.random.normal(mu, sigma, p)
>>> np.save(outfile, X)
>>> 'The array is'
>>> X

```

------

#### The distribution of the array elements

```python
>>> mu, sigma = 0, 1 # mean and standard deviation
>>> s = np.random.normal(mu, sigma, p)
>>> count, bins, ignored = plt.hist(s, 30, normed=True)
>>> plt.plot(bins , 1/(sigma * np.sqrt(2 * np.pi)) *np.exp( - (bins - mu)**2 / (2 * sigma**2) ),linewidth=2, color='r')
>>> plt.show()
```

------
![normal distribution large](https://upload.wikimedia.org/wikipedia/commons/thumb/2/25/The_Normal_Distribution.svg/1280px-The_Normal_Distribution.svg.png)

------

## Comparing the numbers of comparisons

We can plot the function for Checking 'The Number of Comparisons' taking place between Normal Distribution QuickSort and Ordinary QuickSort:

```python
>>> import matplotlib.pyplot as plt

    # Normal Distribution QuickSort is red
>>> plt.plot([1,2,4,16,32,64,128,256,512,1024,2048],[1,1,6,15,43,136,340,800,2156,6821,16325],linewidth=2, color='r')

    # Ordinary QuickSort is green
>>> plt.plot([1,2,4,16,32,64,128,256,512,1024,2048],[1,1,4,16,67,122,362,949,2131,5086,12866],linewidth=2, color='g')

>>> plt.show()
```
