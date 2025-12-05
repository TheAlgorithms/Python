"""
Apriori Algorithm with Association Rules (support, confidence, lift).

This implementation finds:
- Frequent itemsets
- Association rules with minimum confidence and lift

WIKI: https://en.wikipedia.org/wiki/Apriori_algorithm
"""

from collections import defaultdict
from collections import Counter
from itertools import combinations


def load_data() -> list[list[str]]:
    """
    Returns a sample transaction dataset.

    >>> load_data()
    [['milk'], ['milk', 'butter'], ['milk', 'bread'], ['milk', 'bread', 'chips']]
    """
    return [["milk"], ["milk", "butter"], ["milk", "bread"], ["milk", "bread", "chips"]]


class Apriori:
    """Apriori algorithm class with support, confidence, and lift filtering."""

    def __init__(
        self,
        transactions: list[list[str]],
        min_support: float = 0.25,
        min_confidence: float = 0.5,
        min_lift: float = 1.0,
    ) -> None:
        self.transactions: list[set[str]] = [set(t) for t in transactions]
        self.min_support: float = min_support
        self.min_confidence: float = min_confidence
        self.min_lift: float = min_lift
        self.itemsets: list[dict[frozenset, float]] = []
        self.rules: list[tuple[frozenset, frozenset, float, float]] = []

        self.find_frequent_itemsets()
        self.generate_association_rules()

    def _get_support(self, itemset: frozenset) -> float:
        """Return support of an itemset."""
        return sum(1 for t in self.transactions if itemset.issubset(t)) / len(
            self.transactions
        )

    def confidence(self, antecedent: frozenset, consequent: frozenset) -> float:
        """Calculate confidence of a rule A -> B."""
        support_antecedent = self._get_support(antecedent)
        support_both = self._get_support(antecedent | consequent)
        return support_both / support_antecedent if support_antecedent > 0 else 0.0

    def lift(self, antecedent: frozenset, consequent: frozenset) -> float:
        """Calculate lift of a rule A -> B."""
        support_consequent = self._get_support(consequent)
        conf = self.confidence(antecedent, consequent)
        return conf / support_consequent if support_consequent > 0 else 0.0

    def find_frequent_itemsets(self) -> list[dict[frozenset, float]]:
        """Generate all frequent itemsets."""
        item_counts: dict[frozenset, int] = defaultdict(int)
        for t in self.transactions:
            for item in t:
                item_counts[frozenset([item])] += 1

        total: int = len(self.transactions)
        current_itemsets: dict[frozenset, float] = {
            k: v / total
            for k, v in item_counts.items()
            if v / total >= self.min_support
        }
        if current_itemsets:
            self.itemsets.append(current_itemsets)

        k: int = 2
        while current_itemsets:
            candidates: set[frozenset] = set()
            keys: list[frozenset] = list(current_itemsets.keys())
            for i in range(len(keys)):
                for j in range(i + 1, len(keys)):
                    union = keys[i] | keys[j]
                    if len(union) == k and all(
                        frozenset(sub) in current_itemsets
                        for sub in combinations(union, k - 1)
                    ):
                        candidates.add(union)

            freq_candidates: dict[frozenset, float] = {
                c: self._get_support(c)
                for c in candidates
                if self._get_support(c) >= self.min_support
            }
            if not freq_candidates:
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
    itemset_counter = Counter(tuple(item) for item in itemset)
    pruned = []
    for candidate in candidates:
        is_subsequence = True
        for item in candidate:
            item_tuple = tuple(item)
            if (
                item_tuple not in itemset_counter
                or itemset_counter[item_tuple] < length - 1
            ):
                is_subsequence = False
                break

            self.itemsets.append(freq_candidates)
            current_itemsets = freq_candidates
            k += 1

        return self.itemsets

    def generate_association_rules(
        self,
    ) -> list[tuple[frozenset, frozenset, float, float]]:
        """Generate association rules with min confidence and lift."""
        for level in self.itemsets:
            for itemset in level:
                if len(itemset) < 2:
                    continue
                for i in range(1, len(itemset)):
                    for antecedent in combinations(itemset, i):
                        antecedent_set = frozenset(antecedent)
                        consequent_set = itemset - antecedent_set
                        conf = self.confidence(antecedent_set, consequent_set)
                        lft = self.lift(antecedent_set, consequent_set)
                        if conf >= self.min_confidence and lft >= self.min_lift:
                            self.rules.append(
                                (antecedent_set, consequent_set, conf, lft)
                            )
        return self.rules


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    transactions = load_data()
    model = Apriori(transactions, min_support=0.25, min_confidence=0.1, min_lift=0.0)

    print("Frequent itemsets:")
    for level in model.itemsets:
        for items, sup in level.items():
            print(f"{set(items)}: {sup:.2f}")

    print("\nAssociation Rules:")
    for rule in model.rules:
        antecedent, consequent, conf, lift = rule
        print(
            f"{set(antecedent)} -> {set(consequent)}, conf={conf:.2f}, lift={lift:.2f}"
        )
