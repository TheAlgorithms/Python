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

from collections import defaultdict
from itertools import combinations


def load_data() -> list[list[str]]:
    """
    Returns a sample transaction dataset.

    >>> load_data()
    [['milk'], ['milk', 'butter'], ['milk', 'bread'], ['milk', 'bread', 'chips']]
    """
    return [["milk"], ["milk", "butter"], ["milk", "bread"], ["milk", "bread", "chips"]]


# ---------- Helpers ----------


def get_support(itemset, transactions):
    """Compute support count of an itemset efficiently."""
    return sum(1 for t in transactions if itemset.issubset(t))


def generate_candidates(prev_frequent, k):
    """
    Generate candidate itemsets of size k from frequent itemsets of size k-1.
    """
    prev_list = list(prev_frequent)
    candidates = set()

    for i in range(len(prev_list)):
        for j in range(i + 1, len(prev_list)):
            union = prev_list[i] | prev_list[j]
            if len(union) == k:
                candidates.add(union)

    return candidates


def has_infrequent_subset(candidate, prev_frequent):
    """
    Apriori pruning: all (k-1)-subsets must be frequent.
    """
    for subset in combinations(candidate, len(candidate) - 1):
        if frozenset(subset) not in prev_frequent:
            return True
    return False


# ---------- Main Apriori ----------


def apriori(data: list[list[str]], min_support: int):
    transactions = [set(t) for t in data]

    # 1. initial 1-itemsets
    item_counts = defaultdict(int)
    for t in transactions:
        for item in t:
            item_counts[frozenset([item])] += 1

    frequent = {
        itemset for itemset, count in item_counts.items() if count >= min_support
    }

    all_frequents = [
        (next(iter(i)), c) for i, c in item_counts.items() if c >= min_support
    ]

    k = 2

    while frequent:
        # 2. generate candidates
        candidates = generate_candidates(frequent, k)

        # 3. prune
        candidates = {c for c in candidates if not has_infrequent_subset(c, frequent)}

        # 4. count support
        candidate_counts = defaultdict(int)
        for t in transactions:
            for c in candidates:
                if c.issubset(t):
                    candidate_counts[c] += 1

        # 5. filter frequent
        frequent = {c for c, count in candidate_counts.items() if count >= min_support}

        all_frequents.extend(
            (sorted(c), count)
            for c, count in candidate_counts.items()
            if count >= min_support
        )

        k += 1

    return all_frequents


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
