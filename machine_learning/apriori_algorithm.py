"""
Apriori Algorithm with Association Rules (support, confidence, lift).

This implementation finds:
- Frequent itemsets
- Association rules with minimum confidence and lift

WIKI: https://en.wikipedia.org/wiki/Apriori_algorithm
"""

from collections import defaultdict
from itertools import combinations
from typing import List, Dict, Tuple, Set


def load_data() -> List[List[str]]:
    """
    Returns a sample transaction dataset.

    >>> data = load_data()
    >>> len(data)
    4
    >>> 'milk' in data[0]
    True
    """
    return [["milk"], ["milk", "butter"], ["milk", "bread"], ["milk", "bread", "chips"]]


class Apriori:
    """Apriori algorithm class with support, confidence, and lift filtering."""

    def __init__(
        self,
        transactions: List[List[str]],
        min_support: float = 0.25,
        min_confidence: float = 0.5,
        min_lift: float = 1.0,
    ) -> None:
        self.transactions: List[Set[str]] = [set(t) for t in transactions]
        self.min_support: float = min_support
        self.min_confidence: float = min_confidence
        self.min_lift: float = min_lift
        self.itemsets: List[Dict[frozenset, float]] = []
        self.rules: List[Tuple[frozenset, frozenset, float, float]] = []

        self.find_frequent_itemsets()
        self.generate_association_rules()

    def _get_support(self, itemset: frozenset) -> float:
        """Return support of an itemset."""
        return sum(1 for t in self.transactions if itemset.issubset(t)) / len(
            self.transactions
        )

    def confidence(self, antecedent: frozenset, consequent: frozenset) -> float:
        """Calculate confidence of a rule A -> B."""
        support_antecedent: float = self._get_support(antecedent)
        support_both: float = self._get_support(antecedent | consequent)
        return support_both / support_antecedent if support_antecedent > 0 else 0.0

    def lift(self, antecedent: frozenset, consequent: frozenset) -> float:
        """Calculate lift of a rule A -> B."""
        support_consequent: float = self._get_support(consequent)
        conf: float = self.confidence(antecedent, consequent)
        return conf / support_consequent if support_consequent > 0 else 0.0

    def find_frequent_itemsets(self) -> List[Dict[frozenset, float]]:
        """Generate all frequent itemsets."""
        item_counts: Dict[frozenset, int] = defaultdict(int)
        for t in self.transactions:
            for item in t:
                item_counts[frozenset([item])] += 1

        total: int = len(self.transactions)
        current_itemsets: Dict[frozenset, float] = {
            k: v / total for k, v in item_counts.items() if v / total >= self.min_support
        }
        if current_itemsets:
            self.itemsets.append(current_itemsets)

        k: int = 2
        while current_itemsets:
            candidates: Set[frozenset] = set()
            keys: List[frozenset] = list(current_itemsets.keys())
            for i in range(len(keys)):
                for j in range(i + 1, len(keys)):
                    union = keys[i] | keys[j]
                    if len(union) == k and all(
                        frozenset(sub) in current_itemsets
                        for sub in combinations(union, k - 1)
                    ):
                        candidates.add(union)

            freq_candidates: Dict[frozenset, float] = {
                c: self._get_support(c) for c in candidates if self._get_support(c) >= self.min_support
            }
            if not freq_candidates:
                break

            self.itemsets.append(freq_candidates)
            current_itemsets = freq_candidates
            k += 1

        return self.itemsets

    def generate_association_rules(self) -> List[Tuple[frozenset, frozenset, float, float]]:
        """Generate association rules with min confidence and lift."""
        for level in self.itemsets:
            for itemset in level:
                if len(itemset) < 2:
                    continue
                for i in range(1, len(itemset)):
                    for antecedent in combinations(itemset, i):
                        antecedent_set: frozenset = frozenset(antecedent)
                        consequent_set: frozenset = itemset - antecedent_set
                        conf: float = self.confidence(antecedent_set, consequent_set)
                        lft: float = self.lift(antecedent_set, consequent_set)
                        rule: Tuple[frozenset, frozenset, float, float] = (
                            antecedent_set,
                            consequent_set,
                            conf,
                            lft,
                        )
                        if rule not in self.rules and conf >= self.min_confidence and lft >= self.min_lift:
                            self.rules.append(rule)
        return self.rules


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    transactions: List[List[str]] = load_data()
    model: Apriori = Apriori(
        transactions, min_support=0.25, min_confidence=0.1, min_lift=0.0
    )

    print("Frequent itemsets:")
    for level in model.itemsets:
        for items, sup in level.items():
            print(f"{set(items)}: {sup:.2f}")

    print("\nAssociation Rules:")
    for rule in model.rules:
        antecedent, consequent, conf, lift_value = rule
        print(
            f"{set(antecedent)} -> {set(consequent)}, "
            f"conf={conf:.2f}, lift={lift_value:.2f}"
        )
