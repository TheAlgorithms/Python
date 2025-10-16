"""
Apriori Algorithm is an Association rule mining technique, also known as market basket
analysis, aims to discover interesting relationships or associations among a set of
items in a transactional or relational database.

For example, Apriori Algorithm states: "If a customer buys item A and item B, then they
are likely to buy item C."  This rule suggests a relationship between items A, B, and C,
indicating that customers who purchased A and B are more likely to also purchase item C.

WIKI: https://en.wikipedia.org/wiki/Apriori_algorithm
Examples: https://www.kaggle.com/code/earthian/apriori-association-rules-mining
"""

from collections import defaultdict
from itertools import combinations


def load_data() -> list[list[str]]:
    """
    Returns a sample transaction dataset.

    >>> load_data()
    [['milk'], ['milk', 'butter'], ['milk', 'bread'], ['milk', 'bread', 'chips']]
    """
    return [["milk"], ["milk", "butter"], ["milk", "bread"], ["milk", "bread", "chips"]]


def prune(
    frequent_itemsets: list[list[str]], candidates: list[list[str]]
) -> list[list[str]]:
    """
    Prunes candidate itemsets by ensuring all (k-1)-subsets exist in
    previous frequent itemsets.

    >>> frequent_itemsets = [['X', 'Y'], ['X', 'Z'], ['Y', 'Z']]
    >>> candidates = [['X', 'Y', 'Z'], ['X', 'Y', 'W']]
    >>> prune(frequent_itemsets, candidates)
    [['X', 'Y', 'Z']]
    """

    previous_frequents = {frozenset(itemset) for itemset in frequent_itemsets}

    pruned_candidates = []
    for candidate in candidates:
        all_subsets_frequent = all(
            frozenset(subset) in previous_frequents
            for subset in combinations(candidate, len(candidate) - 1)
        )
        if all_subsets_frequent:
            pruned_candidates.append(candidate)

    return pruned_candidates


def apriori(data: list[list[str]], min_support: int) -> list[tuple[list[str], int]]:
    """
    Returns a list of frequent itemsets and their support counts.

    >>> data = [['A', 'B'], ['A', 'C'], ['B', 'C']]
    >>> apriori(data, 2)
    [(['A'], 2), (['B'], 2), (['C'], 2)]

    >>> data = [['1', '2', '3'], ['1', '2'], ['1', '3'], ['1', '4'], ['2', '3']]
    >>> apriori(data, 3)
    [(['1'], 4), (['2'], 3), (['3'], 3)]
    """

    item_counts: defaultdict[str, int] = defaultdict(int)
    for transaction in data:
        for item in transaction:
            item_counts[item] += 1

    current_frequents = [
        [item] for item, count in item_counts.items() if count >= min_support
    ]
    frequent_itemsets = [
        ([item], count) for item, count in item_counts.items() if count >= min_support
    ]

    k = 2
    while current_frequents:
        candidates = [
            sorted(set(i) | set(j))
            for i in current_frequents
            for j in current_frequents
            if len(set(i).union(j)) == k
        ]

        candidates = [list(c) for c in {frozenset(c) for c in candidates}]

        candidates = prune(current_frequents, candidates)

        candidate_counts: defaultdict[tuple[str, ...], int] = defaultdict(int)
        for transaction in data:
            t_set = set(transaction)
            for candidate in candidates:
                if set(candidate).issubset(t_set):
                    candidate_counts[tuple(sorted(candidate))] += 1

        current_frequents = [
            list(key) for key, count in candidate_counts.items() if count >= min_support
        ]
        frequent_itemsets.extend(
            [
                (list(key), count)
                for key, count in candidate_counts.items()
                if count >= min_support
            ]
        )

        k += 1

    return sorted(frequent_itemsets, key=lambda x: (len(x[0]), x[0]))


if __name__ == "__main__":
    """
    Apriori algorithm for finding frequent itemsets.

    This script loads sample transaction data and runs the Apriori algorithm
    with a user-defined minimum support threshold.

    The result is a list of frequent itemsets along with their support counts.
    """
    import doctest

    doctest.testmod()

    transactions = load_data()
    min_support_threshold = 2

    frequent_itemsets = apriori(transactions, min_support=min_support_threshold)

    print("Frequent Itemsets:")
    for itemset, support in frequent_itemsets:
        print(f"{itemset}: {support}")
