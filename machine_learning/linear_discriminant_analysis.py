"""
    Linear Discriminant Analysis


    Assumptions About Data :
        1. The input variables has a gaussian distribution.
        2. The variance calculated for each input variables by class grouping is the
           same.
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
                1. Calculate the squared difference for each input variable from the
                   group mean.
                2. Calculate the mean of the squared difference.
                ------------------------------------------------
                Squared_Difference = (x - mean(k)) ** 2
                Variance = (1 / (count(x) - count(classes))) *
                    (for i = 1 to i = n --> sum(Squared_Difference(xi)))

    Making Predictions :
        discriminant(x) = x * (mean / variance) -
            ((mean ** 2) / (2 * variance)) + Ln(probability)
        ---------------------------------------------------------------------------
        After calculating the discriminant value for each class, the class with the
        largest discriminant value is taken as the prediction.

    Author: @EverLookNeverSee
"""
from math import log
from os import name, system
from random import gauss, seed


# Make a training dataset drawn from a gaussian distribution
def gaussian_distribution(mean: float, std_dev: float, instance_count: int) -> list:
    """
    Generate gaussian distribution instances based-on given mean and standard deviation
    :param mean: mean value of class
    :param std_dev: value of standard deviation entered by usr or default value of it
    :param instance_count: instance number of class
    :return: a list containing generated values based-on given mean, std_dev and
        instance_count

    >>> gaussian_distribution(5.0, 1.0, 20) # doctest: +NORMALIZE_WHITESPACE
    [6.288184753155463, 6.4494456086997705, 5.066335808938262, 4.235456349028368,
     3.9078267848958586, 5.031334516831717, 3.977896829989127, 3.56317055489747,
      5.199311976483754, 5.133374604658605, 5.546468300338232, 4.086029056264687,
       5.005005283626573, 4.935258239627312, 3.494170998739258, 5.537997178661033,
        5.320711100998849, 7.3891120432406865, 5.202969177309964, 4.855297691835079]
    """
    seed(1)
    return [gauss(mean, std_dev) for _ in range(instance_count)]


# Make corresponding Y flags to detecting classes
def y_generator(class_count: int, instance_count: list) -> list:
    """
    Generate y values for corresponding classes
    :param class_count: Number of classes(data groupings) in dataset
    :param instance_count: number of instances in class
    :return: corresponding values for data groupings in dataset

    >>> y_generator(1, [10])
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    >>> y_generator(2, [5, 10])
    [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    >>> y_generator(4, [10, 5, 15, 20]) # doctest: +NORMALIZE_WHITESPACE
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
     2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
    """

    return [k for k in range(class_count) for _ in range(instance_count[k])]


# Calculate the class means
def calculate_mean(instance_count: int, items: list) -> float:
    """
    Calculate given class mean
    :param instance_count: Number of instances in class
    :param items: items that related to specific class(data grouping)
    :return: calculated actual mean of considered class

    >>> items = gaussian_distribution(5.0, 1.0, 20)
    >>> calculate_mean(len(items), items)
    5.011267842911003
    """
    # the sum of all items divided by number of instances
    return sum(items) / instance_count


# Calculate the class probabilities
def calculate_probabilities(instance_count: int, total_count: int) -> float:
    """
    Calculate the probability that a given instance will belong to which class
    :param instance_count: number of instances in class
    :param total_count: the number of all instances
    :return: value of probability for considered class

    >>> calculate_probabilities(20, 60)
    0.3333333333333333
    >>> calculate_probabilities(30, 100)
    0.3
    """
    # number of instances in specific class divided by number of all instances
    return instance_count / total_count


# Calculate the variance
def calculate_variance(items: list, means: list, total_count: int) -> float:
    """
    Calculate the variance
    :param items: a list containing all items(gaussian distribution of all classes)
    :param means: a list containing real mean values of each class
    :param total_count: the number of all instances
    :return: calculated variance for considered dataset

    >>> items = gaussian_distribution(5.0, 1.0, 20)
    >>> means = [5.011267842911003]
    >>> total_count = 20
    >>> calculate_variance([items], means, total_count)
    0.9618530973487491
    """
    squared_diff = []  # An empty list to store all squared differences
    # iterate over number of elements in items
    for i in range(len(items)):
        # for loop iterates over number of elements in inner layer of items
        for j in range(len(items[i])):
            # appending squared differences to 'squared_diff' list
            squared_diff.append((items[i][j] - means[i]) ** 2)

    # one divided by (the number of all instances - number of classes) multiplied by
    # sum of all squared differences
    n_classes = len(means)  # Number of classes in dataset
    return 1 / (total_count - n_classes) * sum(squared_diff)


# Making predictions
def predict_y_values(
    x_items: list, means: list, variance: float, probabilities: list
) -> list:
    """This function predicts new indexes(groups for our data)
    :param x_items: a list containing all items(gaussian distribution of all classes)
    :param means: a list containing real mean values of each class
    :param variance: calculated value of variance by calculate_variance function
    :param probabilities: a list containing all probabilities of classes
    :return: a list containing predicted Y values

    >>> x_items = [[6.288184753155463, 6.4494456086997705, 5.066335808938262,
    ...                4.235456349028368, 3.9078267848958586, 5.031334516831717,
    ...                3.977896829989127, 3.56317055489747, 5.199311976483754,
    ...                5.133374604658605, 5.546468300338232, 4.086029056264687,
    ...                5.005005283626573, 4.935258239627312, 3.494170998739258,
    ...                5.537997178661033, 5.320711100998849, 7.3891120432406865,
    ...                5.202969177309964, 4.855297691835079], [11.288184753155463,
    ...                11.44944560869977, 10.066335808938263, 9.235456349028368,
    ...                8.907826784895859, 10.031334516831716, 8.977896829989128,
    ...                8.56317055489747, 10.199311976483754, 10.133374604658606,
    ...                10.546468300338232, 9.086029056264687, 10.005005283626572,
    ...                9.935258239627313, 8.494170998739259, 10.537997178661033,
    ...                10.320711100998848, 12.389112043240686, 10.202969177309964,
    ...                9.85529769183508], [16.288184753155463, 16.449445608699772,
    ...                15.066335808938263, 14.235456349028368, 13.907826784895859,
    ...                15.031334516831716, 13.977896829989128, 13.56317055489747,
    ...                15.199311976483754, 15.133374604658606, 15.546468300338232,
    ...                14.086029056264687, 15.005005283626572, 14.935258239627313,
    ...                13.494170998739259, 15.537997178661033, 15.320711100998848,
    ...                17.389112043240686, 15.202969177309964, 14.85529769183508]]

    >>> means = [5.011267842911003, 10.011267842911003, 15.011267842911002]
    >>> variance = 0.9618530973487494
    >>> probabilities = [0.3333333333333333, 0.3333333333333333, 0.3333333333333333]
    >>> predict_y_values(x_items, means, variance,
    ...                  probabilities)  # doctest: +NORMALIZE_WHITESPACE
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
    2, 2, 2, 2, 2, 2, 2, 2, 2]

    """
    # An empty list to store generated discriminant values of all items in dataset for
    # each class
    results = []
    # for loop iterates over number of elements in list
    for i in range(len(x_items)):
        # for loop iterates over number of inner items of each element
        for j in range(len(x_items[i])):
            temp = []  # to store all discriminant values of each item as a list
            # for loop iterates over number of classes we have in our dataset
            for k in range(len(x_items)):
                # appending values of discriminants for each class to 'temp' list
                temp.append(
                    x_items[i][j] * (means[k] / variance)
                    - (means[k] ** 2 / (2 * variance))
                    + log(probabilities[k])
                )
            # appending discriminant values of each item to 'results' list
            results.append(temp)

    return [result.index(max(result)) for result in results]


# Calculating Accuracy
def accuracy(actual_y: list, predicted_y: list) -> float:
    """
    Calculate the value of accuracy based-on predictions
    :param actual_y:a list containing initial Y values generated by 'y_generator'
        function
    :param predicted_y: a list containing predicted Y values generated by
        'predict_y_values' function
    :return: percentage of accuracy

    >>> actual_y = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1,
    ... 1, 1 ,1 ,1 ,1 ,1 ,1]
    >>> predicted_y = [0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0,
    ... 0, 0, 1, 1, 1, 0, 1, 1, 1]
    >>> accuracy(actual_y, predicted_y)
    50.0

    >>> actual_y = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1,
    ... 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
    >>> predicted_y = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1,
    ... 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
    >>> accuracy(actual_y, predicted_y)
    100.0
    """
    # iterate over one element of each list at a time (zip mode)
    # prediction is correct if actual Y value equals to predicted Y value
    correct = sum(1 for i, j in zip(actual_y, predicted_y) if i == j)
    # percentage of accuracy equals to number of correct predictions divided by number
    # of all data and multiplied by 100
    return (correct / len(actual_y)) * 100


# Main Function
def main():
    """ This function starts execution phase """
    while True:
        print(" Linear Discriminant Analysis ".center(50, "*"))
        print("*" * 50, "\n")
        print("First of all we should specify the number of classes that")
        print("we want to generate as training dataset")
        # Trying to get number of classes
        n_classes = 0
        while True:
            try:
                user_input = int(
                    input("Enter the number of classes (Data Groupings): ").strip()
                )
                if user_input > 0:
                    n_classes = user_input
                    break
                else:
                    print(
                        f"Your entered value is {user_input} , Number of classes "
                        f"should be positive!"
                    )
                    continue
            except ValueError:
                print("Your entered value is not numerical!")

        print("-" * 100)

        std_dev = 1.0  # Default value for standard deviation of dataset
        # Trying to get the value of standard deviation
        while True:
            try:
                user_sd = float(
                    input(
                        "Enter the value of standard deviation"
                        "(Default value is 1.0 for all classes): "
                    ).strip()
                    or "1.0"
                )
                if user_sd >= 0.0:
                    std_dev = user_sd
                    break
                else:
                    print(
                        f"Your entered value is {user_sd}, Standard deviation should "
                        f"not be negative!"
                    )
                    continue
            except ValueError:
                print("Your entered value is not numerical!")

        print("-" * 100)

        # Trying to get number of instances in classes and theirs means to generate
        # dataset
        counts = []  # An empty list to store instance counts of classes in dataset
        for i in range(n_classes):
            while True:
                try:
                    user_count = int(
                        input(f"Enter The number of instances for class_{i+1}: ")
                    )
                    if user_count > 0:
                        counts.append(user_count)
                        break
                    else:
                        print(
                            f"Your entered value is {user_count}, Number of "
                            "instances should be positive!"
                        )
                        continue
                except ValueError:
                    print("Your entered value is not numerical!")
        print("-" * 100)

        # An empty list to store values of user-entered means of classes
        user_means = []
        for a in range(n_classes):
            while True:
                try:
                    user_mean = float(
                        input(f"Enter the value of mean for class_{a+1}: ")
                    )
                    if isinstance(user_mean, float):
                        user_means.append(user_mean)
                        break
                    print(f"You entered an invalid value: {user_mean}")
                except ValueError:
                    print("Your entered value is not numerical!")
        print("-" * 100)

        print("Standard deviation: ", std_dev)
        # print out the number of instances in classes in separated line
        for i, count in enumerate(counts, 1):
            print(f"Number of instances in class_{i} is: {count}")
        print("-" * 100)

        # print out mean values of classes separated line
        for i, user_mean in enumerate(user_means, 1):
            print(f"Mean of class_{i} is: {user_mean}")
        print("-" * 100)

        # Generating training dataset drawn from gaussian distribution
        x = [
            gaussian_distribution(user_means[j], std_dev, counts[j])
            for j in range(n_classes)
        ]
        print("Generated Normal Distribution: \n", x)
        print("-" * 100)

        # Generating Ys to detecting corresponding classes
        y = y_generator(n_classes, counts)
        print("Generated Corresponding Ys: \n", y)
        print("-" * 100)

        # Calculating the value of actual mean for each class
        actual_means = [calculate_mean(counts[k], x[k]) for k in range(n_classes)]
        # for loop iterates over number of elements in 'actual_means' list and print
        # out them in separated line
        for i, actual_mean in enumerate(actual_means, 1):
            print(f"Actual(Real) mean of class_{i} is: {actual_mean}")
        print("-" * 100)

        # Calculating the value of probabilities for each class
        probabilities = [
            calculate_probabilities(counts[i], sum(counts)) for i in range(n_classes)
        ]

        # for loop iterates over number of elements in 'probabilities' list and print
        # out them in separated line
        for i, probability in enumerate(probabilities, 1):
            print(f"Probability of class_{i} is: {probability}")
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
        print(f"Accuracy: {accuracy(y, pre_indexes)}")
        print("-" * 100)
        print(" DONE ".center(100, "+"))

        if input("Press any key to restart or 'q' for quit: ").strip().lower() == "q":
            print("\n" + "GoodBye!".center(100, "-") + "\n")
            break
        system("cls" if name == "nt" else "clear")


if __name__ == "__main__":
    main()
