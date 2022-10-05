#author: Arnav sharma @arnavjune2
import numpy as np
import pylab as p

def meanfilt (x, k):
    """Apply a length-k mean filter to a 1D array x.
    Boundaries are extended by repeating endpoints.
    """

    assert k % 2 == 1, "Mean filter length must be odd."
    assert x.ndim == 1, "Input must be one-dimensional."
    
    k2 = (k - 1) // 2
    y = np.zeros ((len (x), k), dtype=x.dtype)
    y[:,k2] = x
    for i in range (k2):
        j = k2 - i
        y[j:,i] = x[:-j]
        y[:j,i] = x[0]
        y[:-j,-(i+1)] = x[j:]
        y[-j:,-(i+1)] = x[-1]
    return np.mean (y, axis=1)

if __name__ == '__main__':
    def test ():
        x = np.linspace (0, 1, 101)
        x[3::10] = 1.5
        p.plot (x)
        p.plot (meanfilt(x,3))
        p.plot (medfilt (x,3))
        p.show ()
        
test()
