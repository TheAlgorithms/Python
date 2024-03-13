"""
Apriori Algorithm is a Association rule mining technique, also known as market basket
analysis, aims to discover interesting relationships or associations among a set of
items in a transactional or relational database.

For example, Apriori Algorithm states: "If a customer buys item A and item B, then they
are likely to buy item C."  This rule suggests a relationship between items A, B, and C,
indicating that customers who purchased A and B are more likely to also purchase item C.

WIKI: https://en.wikipedia.org/wiki/Apriori_algorithm
Examples: https://www.kaggle.com/code/earthian/apriori-association-rules-mining
"""

from itertools import combinations


def load_data() -> list[list[str]]:
    """
    Returns a sample transaction dataset.

    >>> load_data()
    [['milk'], ['milk', 'butter'], ['milk', 'bread'], ['milk', 'bread', 'chips']]
    """
    return [["milk"], ["milk", "butter"], ["milk", "bread"], ["milk", "bread", "chips"]]


def prune(itemset: list, candidates: list, length: int) -> list:
    """
    Prune candidate itemsets that are not frequent.
    The goal of pruning is to filter out candidate itemsets that are not frequent.  This
    is done by checking if all the (k-1) subsets of a candidate itemset are present in
    the frequent itemsets of the previous iteration (valid subsequences of the frequent
    itemsets from the previous iteration).

    Prunes candidate itemsets that are not frequent.

    >>> itemset = ['X', 'Y', 'Z']
    >>> candidates = [['X', 'Y'], ['X', 'Z'], ['Y', 'Z']]
    >>> prune(itemset, candidates, 2)
    [['X', 'Y'], ['X', 'Z'], ['Y', 'Z']]

    >>> itemset = ['1', '2', '3', '4']
    >>> candidates = ['1', '2', '4']
    >>> prune(itemset, candidates, 3)
    []
    """
    pruned = []
    for candidate in candidates:
        is_subsequence = True
        for item in candidate:
            if item not in itemset or itemset.count(item) < length - 1:
                is_subsequence = False
                break
        if is_subsequence:
            pruned.append(candidate)
    return pruned


def apriori(data: list[list[str]], min_support: int) -> list[tuple[list[str], int]]:
    """
    Returns a list of frequent itemsets and their support counts.

    >>> data = [['A', 'B', 'C'], ['A', 'B'], ['A', 'C'], ['A', 'D'], ['B', 'C']]
    >>> apriori(data, 2)
    [(['A', 'B'], 1), (['A', 'C'], 2), (['B', 'C'], 2)]

    >>> data = [['1', '2', '3'], ['1', '2'], ['1', '3'], ['1', '4'], ['2', '3']]
    >>> apriori(data, 3)
    []
    """
    itemset = [list(transaction) for transaction in data]
    frequent_itemsets = []
    length = 1

    while itemset:
        # Count itemset support
        counts = [0] * len(itemset)
        for transaction in data:
            for j, candidate in enumerate(itemset):
                if all(item in transaction for item in candidate):
                    counts[j] += 1

        # Prune infrequent itemsets
        itemset = [item for i, item in enumerate(itemset) if counts[i] >= min_support]

        # Append frequent itemsets (as a list to maintain order)
        for i, item in enumerate(itemset):
            frequent_itemsets.append((sorted(item), counts[i]))

        length += 1
        itemset = prune(itemset, list(combinations(itemset, length)), length)

    return frequent_itemsets


if __name__ == "__main__":
    """
    Apriori algorithm for finding frequent itemsets.

    Args:
        data: A list of transactions, where each transaction is a list of items.
        min_support: The minimum support threshold for frequent itemsets.

    Returns:
        A list of frequent itemsets along with their support counts.
    """
    import doctest

    doctest.testmod()

    # user-defined threshold or minimum support level
    frequent_itemsets = apriori(data=load_data(), min_support=2)
    print("\n".join(f"{itemset}: {support}" for itemset, support in frequent_itemsets))
