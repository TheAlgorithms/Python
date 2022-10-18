"""
This program finds the approximate integration value/area under the curve of
a specified function within specified limits using Monte Carlo integration method.

Further, a graph of the individual areas under the curve considered for the calculation
is also plotted. (PLOT SECTION -> Optional implementation)

Link to source material:
https://towardsdatascience.com/the-basics-of-monte-carlo-integration-5fe16b40482d

"""

import doctest
import random

import numpy as np


def function_to_be_integrated(univariate_variable: int) -> float:
    """
    Function to calculate the sin of a particular value of x

    :param univariate_variable: int
    :return: float

    >>> round(function_to_be_integrated(0))
    0
    """

    return np.sin(univariate_variable)


def monte_carlo(lower_limit: int, upper_limit: int, number_of_sections: int) -> float:

    # Doctest
    """
    Monte Carlo integration function

    :param lower_limit: int
    :param upper_limit: int
    :param N: int
    :return: float

    >>> round(monte_carlo(0, np.pi, 1000))
    2
    """

    # list to store all the values for plotting
    plt_vals = []

    # array of zeros of length N
    ar = np.zeros(number_of_sections)

    # we iterate through all the values to generate
    # multiple results and show whose intensity is
    # the most.
    for i in range(number_of_sections):

        # iterating over each Value of ar and filling it
        # with a random value between the limits a and b
        for i in range(len(ar)):
            ar[i] = random.uniform(lower_limit, upper_limit)

        # variable to store sum of the functions of different
        # values of univariate_variable
        integral = 0.0

        # iterates and sums up values of different functions
        # of univariate_variable
        for i in ar:
            integral += function_to_be_integrated(i)

        # we get the answer by the formula derived adobe
        answer = (upper_limit - lower_limit) / float(number_of_sections) * integral
        # appends the solution to a list for plotting the graph
        plt_vals.append(answer)

    """
    #--------PLOT SECTION (OPTIONAL)----------#

    # import matplotlib.pyplot as plt

    # details of the plot to be generated
    # sets the title of the plot
    plt.title("Distributions of areas calculated")

    # 3 parameters (array on which histogram needs
    plt.hist(plt_vals, bins=30, ec="black")

    # sets the label of the x-axis of the plot
    plt.xlabel("Areas")
    plt.show() # shows the plot

    #-----END OF PLOT SECTION (OPTIONAL)------#
    """

    return sum(plt_vals) / number_of_sections  # taking the average value


if __name__ == "__main__":
    doctest.testmod()

    # define parameters
    # limits of integration (specify limits)
    # example limits
    lower_limit = 0
    upper_limit = np.pi  # gets the value of pi

    number_of_sections = 1000  # Number of individual ares to be considered

    # function call
    # the final area under the curve(integration) value is considered as the average
    # of all the individual areas calculated
    print(f"Approx. value: {monte_carlo(lower_limit,upper_limit,number_of_sections)}.")
