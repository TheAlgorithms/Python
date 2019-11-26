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
def gaussian_distribution(mean: float, std_dev: float, instance_count: int) -> list:
    """ This function generates gaussian distribution instances
        based-on given mean and standard deviation
        :param mean: mean value of class
        :param std_dev: value of standard deviation entered by usr or default value of it
        :param instance_count: instance number of class
        :return: a list containing generated values based-on given mean, std_dev and instance_count
        """
    generated_instances = []  # An empty list to store generated instances
    return [gauss(mean, std_dev) for _ in range(instance_count)]


# Making corresponding Y flags to detecting classes
def y_generator(class_count: int, instance_count: list) -> list:
    """ This function generates y values for corresponding classes
    :param class_count: Number of classes(data groupings) in dataset
    :param instance_count: number of instances in class
    :return: corresponding values for data groupings in dataset
    """
    ys = []  # An empty list to store generated corresponding Ys
    # for loop iterates over class_count
    for k in range(class_count):
        return [k for _ in range(instance_count[k]) for k in range(class_count)]


# Calculating the class means
def calculate_mean(instance_count: int, items: list) -> float:
    """ This function calculates given class mean
    :param instance_count: Number of instances in class
    :param items: items that related to specific class(data grouping)
    :return: calculated actual mean of considered class
    """
    # the sum of all items divided by number of instances
    return sum(items) / instance_count


# Calculating the class probabilities
def calculate_probabilities(instance_count: int, total_count: int) -> float:
    """ This function calculates the probability that a given instance
        will belong to which class
        :param instance_count: number of instances in class
        :param total_count: the number of all instances
        :return: value of probability for considered class
        """
    # number of instances in specific class divided by number of all instances
    return instance_count / total_count


# Calculating the variance
def calculate_variance(items: list, means: list, total_count: int) -> float:
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
def predict_y_values(x_items: list, means: list, variance: float, probabilities: list) -> list:
    """ This function predicts new indexes(groups for our data)
    :param x_items: a list containing all items(gaussian distribution of all classes)
    :param means: a list containing real mean values of each class
    :param variance: calculated value of variance by calculate_variance function
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


# Calculating Accuracy
def accuracy(actual_y: list, predicted_y: list) -> float:
    """ This function calculates the value of accuracy based-on predictions
    :param actual_y:a list containing initial Y values generated by 'y_generator' function
    :param predicted_y: a list containing predicted Y values generated by 'predict_y_values' function
    :return: percentage of accuracy
    """
    correct = 0     # initial value for number of correct predictions
    # for loop iterates over one element of each list at a time (zip mode)
    for i, j in zip(actual_y, predicted_y):
        # if actual Y value equals to predicted Y value
        if i == j:
            # prediction is correct
            correct += 1
    # percentage of accuracy equals to number of correct predictions divided by number of
    # all data and multiplied by 100
    percentage = (correct / len(actual_y)) * 100
    return percentage


# Main Function
def main():
    """ This function starts execution phase """

    while True:

        print(" Linear Discriminant Analysis ".center(100, "*"))
        print("*" * 100, "\n")
        print("First of all we should specify the number of classes that \n"
              "we want to generate as training dataset")

        # Trying to get number of classes
        n_classes = 0
        while True:
            try:
                user_input = int(input("Enter the number of classes (Data Groupings): "))
                if user_input > 0:
                    n_classes = user_input
                    break
                else:
                    print("Your entered value is {} , Number of classes should be positive!".format(user_input))
                    continue
            except ValueError:
                print("Your entered value is not numerical!")

        print("-" * 100)

        std_dev = 1.0  # Default value for standard deviation of dataset
        # Trying to get the value of standard deviation
        while True:
            try:
                user_sd = float(input("Enter the value of standard deviation"
                                      "(Default value is 1.0 for all classes): ") or "1.0")
                if user_sd >= 0.0:
                    std_dev = user_sd
                    break
                else:
                    print("Your entered value is {}, Standard deviation should not be negative!".format(user_sd))
                    continue
            except ValueError:
                print("Your entered value is not numerical!")

        print("-" * 100)

        # Trying to get number of instances in classes and theirs means to generate dataset
        counts = []  # An empty list to store instance counts of classes in dataset
        for i in range(n_classes):
            while True:
                try:
                    user_count = int(input("Enter The number of instances for class_{}: ".format(i + 1)))
                    if user_count > 0:
                        counts.append(user_count)
                        break
                    else:
                        print("Your entered value is {}, Number of instances should be positive!".format(user_count))
                        continue
                except ValueError:
                    print("Your entered value is not numerical!")

        print("-" * 100)

        user_means = []  # An empty list to store values of user-entered means of classes
        for a in range(n_classes):
            while True:
                try:
                    user_mean = float(input("Enter the value of mean for class_{}: ".format(a + 1)))
                    if isinstance(user_mean, float):
                        user_means.append(user_mean)
                        break
                    else:
                        print("Your entered value is {}, And this is not valid!".format(user_mean))

                except ValueError:
                    print("Your entered value is not numerical!")

        print("-" * 100)

        print("Standard deviation: ", std_dev)

        # print out the number of instances in classes in separated line
        for b in range(len(counts)):
            print("Number of instances in class_{} is: {}".format(b + 1, counts[b]))

        print("-" * 100)

        # print out mean values of classes separated line
        for c in range(len(user_means)):
            print("Mean of class_{} is: {}".format(c + 1, user_means[c]))

        print("-" * 100)

        # Generating training dataset drawn from gaussian distribution
        x = []  # An empty list to store generated values of gaussian distribution
        # for loop iterates over number of classes
        for j in range(n_classes):
            # appending return values of 'gaussian_distribution' function to 'x' list
            x.append(gaussian_distribution(user_means[j], std_dev, counts[j]))
        print("Generated Normal Distribution: \n", x)

        print("-" * 100)

        # Generating Ys to detecting corresponding classes
        y = y_generator(n_classes, counts)
        print("Generated Corresponding Ys: \n", y)

        print("-" * 100)

        # Calculating the value of actual mean for each class
        actual_means = []  # An empty list to store value of actual means
        # for loop iterates over number of classes(data groupings)
        for k in range(n_classes):
            # appending return values of 'calculate_mean' function to 'actual_means' list
            actual_means.append(calculate_mean(counts[k], x[k]))
        # for loop iterates over number of elements in 'actual_means' list and print out them in separated line
        for d in range(len(actual_means)):
            print("Actual(Real) mean of class_{} is: {}".format(d + 1, actual_means[d]))

        print("-" * 100)

        # Calculating the value of probabilities for each class
        probabilities = []  # An empty list to store values of probabilities for each class
        # # for loop iterates over number of classes(data groupings)
        for l in range(n_classes):
            # appending return values of 'prob_calc' function to 'probabilities' list
            probabilities.append(calculate_probabilities(counts[l], sum(counts)))
        # for loop iterates over number of elements in 'probabilities' list and print out them in separated line
        for e in range(len(probabilities)):
            print("Probability of class_{} is: {}".format(e + 1, probabilities[e]))

        print("-" * 100)

        # Calculating the values of variance for each class
        variance = calculate_variance(x, actual_means, sum(counts))
        print("Variance: ", variance)

        print("-" * 100)

        # Predicting Y values
        # storing predicted Y values in 'pre_indexes' variable
        pre_indexes = predict_y_values(x, actual_means, variance, probabilities)

        print("-" * 100)

        # Calculating Accuracy of the model
        print("Accuracy: ", accuracy(y, pre_indexes))
        print("-" * 100)
        print(" DONE ".center(100, "+"))

        command = input("Press any key to restart and 'q' for quit: ")
        if command.lower() == "q":
            print("\n" + "GoodBye!".center(100, "-") + "\n")
            break
        else:
            if name == "nt":  # Related to Windows OS
                system("cls")
                continue
            else:  # Related to Mac OSX and Linux OS
                system("clear")
                continue


if __name__ == '__main__':
    main()
