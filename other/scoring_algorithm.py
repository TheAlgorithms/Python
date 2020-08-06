"""
developed by: markmelnic
original repo: https://github.com/markmelnic/Scoring-Algorithm

Analyse data using a range based percentual proximity algorithm
and calculate the linear maximum likelihood estimation.
The basic principle is that all values supplied will be broken
down to a range from 0 to 1 and each column's score will be added
up to get the total score.

==========
Example for data of vehicles
price|mileage|registration_year
20k  |60k    |2012
22k  |50k    |2011
23k  |90k    |2015
16k  |210k   |2010

We want the vehicle with the lowest price,
lowest mileage but newest registration year.
Thus the weights for each column are as follows:
[0, 0, 1]

>>> procentual_proximity([[20, 60, 2012],[23, 90, 2015],[22, 50, 2011]], [0, 0, 1])
[[20, 60, 2012, 2.0], [23, 90, 2015, 1.0], [22, 50, 2011, 1.3333333333333335]]
"""


def procentual_proximity(source_data: list, weights: list) -> list:

    """
    weights - int list
    possible values - 0 / 1
    0 if lower values have higher weight in the data set
    1 if higher values have higher weight in the data set
    """

    # getting data
    data_lists = []
    for item in source_data:
        for i in range(len(item)):
            try:
                data_lists[i].append(float(item[i]))
            except IndexError:
                # generate corresponding number of lists
                data_lists.append([])
                data_lists[i].append(float(item[i]))

    score_lists = []
    # calculating each score
    for dlist, weight in zip(data_lists, weights):
        mind = min(dlist)
        maxd = max(dlist)

        score = []
        # for weight 0 score is 1 - actual score
        if weight == 0:
            for item in dlist:
                try:
                    score.append(1 - ((item - mind) / (maxd - mind)))
                except ZeroDivisionError:
                    score.append(1)

        elif weight == 1:
            for item in dlist:
                try:
                    score.append((item - mind) / (maxd - mind))
                except ZeroDivisionError:
                    score.append(0)

        # weight not 0 or 1
        else:
            raise ValueError("Invalid weight of %f provided" % (weight))

        score_lists.append(score)

    # initialize final scores
    final_scores = [0 for i in range(len(score_lists[0]))]

    # generate final scores
    for i, slist in enumerate(score_lists):
        for j, ele in enumerate(slist):
            final_scores[j] = final_scores[j] + ele

    # append scores to source data
    for i, ele in enumerate(final_scores):
        source_data[i].append(ele)

    return source_data
