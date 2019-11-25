"""
    Linear Discriminant Analysis


    Assumptions About Data :
        1. The input variables has a gaussian distribution.
        2. The variance calculated for each input variables by class grouping is the same.
        3. The mix of classes in your training set is representative of the problem.


    Learning The Model :
        The LDA model requires the estimation of statistics from the training data :
            1. Mean of each input value for each class.
            2. Probability of an instance belong to each class.
            3. Covariance for the input data for each class

        Calculate the class means :
            mean(x) = 1/n ( for i = 1 to i = n --> sum(xi))

        Calculate the class probabilities :
            P(y = 0) = count(y = 0) / (count(y = 0) + count(y = 1))
            P(y = 1) = count(y = 1) / (count(y = 0) + count(y = 1))

        Calculate the variance :
            We can calculate the variance for dataset in two steps :
                1. Calculate the squared difference for each input variable from the group mean.
                2. Calculate the mean of the squared difference.
                ------------------------------------------------
                Squared_Difference = (x - mean(k)) ** 2
                Variance = (1 / (count(x) - count(classes))) * (for i = 1 to i = n --> sum(Squared_Difference(xi)))

    Making Predictions :
        discriminant(x) = x * (mean / variance) - ((mean ** 2) / (2 * variance)) + Ln(probability)
        ------------------------------------------------------------------------------------------
        After calculating the discriminant value for each class, the class with the largest discriminant value
        is taken as the prediction.

    Author: @EverLookNeverSee

"""

# importing modules
from random import gauss
from math import log
from os import system, name     # to use < clear > or < cls > commands in terminal or cmd


# Making training dataset drawn from a gaussian distribution
def Normal_gen(mean: float, std_dev: float, instance_count: int) -> list:
    """ This function generates gaussian distribution instances
        based-on given mean and standard deviation
        :param mean: mean value of class
        :param std_dev: value of standard deviation entered by usr or default value of it
        :param instance_count: instance number of class
        :return: a list containing generated values based-on given mean, std_dev and instance_count
        """
    generated_instances = []  # An empty list to store generated instances
    # for loop iterates over instance_count
    for r in range(instance_count):
        # appending corresponding gaussian distribution to 'generated_instances' list
        generated_instances.append(gauss(mean, std_dev))

    return generated_instances


# Making corresponding Y flags to detecting classes
def Y_gen(class_count: int, instance_count: list) -> list:
    """ This function generates y values for corresponding classes
    :param class_count: Number of classes(data groupings) in dataset
    :param instance_count: number of instances in class
    :return: corresponding values for data groupings in dataset
    """
    ys = []  # An empty list to store generated corresponding Ys
    # for loop iterates over class_count
    for k in range(class_count):
        # for loop iterates over related number of instances of each class
        for p in range(instance_count[k]):
            # appending corresponding Ys to 'ys' list
            ys.append(k)
    return ys


# Calculating the class means
def mean_calc(instance_count: int, items: list) -> float:
    """ This function calculates given class mean
    :param instance_count: Number of instances in class
    :param items: items that related to specific class(data grouping)
    :return: calculated actual mean of considered class
    """
    # the sum of all items divided by number of instances
    class_mean = sum(items) / instance_count
    return class_mean


# Calculating the class probabilities
def prob_calc(instance_count: int, total_count: int) -> float:
    """ This function calculates the probability that a given instance
        will belong to which class
        :param instance_count: number of instances in class
        :param total_count: the number of all instances
        :return: value of probability for considered class
        """
    # number of instances in specific class divided by number of all instances
    probability = instance_count / total_count
    return probability


# Calculating the variance
def var_calc(items: list, means: list, total_count: int) -> float:
    """ This function calculates the variance
    :param items: a list containing all items(gaussian distribution of all classes)
    :param means: a list containing real mean values of each class
    :param total_count: the number of all instances
    :return: calculated variance for considered dataset
    """

    squared_diff = []  # An empty list to store all squared differences
    n_classes = len(means)  # Number of classes in dataSet

    # for loo iterates over number of elements in items
    for i in range(len(items)):
        # for loop iterates over number of elements in inner layer of items
        for j in range(len(items[i])):
            # appending squared differences to 'squared_diff' list
            squared_diff.append((items[i][j] - means[i]) ** 2)

    # one divided by (the number of all instances - number of classes) multiplied by sum of all squared differences
    variance = 1 / (total_count - n_classes) * sum(squared_diff)
    return variance


# Making predictions
def predict(x_items: list, means: list, variance: float, probabilities: list) -> list:
    """ This function predicts new indexes(groups for our data)
    :param x_items: a list containing all items(gaussian distribution of all classes)
    :param means: a list containing real mean values of each class
    :param variance: calculated value of variance by var_calc function
    :param probabilities: a list containing all probabilities of classes
    :return: a list containing predicted Y values
    """

    results = []    # An empty list to store generated discriminant values of all items in dataset for each class
    # for loop iterates over number of elements in list
    for i in range(len(x_items)):
        # for loop iterates over number of inner items of each element
        for j in range(len(x_items[i])):
            temp = []   # to store all discriminant values of each item as a list
            # for loop iterates over number of classes we have in our dataset
            for k in range(len(x_items)):
                # appending values of discriminants for each class to 'temp' list
                temp.append(x_items[i][j] * (means[k] / variance) - (means[k] ** 2 / (2 * variance)) +
                            log(probabilities[k]))
            # appending discriminant values of each item to 'results' list
            results.append(temp)

    print("Generated Discriminants: \n", results)

    predicted_index = []    # An empty list to store predicted indexes
    # for loop iterates over elements in 'results'
    for l in results:
        # after calculating the discriminant value for each class , the class with the largest
        # discriminant value is taken as the prediction, than we try to get index of that.
        predicted_index.append(l.index(max(l)))
    return predicted_index
