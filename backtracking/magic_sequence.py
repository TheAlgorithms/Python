#    @brief [Magic sequence](https://www.csplib.org/Problems/prob019/)
#    implementation

#    @details Solve the magic sequence problem with backtracking

#    "A magic sequence of length $n$ is a sequence of integers $x_0
#    \ldots x_{n-1}$ between $0$ and $n-1$, such that for all $i$
#    in $0$ to $n-1$, the number $i$ occurs exactly $x_i$ times in
#    the sequence. For instance, $6,2,1,0,0,0,1,0,0,0$ is a magic
#    sequence since $0$ occurs $6$ times in it, $1$ occurs twice, etc."
#    Quote taken from the [CSPLib](https://www.csplib.org/Problems/prob019/)
#    website


import sys
import copy
import doctest

def backtrack(
    nb_element: int, sequence: list[any], res: list[int] = [], depth: int = 0
) -> list[int]:
    """
    >>> backtrack(4, [None for x in range(4)])
    [[1, 2, 1, 0], [2, 0, 2, 0]]
    >>> backtrack(7, [None for x in range(7)])
    [[1, 2, 1, 0], [2, 0, 2, 0], [3, 2, 1, 1, 0, 0, 0]]
    >>> backtrack(10, [None for x in range(10)])
    [[1, 2, 1, 0], [2, 0, 2, 0], [3, 2, 1, 1, 0, 0, 0], [6, 2, 1, 0, 0, 0, 1, 0, 0, 0]]

    """
    """
    this function return a list of solition

    Args:
        nb_element (int): number of element in the sequence
        sequence (list[any]): use for generete the solotion
        res (list[int], optional): empty list for recover the solution. Defaults to [].
        depth (int, optional): position in the three. Defaults to 0.

    Returns:
        list[int]: list of solution
    """

    # check if i not exceed the length of the sequence before check the magic sequence
    if depth == len(sequence):
        if check_magic_sequence(sequence):
            res.append(copy.deepcopy(sequence))
        return 0
    for i in range(0, nb_element):
        # check filter for pass to the next step
        if somme_elem_lower_to_len(sequence):
            sequence[depth] = i
            backtrack(nb_element, copy.deepcopy(sequence), res, depth + 1)
        else:
            break
    return res


def check_magic_sequence(sequence: list[int]) -> bool:
    """
    >>> check_magic_sequence([2,2,2])
    False
    >>> check_magic_sequence([3, 2, 1, 1, 0, 0, 0])
    True
    >>> check_magic_sequence([0])
    False
    >>> check_magic_sequence([1,2,1,0])
    True
    """
    """
    the function check if the sequence is a magic

    Args:
        sequence (list[int]): list of integer

    Returns:
        bool: return true if the sequence is magic else return false
    """
    for i in range(len(sequence)):
        count = 0
        for j in range(len(sequence)):
            # check if the position i is equal to the number at the position j
            if i == sequence[j]:
                count += 1
        # check if the number of i is different to the number at the position i
        if count != sequence[i]:
            return False
    if somme_elem_lower_to_len(sequence):
        return True
    return False


def somme_elem_lower_to_len(sequence: list[any]) -> bool:
    """
    >>> somme_elem_lower_to_len([2,2,2])
    False
    >>> somme_elem_lower_to_len([1,0,0])
    True
    >>> somme_elem_lower_to_len([None])
    True
    """
    """
    the function check if the summe of the elements of the sequence
    are not greater than the length of the sequence

    Args:
        sequence (list[any]): list of integer or NoneType

    Returns:
        bool: return true if the result is lower than the length of the sequence
    """


    res = 0
    for i in sequence:
        if i != None:
            res = res + i
    if res <= len(sequence):
        return True
    else:
        return False


if __name__ == "__main__":
    doctest.testmod()
    try:
        nb_element = int(sys.argv[1])
    except:
        print(
            "no first arg given so number of element is initialized to 4 because it's the first one to give a answer"
        )
        nb_element = 4
    res = backtrack(nb_element, [None for x in range(nb_element)])
    print(res)
