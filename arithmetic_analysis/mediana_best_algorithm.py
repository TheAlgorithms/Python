import random
def pick_pivot(l):
    """
    Pick a good pivot within l, a list of numbers
    This algorithm runs in O(n) time.
    """
    assert len(l) > 0

    # If there are < 5 items, just return the median
    if len(l) < 5:
        # In this case, we fall back on the first median function we wrote.
        # Since we only run this on a list of 5 or fewer items, it doesn't
        # depend on the length of the input and can be considered constant
        # time.
        return nlogn_median(l)

    # First, we'll split `l` into groups of 5 items. O(n)
    chunks = chunked(l, 5)

    # For simplicity, we can drop any chunks that aren't full. O(n)
    full_chunks = [chunk for chunk in chunks if len(chunk) == 5]

    # Next, we sort each chunk. Each group is a fixed length, so each sort
    # takes constant time. Since we have n/5 chunks, this operation
    # is also O(n)
    sorted_groups = [sorted(chunk) for chunk in full_chunks]

    # The median of each chunk is at index 2
    medians = [chunk[2] for chunk in sorted_groups]

    # It's a bit circular, but I'm about to prove that finding
    # the median of a list can be done in provably O(n).
    # Finding the median of a list of length n/5 is a subproblem of size n/5
    # and this recursive call will be accounted for in our analysis.
    # We pass pick_pivot, our current function, as the pivot builder to
    # quickselect. O(n)
    median_of_medians = quickselect_median(medians, pick_pivot)
    return median_of_medians


def chunked(l, chunk_size):
    """Split list `l` it to chunks of `chunk_size` elements."""
    return [l[i:i + chunk_size] for i in range(0, len(l), chunk_size)]


def nlogn_median(l):
    l = sorted(l)
    if len(l) % 2 == 1:
        return l[int((len(l) / 2))]
    else:
        return 0.5 * (l[len(l) / 2 - 1] + l[len(l) / 2])


def quickselect_median(l, pivot_fn=random.choice):
    if len(l) % 2 == 1:
        return quickselect(l, len(l) / 2, pivot_fn)
    else:
        return 0.5 * (quickselect(l, len(l) / 2 - 1, pivot_fn) +
                      quickselect(l, len(l) / 2, pivot_fn))


def quickselect(l, k, pivot_fn):
    """
    Select the kth element in l (0 based)
    :param l: List of numerics
    :param k: Index
    :param pivot_fn: Function to choose a pivot, defaults to random.choice
    :return: The kth element of l
    """
    if len(l) == 1:
        assert k == 0
        return l[0]

    pivot = pivot_fn(l)

    lows = [el for el in l if el < pivot]
    highs = [el for el in l if el > pivot]
    pivots = [el for el in l if el == pivot]

    if k < len(lows):
        return quickselect(lows, k, pivot_fn)
    elif k < len(lows) + len(pivots):
        # We got lucky and guessed the median
        return pivots[0]
    else:
        return quickselect(highs, k - len(lows) - len(pivots), pivot_fn)


l = [9,1,0,2,3,4,6,8,7,10,5]

print(pick_pivot(l))

"""
Considere a lista abaixo. Gostaríamos de encontrar a mediana.
l = [9,1,0,2,3,4,6,8,7,10,5]
len (l) == 11, então estamos procurando pelo 6º menor elemento
Primeiro, devemos escolher um pivô. Selecionamos aleatoriamente o índice 3.
O valor neste índice é 2.

Particionamento com base no pivô:
[1,0,2], [9,3,4,6,8,7,10,5]
Queremos o 6º elemento. 6-len (esquerda) = 3, então queremos
o terceiro menor elemento na matriz certa

Agora estamos procurando o terceiro menor elemento na matriz abaixo:
[9,3,4,6,8,7,10,5]
Escolhemos um índice aleatoriamente para ser nosso pivô.
Escolhemos o índice 3, o valor em que, l [3] = 6

Particionamento com base no pivô:
[3,4,5,6] [9,7,10]
Queremos o terceiro menor elemento, então sabemos que é o
3º menor elemento na matriz esquerda

Agora estamos procurando o terceiro menor na matriz abaixo:
[3,4,5,6]
Escolhemos um índice aleatoriamente para ser nosso pivô.
Escolhemos o índice 1, o valor em que, l [1] = 4
Particionamento com base no pivô:
[3,4] [5,6]
Estamos procurando o item no índice 3, então sabemos que é
o menor na matriz certa.

Agora estamos procurando o menor elemento na matriz abaixo:
[5,6]

Neste ponto, podemos ter um caso base que escolhe a maior
ou item menor com base no índice.
Estamos procurando o menor item, que é 5.
retorno 5

Esse algoritmo roda em O(n)
http://people.csail.mit.edu/rivest/pubs/BFPRT73.pdf
"""