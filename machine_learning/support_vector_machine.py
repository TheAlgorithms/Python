import numpy as np

Vector = np.ndarray  # using numpy arrays to represent data


def margin_hard(data: list[Vector], cl: list[int]) -> tuple[Vector, float]:
    """
    Assuming the data is linearly separable
    Result will be falsy otherwise

    Args:
        data (list[Vector]): list of observations
        cl (list[int]): classification of each observation (in {1, -1})
    """

    pass
