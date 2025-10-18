"""
Apriori Algorithm — Association Rule Mining Technique

The Apriori algorithm is a **classic association rule learning method**, also known as
**Market Basket Analysis**, used to discover interesting relationships or associations
among a set of items in a transactional database.

For example:
"If a customer buys item A and item B, they are likely to buy item C."
This suggests a relationship between items A, B, and C — indicating that customers
who purchased A and B are more likely to also purchase C.

📘 WIKI: https://en.wikipedia.org/wiki/Apriori_algorithm  
📊 Example Notebook: https://www.kaggle.com/code/earthian/apriori-association-rules-mining
"""

from itertools import combinations


def load_data() -> list[list[str]]:
    """
    Returns a sample transaction dataset.

    >>> load_data()
    [['milk'], ['milk', 'butter'], ['milk', 'bread'], ['milk', 'bread', 'chips']]
    """
    return [["milk"], ["milk", "butter"], ["milk", "bread"], ["milk", "bread", "chips"]]


def get_item_support(data: list[list[str]], candidates: list[list[str]]) -> dict[tuple[str], int]:
    """
    Compute the support count for each candidate itemset.

    Args:
        data: A list of transactions (each transaction is a list of items)
        candidates: List of candidate itemsets

    Returns:
        Dictionary mapping itemsets to their support count.
    """
    support_count = {tuple(sorted(candidate)): 0 for candidate in candidates}
    for transaction in data:
        for candidate in candidates:
            if all(item in transaction for item in candidate):
                support_count[tuple(sorted(candidate))] += 1
    return support_count


def prune_candidates(prev_freq_itemsets: list[list[str]], k: int) -> list[list[str]]:
    """
    Generate and prune candidate itemsets of size k from previous frequent itemsets.

    Args:
        prev_freq_itemsets: Frequent itemsets of size (k-1)
        k: Desired size of next candidate itemsets

    Returns:
        List of pruned candidate itemsets.
    """
    candidates = []
    for i in range(len(prev_freq_itemsets)):
        for j in range(i + 1, len(prev_freq_itemsets)):
            l1, l2 = sorted(prev_freq_itemsets[i]), sorted(prev_freq_itemsets[j])
            if l1[:-1] == l2[:-1]:
                candidate = sorted(list(set(l1) | set(l2)))
                # Prune candidates whose subsets are not frequent
                subsets = list(combinations(candidate, k - 1))
                if all(list(subset) in prev_freq_itemsets for subset in subsets):
                    candidates.append(candidate)
    return candidates


def apriori(data: list[list[str]], min_support: int) -> list[tuple[list[str], int]]:
    """
    Apriori algorithm for finding frequent itemsets.

    Args:
        data: A list of transactions, where each transaction is a list of items.
        min_support: The minimum support threshold for frequent itemsets.

    Returns:
        A list of frequent itemsets along with their support counts.

    Example:
    >>> data = [['A', 'B', 'C'], ['A', 'B'], ['A', 'C'], ['A', 'D'], ['B', 'C']]
    >>> apriori(data, 2)
    [(['A'], 4), (['B'], 3), (['C'], 3), (['A', 'B'], 2), (['A', 'C'], 2), (['B', 'C'], 2)]
    """
    # Step 1: Find unique items
    single_items = sorted({item for transaction in data for item in transaction})
    current_candidates = [[item] for item in single_items]
    frequent_itemsets = []

    k = 1
    while current_candidates:
        support_count = get_item_support(data, current_candidates)
        # Keep itemsets meeting minimum support
        current_freq_itemsets = [
            list(itemset) for itemset, count in support_count.items() if count >= min_support
        ]
        frequent_itemsets.extend(
            [(list(itemset), count) for itemset, count in support_count.items() if count >= min_support]
        )

        # Generate next level of candidates
        k += 1
        current_candidates = prune_candidates(current_freq_itemsets, k)

    return frequent_itemsets


if __name__ == "__main__":
    """
    Run Apriori algorithm on the sample dataset with user-defined minimum support.
    """
    import doctest
    doctest.testmod()

    transactions = load_data()
    min_support = 2
    results = apriori(transactions, min_support)

    print("Frequent Itemsets and Support Counts:\n")
    for itemset, support in results:
        print(f"{itemset}: {support}")
