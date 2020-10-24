def distribute_candy(children_ratings: list) -> int:
    """
    There are N children standing in a line. Each child is assigned a rating value.
    You are giving candies to these children subjected to the following requirements:
        1. Each child must have at least one candy.
        2. Children with a higher rating get more candies than their neighbors.
    What is the minimum candies you must give?
    Input Format:
        A list of Numbers representing children ratings.
    Output Format:
        Minimum number of candies to be given.

    >>> distribute_candy([1, 2])
    3
    >>> distribute_candy([1, 5, 2, 1])
    7
    >>> distribute_candy([1, 3, 2, 1])
    7
    """

    candy = [1] * len(children_ratings)

    for idx in range(1, len(children_ratings)):
        if children_ratings[idx] > children_ratings[idx - 1]:
            candy[idx] = candy[idx - 1] + 1

    for idx in range(len(children_ratings) - 2, -1, -1):
        if children_ratings[idx] > children_ratings[idx + 1]:
            candy[idx] = max(candy[idx + 1] + 1, candy[idx])

    return sum(candy)


if __name__ == "__main__":
    c1 = distribute_candy([1, 2])
    c2 = distribute_candy([1, 5, 2, 1])
    c3 = distribute_candy([1, 3, 2, 1])
    print(str([1, 2]), "=>", c1)
    print(str([1, 5, 2, 1]), "=>", c2)
    print(str([1, 3, 2, 1]), "=>", c3)
