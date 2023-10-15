"""
Apriori Algorithm is a Association rule mining technique, also known as market basket analysis, is a data mining technique that aims to discover interesting relationships or associations among a set of items in a transactional or relational database. It focuses on finding patterns and dependencies between items based on their co-occurrence in transactions.

Association rule mining is commonly used in retail and e-commerce industries to uncover relationships between products that are frequently purchased together. The technique helps businesses understand customer behavior, improve marketing strategies, optimize product placement, and support decision-making processes.

The output of association rule mining is typically represented in the form of "if-then" rules, known as association rules. These rules consist of an antecedent (a set of items) and a consequent (another item or set of items). The rules indicate the likelihood or support of the consequent item(s) appearing in transactions that contain the antecedent item(s). The strength of the association is measured by various metrics such as support, confidence, and lift.

For example, Apriori Algorithm state: "If a customer buys item A and item B, then they are likely to buy item C." This rule suggests a relationship between items A, B, and C, indicating that customers who purchased A and B are more likely to purchase item C as well.

WIKI: https://en.wikipedia.org/wiki/Apriori_algorithm
Examples: https://www.kaggle.com/code/earthian/apriori-association-rules-mining
"""

from typing import List, Tuple


def load_data() -> List[List[str]]:
    """
    Returns a sample transaction dataset.

    >>> load_data()
    [['milk', 'bread'], ['milk', 'butter'], ['milk', 'bread', 'nuts'], ['milk', 'bread', 'chips'], ['milk', 'butter', 'chips'], ['milk', 'bread', 'butter', 'cola'], ['nuts', 'bread', 'butter', 'cola'], ['bread', 'butter', 'cola', 'ice'], ['bread', 'butter', 'cola', 'ice', 'bun']]
    """
    # Sample transaction dataset
    data = [
        ["milk", "bread"],
        ["milk", "butter"],
        ["milk", "bread", "nuts"],
        ["milk", "bread", "chips"],
        ["milk", "butter", "chips"],
        ["milk", "bread", "butter", "cola"],
        ["nuts", "bread", "butter", "cola"],
        ["bread", "butter", "cola", "ice"],
        ["bread", "butter", "cola", "ice", "bun"],
    ]
    return data

def generate_candidates(itemset: List[str], length: int) -> List[List[str]]:
    """
    Generates candidate itemsets of size k from the given itemsets.

    >>> itemsets = [['milk', 'bread'], ['milk', 'butter'], ['milk', 'bread', 'nuts']]
    >>> generate_candidates(itemsets, 2)
    [['milk', 'bread'], ['milk', 'butter'], ['bread', 'butter']]

    >>> itemsets = [['milk', 'bread'], ['milk', 'butter'], ['bread', 'butter']]
    >>> generate_candidates(itemsets, 3)
    [['milk', 'bread', 'butter']]
    """

def generate_candidates(itemset: List[str], length: int):
    candidates = []
    for i in range(len(itemset)):
        for j in range(i + 1, len(itemset)):
            # Create a candidate by taking the union of two lists
            candidate = list(itemset[i]) + [
                item for item in itemset[j] if item not in itemset[i]
            ]
            if len(candidate) == length:
                candidates.append(candidate)

    return candidates


def prune(
    itemset: List[str], candidates: List[List[str]], length: int
) -> List[List[str]]:
    # Prune candidate itemsets
    """
    The goal of pruning is to filter out candidate itemsets that are not frequent. This is done by checking if all the (k-1) subsets of a candidate itemset are present in the frequent itemsets of the previous iteration (valid subsequences of the frequent itemsets from the previous iteration).

    Prunes candidate itemsets that are not frequent.

    >>> itemset = ['bread', 'butter', 'milk']
    >>> candidates = [['bread', 'butter'], ['bread', 'milk'], ['butter', 'milk'], ['bread', 'butter', 'milk'], ['nuts', 'bread', 'butter']]
    >>> prune(itemset, candidates, 3)
    [['bread', 'butter', 'milk']]

    >>> itemset = ['bread', 'butter', 'milk']
    >>> candidates = [['bread', 'butter'], ['bread', 'milk'], ['butter', 'milk'], ['bread', 'butter', 'milk'], ['nuts', 'bread', 'butter']]
    >>> prune(itemset, candidates, 2)
    [['bread', 'butter'], ['bread', 'milk'], ['butter', 'milk'], ['nuts', 'bread', 'butter']]
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


def apriori(data: List[List[str]], min_support: int) -> List[Tuple[List[str], int]]:
    """
    Returns a list of frequent itemsets and their support counts.

    >>> data = [['milk', 'bread'], ['milk', 'butter'], ['milk', 'bread', 'nuts'], ['milk', 'bread', 'chips'], ['milk', 'butter', 'chips'], ['milk', 'bread', 'butter', 'cola'], ['nuts', 'bread', 'butter', 'cola'], ['bread', 'butter', 'cola', 'ice'], ['bread', 'butter', 'cola', 'ice', 'bun']]
    >>> apriori(data, 3)
    [(['bread'], 7), (['butter'], 7), (['milk'], 8), (['cola', 'butter'], 3), (['bread', 'butter'], 4), (['bread', 'milk'], 4), (['butter', 'milk'], 4), (['bread', 'cola'], 3), (['milk', 'cola'], 3), (['bread', 'butter', 'milk'], 3), (['bread', 'milk', 'cola'], 3), (['butter', 'milk', 'cola'], 3), (['bread', 'butter', 'cola'], 3), (['bread', 'butter', 'milk', 'cola'], 3)]

    >>> data = [['milk', 'bread'], ['milk', 'butter'], ['milk', 'bread', 'nuts'], ['milk', 'bread', 'chips'], ['milk', 'butter', 'chips'], ['milk', 'bread', 'butter', 'cola'], ['nuts', 'bread', 'butter', 'cola'], ['bread', 'butter', 'cola', 'ice'], ['bread', 'butter', 'cola', 'ice', 'bun']]
    >>> apriori(data, 5)
    [(['bread'], 7), (['butter'], 7), (['milk'], 8)]
    """
    itemset = [set(transaction) for transaction in data]
    frequent_itemsets = []
    length = 1

    while itemset:
        # Count itemset support
        counts = [0] * len(itemset)
        for i, transaction in enumerate(data):
            for j, item in enumerate(itemset):
                if item.issubset(
                    transaction
                ):  # using set for faster membership checking
                    counts[j] += 1

        # Prune infrequent itemsets
        itemset = [item for i, item in enumerate(itemset) if counts[i] >= min_support]

        # Append frequent itemsets (as a list to maintain order)
        for i, item in enumerate(itemset):
            frequent_itemsets.append((list(item), counts[i]))

        length += 1
        candidates = generate_candidates(itemset, len(next(iter(itemset))) + 1)
        itemset = prune(itemset, candidates, len(next(iter(itemset))) + 1)

    return frequent_itemsets


if __name__ == "__main__":
    """
    Apriori algorithm for finding frequent itemsets.

    Args:
        data (List[List[str]]): A list of transactions, where each transaction is a list of items.
        min_support (int): The minimum support threshold for frequent itemsets.

    Returns:
        List[Tuple[List[str], int]]: A list of frequent itemsets along with their support counts.

    Example:
    >>> data = [["milk", "bread"], ["milk", "butter"], ["milk", "bread", "nuts"]]
    >>> min_support = 2
    >>> frequent_itemsets = apriori(data, min_support)
    >>> frequent_itemsets
    [(['milk'], 3), (['bread'], 3), (['butter'], 2), (['nuts'], 1), (['milk', 'bread'], 2)]

    >>> data = [["apple", "banana", "cherry"], ["banana", "cherry"], ["apple", "banana"]]
    >>> min_support = 2
    >>> frequent_itemsets = apriori(data, min_support)
    >>> frequent_itemsets
    [(['apple'], 2), (['banana'], 3), (['cherry'], 2), (['apple', 'banana'], 2), (['banana', 'cherry'], 2)]
    """
    data = load_data()
    min_support = 2  # user-defined threshold or minimum support level
    frequent_itemsets = apriori(data, min_support)
    for itemset, support in frequent_itemsets:
        print(f"{itemset}: {support}")
