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
"""


def get_data(source_data: list[list[float]]) -> list[list[float]]:
    """
    >>> get_data([[20, 60, 2012],[23, 90, 2015],[22, 50, 2011]])
    [[20.0, 23.0, 22.0], [60.0, 90.0, 50.0], [2012.0, 2015.0, 2011.0]]
    """
    data_lists: list[list[float]] = []
    for data in source_data:
        for i, el in enumerate(data):
            if len(data_lists) < i + 1:
                data_lists.append([])
            data_lists[i].append(float(el))
    return data_lists


def calculate_each_score(
    data_lists: list[list[float]], weights: list[int]
) -> list[list[float]]:
    """
    >>> calculate_each_score([[20, 23, 22], [60, 90, 50], [2012, 2015, 2011]],
    ...                      [0, 0, 1])
    [[1.0, 0.0, 0.33333333333333337], [0.75, 0.0, 1.0], [0.25, 1.0, 0.0]]
    """
    score_lists: list[list[float]] = []
    for dlist, weight in zip(data_lists, weights):
        mind = min(dlist)
        maxd = max(dlist)

        score: list[float] = []
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
            raise ValueError(f"Invalid weight of {weight:f} provided")

        score_lists.append(score)

    return score_lists


def generate_final_scores(score_lists: list[list[float]]) -> list[float]:
    """
    >>> generate_final_scores([[1.0, 0.0, 0.33333333333333337],
    ...                        [0.75, 0.0, 1.0],
    ...                        [0.25, 1.0, 0.0]])
    [2.0, 1.0, 1.3333333333333335]
    """
    # initialize final scores
    final_scores: list[float] = [0 for i in range(len(score_lists[0]))]

    for slist in score_lists:
        for j, ele in enumerate(slist):
            final_scores[j] = final_scores[j] + ele

    return final_scores


def procentual_proximity(
    source_data: list[list[float]], weights: list[int]
) -> list[list[float]]:
    """
    weights - int list
    possible values - 0 / 1
    0 if lower values have higher weight in the data set
    1 if higher values have higher weight in the data set

    >>> procentual_proximity([[20, 60, 2012],[23, 90, 2015],[22, 50, 2011]], [0, 0, 1])
    [[20, 60, 2012, 2.0], [23, 90, 2015, 1.0], [22, 50, 2011, 1.3333333333333335]]
    """

    data_lists = get_data(source_data)
    score_lists = calculate_each_score(data_lists, weights)
    final_scores = generate_final_scores(score_lists)

    # append scores to source data
    for i, ele in enumerate(final_scores):
        source_data[i].append(ele)

    return source_data
