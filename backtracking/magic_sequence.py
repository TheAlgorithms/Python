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


def backtrack(
    n: int, sequence: list[any], res: list[int] = [], depth: int = 0
) -> list[int]:
    """
    this function return a list of solition

    Args:
        n (int): number of element in the sequence
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
    for i in range(0, n):
        # check filter for pass to the next step
        if somme_elem_lower_to_len(sequence):
            sequence[depth] = i
            backtrack(n, copy.deepcopy(sequence), res, depth + 1)
        else:
            break
    return res


def check_magic_sequence(sequence: list[int]) -> bool:
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

    try:
        nb_element = int(sys.argv[1])
    except:
        print(
            "no first arg given so number of element is initialized to 4 because it's the first one to give a answer"
        )
        nb_element = 4
    res = backtrack(nb_element, [None for x in range(nb_element)])
    print(res)
