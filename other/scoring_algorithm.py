"""
developed by: markmelnic
original repo: https://github.com/markmelnic/Scoring-Algorithm
        pypi: https://pypi.org/project/scalg/

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

>>> score([[20, 60, 2012],[23, 90, 2015],[22, 50, 2011]], [0, 0, 1])
[[20, 60, 2012, 2.0], [23, 90, 2015, 1.0], [22, 50, 2011, 1.3333333333333335]]
>>> score([[20, 60, 2012],[23, 90, 2015],[22, 50, 2011]], [0, 0, 1], 'scores')
[2.0, 1.0, 1.3333333333333335]
>>> score_columns([[20, 60, 2012],[23, 90, 2015],[22, 50, 2011]], [0, 2], [0, 0, 1])
[[20, 2012, 1.25], [23, 2015, 1.0], [22, 2011, 0.33333333333333337]]
"""


def score(source_data: list, weights: list, *args) -> list:
    """Analyse and score a dataset using a range based percentualF proximity
    algorithm and calculate the linear maximum likelihood estimation.
    Args:
        source_data (list): Data set to process.
        weights (list): Weights corresponding to each column from the data set.
            0 if lower values have higher weight in the data set,
            1 if higher values have higher weight in the data set
    Optional args:
        "score_lists" (str): Returns a list with lists of each column scores.
        "scores" (str): Returns only the final scores.
    Raises:
        ValueError: Weights can only be either 0 or 1 (int)
    Returns:
        list: Source data with the score of the set appended at as the last element.
    """

    # getting data
    data_lists = []
    for item in source_data:
        for i, val in enumerate(item):
            try:
                data_lists[i].append(float(val))
            except IndexError:
                data_lists.append([])
                data_lists[i].append(float(val))

    # calculating price score
    score_lists = []
    for dlist, weight in zip(data_lists, weights):
        mind = min(dlist)
        maxd = max(dlist)

        score = []
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

        else:
            raise ValueError("Invalid weight of %f provided" % (weight))

        score_lists.append(score)

    # return score lists
    if "score_lists" in args:
        return score_lists

    # initialize final scores
    final_scores = [0 for i in range(len(score_lists[0]))]

    # generate final scores
    for i, slist in enumerate(score_lists):
        for j, ele in enumerate(slist):
            final_scores[j] = final_scores[j] + ele

    # return only scores
    if "scores" in args:
        return final_scores

    # append scores to source data
    for i, ele in enumerate(final_scores):
        source_data[i].append(ele)

    return source_data


def score_columns(source_data: list, columns: list, weights: list, *args) -> list:
    """Analyse specific columns of the source_data dataset.
    Args:
        source_data (list): Data set to process.
        columns (list): Indexes of the source_data columns to be scored.
        weights (list): Weights corresponding to each column from the data set.
            0 if lower values have higher weight in the data set,
            1 if higher values have higher weight in the data set
    Optional args:
        "score_lists" (str): Returns a list with lists of each column scores.
        "scores" (str): Returns only the final scores.
    Raises:
        ValueError: Weights can only be either 0 or 1 (int)
    Returns:
        list: Source data with the score of the set appended at as the last element.
    """

    temp_data = []
    for item in source_data:
        temp_data.append([item[c] for c in columns])

    if len(weights) > len(columns):
        weights = [weights[item] for item in columns]

    if "scores" in args:
        return score(temp_data, weights, "scores")
    elif "score_lists" in args:
        return score(temp_data, weights, "score_lists")
    else:
        return score(temp_data, weights)
