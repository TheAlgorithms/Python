"""
An AND Gate is a logic gate in boolean algebra which results to 1 (True) if all the
inputs are 1 (True), and 0 (False) otherwise.

Following is the truth table of a Two Input AND Gate:
    ------------------------------
    | Input 1 | Input 2 | Output |
    ------------------------------
    |    0    |    0    |    0   |
    |    0    |    1    |    0   |
    |    1    |    0    |    0   |
    |    1    |    1    |    1   |
    ------------------------------

Refer - https://www.geeksforgeeks.org/logic-gates/
"""


def and_gate(input_1: int, input_2: int) -> int:
    """
    Calculate AND of the input values

    >>> and_gate(0, 0)
    0
    >>> and_gate(0, 1)
    0
    >>> and_gate(1, 0)
    0
    >>> and_gate(1, 1)
    1
    """
    if input_1 not in (0, 1) or input_2 not in (0, 1):
        raise ValueError("Inputs must be 0 or 1")
    return int(input_1 and input_2)


def n_input_and_gate(inputs: list[int]) -> int:
    """
    Calculate AND of a list of input values

    >>> n_input_and_gate([1, 0, 1, 1, 0])
    0
    >>> n_input_and_gate([1, 1, 1, 1, 1])
    1
    """
    if not inputs:
        raise ValueError("Input list cannot be empty")
    if any(x not in (0, 1) for x in inputs):
        raise ValueError("All inputs must be 0 or 1")
    return int(all(inputs))



if __name__ == "__main__":
    import doctest

    doctest.testmod()
    print("\n--- N-Input AND Gate Simulator ---")
    try:
        n = int(input("Enter the number of inputs: "))
        inputs = []
        for i in range(n):
            val = int(input(f"Enter input {i + 1} (0 or 1): "))
            if val not in (0, 1):
                raise ValueError("Inputs must be 0 or 1")
            inputs.append(val)

        result = n_input_and_gate(inputs)
        print(f"Inputs: {inputs}")
        print(f"AND Gate Output: {result}")
    except ValueError as e:
        print("Error:", e)
