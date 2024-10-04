"""
Apriori Algoritması, pazar sepeti analizi olarak da bilinen bir Birliktelik kuralı madenciliği tekniğidir ve
bir işlem veya ilişkisel veritabanındaki bir dizi öğe arasında ilginç ilişkiler veya birliktelikler keşfetmeyi amaçlar.

Örneğin, Apriori Algoritması şunu belirtir: "Bir müşteri A ve B ürünlerini satın alırsa, muhtemelen C ürününü de satın alır."
Bu kural, A, B ve C ürünleri arasında bir ilişki önerir ve A ve B'yi satın alan müşterilerin C ürününü de satın alma olasılığının yüksek olduğunu gösterir.

WIKI: https://en.wikipedia.org/wiki/Apriori_algorithm
Örnekler: https://www.kaggle.com/code/earthian/apriori-association-rules-mining
"""

from itertools import combinations
from typing import List, Tuple


def load_data() -> List[List[str]]:
    """
    Örnek bir işlem veri seti döndürür.

    >>> load_data()
    [['milk'], ['milk', 'butter'], ['milk', 'bread'], ['milk', 'bread', 'chips']]
    """
    return [["milk"], ["milk", "butter"], ["milk", "bread"], ["milk", "bread", "chips"]]


def prune(itemset: List[str], candidates: List[List[str]], length: int) -> List[List[str]]:
    """
    Sık olmayan aday öğe kümelerini budar.
    Budamanın amacı, sık olmayan aday öğe kümelerini filtrelemektir. Bu, bir aday öğe kümesinin tüm (k-1) alt kümelerinin
    önceki iterasyonun sık öğe kümelerinde (önceki iterasyonun sık öğe kümelerinin geçerli alt dizileri) bulunup bulunmadığını
    kontrol ederek yapılır.

    Sık olmayan aday öğe kümelerini budar.

    >>> itemset = ['X', 'Y', 'Z']
    >>> candidates = [['X', 'Y'], ['X', 'Z'], ['Y', 'Z']]
    >>> prune(itemset, candidates, 2)
    [['X', 'Y'], ['X', 'Z'], ['Y', 'Z']]

    >>> itemset = ['1', '2', '3', '4']
    >>> candidates = [['1', '2'], ['1', '4'], ['2', '4']]
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


def apriori(data: List[List[str]], min_support: int) -> List[Tuple[List[str], int]]:
    """
    Sık öğe kümelerini ve destek sayılarını döndürür.

    >>> data = [['A', 'B', 'C'], ['A', 'B'], ['A', 'C'], ['A', 'D'], ['B', 'C']]
    >>> apriori(data, 2)
    [(['A', 'B'], 2), (['A', 'C'], 2), (['B', 'C'], 2)]

    >>> data = [['1', '2', '3'], ['1', '2'], ['1', '3'], ['1', '4'], ['2', '3']]
    >>> apriori(data, 3)
    []
    """
    itemset = [list(transaction) for transaction in data]
    frequent_itemsets = []
    length = 1

    while itemset:
        # Öğe kümesi desteğini say
        counts = [0] * len(itemset)
        for transaction in data:
            for j, candidate in enumerate(itemset):
                if all(item in transaction for item in candidate):
                    counts[j] += 1

        # Sık olmayan öğe kümelerini buda
        itemset = [item for i, item in enumerate(itemset) if counts[i] >= min_support]

        # Sık öğe kümelerini ekle (sıralamayı korumak için liste olarak)
        for i, item in enumerate(itemset):
            frequent_itemsets.append((sorted(item), counts[i]))

        length += 1
        itemset = prune(itemset, list(combinations(itemset, length)), length)

    return frequent_itemsets


if __name__ == "__main__":
    """
    Sık öğe kümelerini bulmak için Apriori algoritması.

    Args:
        data: Her işlemin bir öğe listesi olduğu bir işlem listesi.
        min_support: Sık öğe kümeleri için minimum destek eşiği.

    Returns:
        Sık öğe kümeleri ve destek sayıları ile birlikte bir liste.
    """
    import doctest

    doctest.testmod()

    # kullanıcı tanımlı eşik veya minimum destek seviyesi
    frequent_itemsets = apriori(data=load_data(), min_support=2)
    print("\n".join(f"{itemset}: {support}" for itemset, support in frequent_itemsets))
