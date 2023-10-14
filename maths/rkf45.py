from collections.abc import Callable
import numpy as np

class RangeError(Exception):
    'Will be raised when initial x is greater than or equal to final x'
    pass

def rkf45(ode:Callable , y0:float,x0:float,step_size:float,xn:float,) ->np.ndarray:
    """
    Calculate Numerical-Solution to an ODE at each nodal point using Runge-Kutta-Fehlberg Method (rkf45) of order 5.

    Reference: https://en.wikipedia.org/wiki/Runge%E2%80%93Kutta%E2%80%93Fehlberg_method

    args:
    ode (callable): Ordinary Differential Equation as function of x and y.
    y0 (float) : Initial value of y.
    x0 (float) : Initial value of x.
    step_size (float) : Increament value of x (step-size).
    xn (float) : Final value of x.
    

    Returns: 
        np.ndarray: Solution of y at each nodal point

    #excact value of y[1] is tan(0.2) = 0.2027100355086
    >>> def f(x,y):
    ...     return 1+y**2
    >>> y=rkf45(f,0,0,0.2,1)
    >>> y[1]
    0.2027100937470787
    """
    if x0>=xn:
        raise RangeError("Final value of x should be greater than initial value of x.")
    
    n=int((xn-x0)/step_size)
    y=np.zeros((n+1),)
    x=np.zeros(n+1)
    y[0]=y0
    x[0]=x0
    for i in range(n):
        k1=step_size*ode(x[i],y[i])
        k2=step_size*ode(x[i]+step_size/4,y[i]+k1/4)
        k3=step_size*ode(x[i]+(3/8)*step_size,y[i]+(3/32)*k1+(9/32)*k2)
        k4=step_size*ode(x[i]+(12/13)*step_size,y[i] +(1932/2197)*k1 -(7200/2197)*k2 +(7296/2197)*k3)
        k5=step_size*ode(x[i]+step_size,y[i]+(439/216)*k1-8*k2+(3680/513)*k3-(845/4104)*k4)
        k6=step_size*ode(x[i]+step_size/2,y[i]-(8/27)*k1+2*k2-(3544/2565)*k3+(1859/4104)*k4-(11/40)*k5)
        y[i+1]=y[i]+(16/135)*k1+(6656/12825)*k3+(28561/56430)*k4-(9/50)*k5+(2/55)*k6
        x[i+1]=step_size+x[i]
    return y

if __name__=='__main__':
    import doctest
    doctest.testmod()

