# This program implements the AND and OR gates using the Adaline algorithm.

def weight_change_or(weight: list[float], threshold: float, learning_rate: float) -> list[float]:
    """
    This function updates the weights for the OR gate using the Adaline algorithm.

    Args:
        weight (list[float]): The weights for the Adaline algorithm.
        threshold (float): The threshold value for the Adaline algorithm.
        learning_rate (float): The learning rate for the Adaline algorithm.

    Returns:
        list[float]: The updated weights for the OR gate.
    >>> weight_change_or([1.2, 0.6], 1, 0.5)
    [1.2, 1.1]
    """
    output = weight[0]*0 + weight[1]*0
    if output <= threshold:
        output_left = weight[0]*0 + weight[1]*1
        if output_left >= threshold:
            output_left_down = weight[0]*1 + weight[1]*0
            if output_left_down >= threshold:
                output_all = weight[0]*1 + weight[1]*1
                if output_all >= threshold:
                    return weight
                else:
                    weight[0] = weight[0] + learning_rate*1*1
                    weight[1] = weight[1] + learning_rate*1*1
                    return weight_change_or(weight, threshold, learning_rate)
            else:
                weight[0] = weight[0] + learning_rate*1*1
                weight[1] = weight[1] + learning_rate*1*0
                return weight_change_or(weight, threshold, learning_rate)
        else:
            weight[0] = weight[0] + learning_rate*1*0
            weight[1] = weight[1] + learning_rate*1*1
            return weight_change_or(weight, threshold, learning_rate)
    else:
        threshold += learning_rate
        return weight_change_or(weight, threshold, learning_rate)


def weight_change_and(weight: list[float], threshold: float, learning_rate: float) -> list[float]:
    """
    This function updates the weights for the AND gate using the Adaline algorithm.

    Args:
        weight (list[float]): The weights for the Adaline algorithm.
        threshold (float): The threshold value for the Adaline algorithm.
        learning_rate (float): The learning rate for the Adaline algorithm.

    Returns:
        list[float]: The updated weights for the AND gate.
    >>> weight_change_and([1.2, 0.6], 1, 0.5)
    [0.7, 0.1]
    """
    output = weight[0]*0 + weight[1]*0
    if output <= threshold:
        output_left = weight[0]*0 + weight[1]*1
        if output_left <= threshold:
            output_left_down = weight[0]*1 + weight[1]*0
            if output_left_down <= threshold:
                output_all = weight[0]*1 + weight[1]*1
                if output_all >= threshold:
                    return weight
                else:
                    weight[0] = weight[0] + (learning_rate*1*1)
                    weight[1] = weight[1] + (learning_rate*1*1)
                    return weight_change_and(weight, threshold, learning_rate)
            else:
                weight[0] = weight[0] - (learning_rate*1*1)
                weight[1] = weight[1] - (learning_rate*1*0)
                return weight_change_and(weight, threshold, learning_rate)
        else:
            weight[0] = weight[0] - (learning_rate*1*0)
            weight[1] = weight[1] - (learning_rate*1*1)
            return weight_change_and(weight, threshold, learning_rate)
    else:
        threshold += learning_rate
        return weight_change_and(weight, threshold, learning_rate)


def and_gate(weight: list[float], input_a: int, input_b: int, threshold: float, learning_rate: float) -> int:
    """
    This function implements the AND gate using the Adaline algorithm.

    Args:
        weight (list[float]): The weights for the Adaline algorithm.
        input_a (int): The first input value.
        input_b (int): The second input value.
        threshold (float): The threshold value for the Adaline algorithm.
        learning_rate (float): The learning rate for the Adaline algorithm.

    Returns:
        int: The output of the AND gate.
    >>> and_gate([1.2, 0.6], 0, 0, 1, 0.5)
    0
    >>> and_gate([1.2, 0.6], 0, 1, 1, 0.5)
    0
    >>> and_gate([1.2, 0.6], 1, 0, 1, 0.5)
    0
    >>> and_gate([1.2, 0.6], 1, 1, 1, 0.5)
    1
    """
    weight = weight_change_and(weight, threshold, learning_rate)
    output = weight[0]*input_a + weight[1]*input_b
    if output >= threshold:
        return 1
    else:
        return 0


def or_gate(weight: list[float], input_a: int, input_b: int, threshold: float, learning_rate: float) -> int:
    """
    This function implements the OR gate using the Adaline algorithm.

    Args:
        weight (list[float]): The weights for the Adaline algorithm.
        input_a (int): The first input value.
        input_b (int): The second input value.
        threshold (float): The threshold value for the Adaline algorithm.
        learning_rate (float): The learning rate for the Adaline algorithm.

    Returns:
        int: The output of the OR gate.
    >>> or_gate([1.2, 0.6], 0, 0, 1, 0.5)
    0
    >>> or_gate([1.2, 0.6], 0, 1, 1, 0.5)
    1
    >>> or_gate([1.2, 0.6], 1, 0, 1, 0.5)
    1
    >>> or_gate([1.2, 0.6], 1, 1, 1, 0.5)
    1
    """
    weight = weight_change_or(weight, threshold, learning_rate)
    output = weight[0]*input_a + weight[1]*input_b
    if output >= threshold:
        return 1
    else:
        return 0

weight = [1.2, 0.6]
weight2 = [1.2, 0.6]
threshold = 1
learning_rate = 0.5
input_a, input_b = input("Input the value of A and B:").split()
input_a = int(input_a)
input_b = int(input_b)
print("\nThe output of OR is:", or_gate(weight, input_a, input_b, threshold, learning_rate))
print("\nThe output of AND is:", and_gate(weight2, input_a, input_b, threshold, learning_rate))
