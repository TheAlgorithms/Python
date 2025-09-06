"""
Apriori Algorithm with Association Rules (support, confidence, lift).

This implementation finds:
- Frequent itemsets
- Association rules with minimum confidence and lift

WIKI: https://en.wikipedia.org/wiki/Apriori_algorithm
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


class Apriori:
    """Apriori algorithm class with support, confidence, and lift filtering."""

    def __init__(self, transactions, min_support=0.25, min_confidence=0.5, min_lift=1.0):
        self.transactions = [set(t) for t in transactions]
        self.min_support = min_support
        self.min_confidence = min_confidence
        self.min_lift = min_lift
        self.itemsets = []
        self.rules = []

        self.find_frequent_itemsets()
        self.generate_association_rules()

    def _get_support(self, itemset: frozenset) -> float:
        """Return support of an itemset."""
        return sum(1 for t in self.transactions if itemset.issubset(t)) / len(self.transactions)

    def confidence(self, antecedent: frozenset, consequent: frozenset) -> float:
        """Calculate confidence of a rule A -> B."""
        support_antecedent = self._get_support(antecedent)
        support_both = self._get_support(antecedent | consequent)
        return support_both / support_antecedent if support_antecedent > 0 else 0

    def lift(self, antecedent: frozenset, consequent: frozenset) -> float:
        """Calculate lift of a rule A -> B."""
        support_consequent = self._get_support(consequent)
        conf = self.confidence(antecedent, consequent)
        return conf / support_consequent if support_consequent > 0 else 0

    def find_frequent_itemsets(self):
        """Generate all frequent itemsets."""
        item_counts = defaultdict(int)
        for t in self.transactions:
            for item in t:
                item_counts[frozenset([item])] += 1

        total = len(self.transactions)
        current_itemsets = {k: v / total for k, v in item_counts.items() if v / total >= self.min_support}
        self.itemsets.append(current_itemsets)

        k = 2
        while current_itemsets:
            candidates = set()
            keys = list(current_itemsets.keys())
            for i in range(len(keys)):
                for j in range(i + 1, len(keys)):
                    union = keys[i] | keys[j]
                    if len(union) == k and all(frozenset(sub) in current_itemsets for sub in combinations(union, k - 1)):
                            candidates.add(union)

            freq_candidates = {c: self._get_support(c) for c in candidates if self._get_support(c) >= self.min_support}
            if not freq_candidates:
                break

            self.itemsets.append(freq_candidates)
            current_itemsets = freq_candidates
            k += 1

        return self.itemsets

    def generate_association_rules(self):
        """Generate association rules with min confidence and lift."""
        for level in self.itemsets:
            for itemset in level:
                if len(itemset) < 2:
                    continue
                for i in range(1, len(itemset)):
                    for antecedent in combinations(itemset, i):
                        antecedent = frozenset(antecedent)
                        consequent = itemset - antecedent
                        conf = self.confidence(antecedent, consequent)
                        lft = self.lift(antecedent, consequent)
                        if conf >= self.min_confidence and lft >= self.min_lift:
                            self.rules.append((antecedent, consequent, conf, lft))
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
        print(f"{set(antecedent)} -> {set(consequent)}, conf={conf:.2f}, lift={lift:.2f}")
