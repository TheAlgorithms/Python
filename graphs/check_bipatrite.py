from collections import defaultdict, deque


def iki_renkli_mi_dfs(graf: defaultdict[int, list[int]]) -> bool:
    """
    Bir grafın derinlik öncelikli arama (DFS) kullanarak iki renkli olup olmadığını kontrol edin.

    Argümanlar:
        graf: Grafı temsil eden komşuluk listesi.

    Dönüş:
        İki renkli ise True, değilse False.

    Grafın iki küme halinde bölünüp bölünemeyeceğini kontrol eder, böylece aynı kümedeki iki düğüm bir kenar ile bağlı değildir.

    Örnekler:
    # FIXME: Bu test geçmelidir.
    >>> iki_renkli_mi_dfs(defaultdict(list, {0: [1, 2], 1: [0, 3], 2: [0, 4]}))
    Traceback (most recent call last):
        ...
    RuntimeError: dictionary changed size during iteration
    >>> iki_renkli_mi_dfs(defaultdict(list, {0: [1, 2], 1: [0, 3], 2: [0, 1]}))
    False
    >>> iki_renkli_mi_dfs({})
    True
    >>> iki_renkli_mi_dfs({0: [1, 3], 1: [0, 2], 2: [1, 3], 3: [0, 2]})
    True
    >>> iki_renkli_mi_dfs({0: [1, 2, 3], 1: [0, 2], 2: [0, 1, 3], 3: [0, 2]})
    False
    >>> iki_renkli_mi_dfs({0: [4], 1: [], 2: [4], 3: [4], 4: [0, 2, 3]})
    True
    >>> iki_renkli_mi_dfs({0: [1, 3], 1: [0, 2], 2: [1, 3], 3: [0, 2], 4: [0]})
    False
    >>> iki_renkli_mi_dfs({7: [1, 3], 1: [0, 2], 2: [1, 3], 3: [0, 2], 4: [0]})
    Traceback (most recent call last):
        ...
    KeyError: 0

    # FIXME: Bu test KeyError: 4 ile başarısız olmalıdır.
    >>> iki_renkli_mi_dfs({0: [1, 3], 1: [0, 2], 2: [1, 3], 3: [0, 2], 9: [0]})
    False
    >>> iki_renkli_mi_dfs({0: [-1, 3], 1: [0, -2]})
    Traceback (most recent call last):
        ...
    KeyError: -1
    >>> iki_renkli_mi_dfs({-1: [0, 2], 0: [-1, 1], 1: [0, 2], 2: [-1, 1]})
    True
    >>> iki_renkli_mi_dfs({0.9: [1, 3], 1: [0, 2], 2: [1, 3], 3: [0, 2]})
    Traceback (most recent call last):
        ...
    KeyError: 0

    # FIXME: Bu test TypeError: list indices must be integers or... ile başarısız olmalıdır.
    >>> iki_renkli_mi_dfs({0: [1.0, 3.0], 1.0: [0, 2.0], 2.0: [1.0, 3.0], 3.0: [0, 2.0]})
    True
    >>> iki_renkli_mi_dfs({"a": [1, 3], "b": [0, 2], "c": [1, 3], "d": [0, 2]})
    Traceback (most recent call last):
        ...
    KeyError: 1
    >>> iki_renkli_mi_dfs({0: ["b", "d"], 1: ["a", "c"], 2: ["b", "d"], 3: ["a", "c"]})
    Traceback (most recent call last):
        ...
    KeyError: 'b'
    """

    def derinlik_oncelikli_arama(dugum: int, renk: int) -> bool:
        """
        Bir düğümden başlayarak graf üzerinde Derinlik Öncelikli Arama (DFS) yapın.

        Argümanlar:
            dugum: Ziyaret edilen mevcut düğüm.
            renk: Mevcut düğüme atanan renk.

        Dönüş:
            Mevcut düğümden başlayarak graf iki renkli ise True, değilse False.
        """
        if ziyaret_edildi[dugum] == -1:
            ziyaret_edildi[dugum] = renk
            for komsu in graf[dugum]:
                if not derinlik_oncelikli_arama(komsu, 1 - renk):
                    return False
        return ziyaret_edildi[dugum] == renk

    ziyaret_edildi: defaultdict[int, int] = defaultdict(lambda: -1)
    for dugum in graf:
        if ziyaret_edildi[dugum] == -1 and not derinlik_oncelikli_arama(dugum, 0):
            return False
    return True


def iki_renkli_mi_bfs(graf: defaultdict[int, list[int]]) -> bool:
    """
    Bir grafın genişlik öncelikli arama (BFS) kullanarak iki renkli olup olmadığını kontrol edin.

    Argümanlar:
        graf: Grafı temsil eden komşuluk listesi.

    Dönüş:
        İki renkli ise True, değilse False.

    Grafın iki küme halinde bölünüp bölünemeyeceğini kontrol eder, böylece aynı kümedeki iki düğüm bir kenar ile bağlı değildir.

    Örnekler:
    # FIXME: Bu test geçmelidir.
    >>> iki_renkli_mi_bfs(defaultdict(list, {0: [1, 2], 1: [0, 3], 2: [0, 4]}))
    Traceback (most recent call last):
        ...
    RuntimeError: dictionary changed size during iteration
    >>> iki_renkli_mi_bfs(defaultdict(list, {0: [1, 2], 1: [0, 2], 2: [0, 1]}))
    False
    >>> iki_renkli_mi_bfs({})
    True
    >>> iki_renkli_mi_bfs({0: [1, 3], 1: [0, 2], 2: [1, 3], 3: [0, 2]})
    True
    >>> iki_renkli_mi_bfs({0: [1, 2, 3], 1: [0, 2], 2: [0, 1, 3], 3: [0, 2]})
    False
    >>> iki_renkli_mi_bfs({0: [4], 1: [], 2: [4], 3: [4], 4: [0, 2, 3]})
    True
    >>> iki_renkli_mi_bfs({0: [1, 3], 1: [0, 2], 2: [1, 3], 3: [0, 2], 4: [0]})
    False
    >>> iki_renkli_mi_bfs({7: [1, 3], 1: [0, 2], 2: [1, 3], 3: [0, 2], 4: [0]})
    Traceback (most recent call last):
        ...
    KeyError: 0

    # FIXME: Bu test KeyError: 4 ile başarısız olmalıdır.
    >>> iki_renkli_mi_bfs({0: [1, 3], 1: [0, 2], 2: [1, 3], 3: [0, 2], 9: [0]})
    False
    >>> iki_renkli_mi_bfs({0: [-1, 3], 1: [0, -2]})
    Traceback (most recent call last):
        ...
    KeyError: -1
    >>> iki_renkli_mi_bfs({-1: [0, 2], 0: [-1, 1], 1: [0, 2], 2: [-1, 1]})
    True
    >>> iki_renkli_mi_bfs({0.9: [1, 3], 1: [0, 2], 2: [1, 3], 3: [0, 2]})
    Traceback (most recent call last):
        ...
    KeyError: 0

    # FIXME: Bu test TypeError: list indices must be integers or... ile başarısız olmalıdır.
    >>> iki_renkli_mi_bfs({0: [1.0, 3.0], 1.0: [0, 2.0], 2.0: [1.0, 3.0], 3.0: [0, 2.0]})
    True
    >>> iki_renkli_mi_bfs({"a": [1, 3], "b": [0, 2], "c": [1, 3], "d": [0, 2]})
    Traceback (most recent call last):
        ...
    KeyError: 1
    >>> iki_renkli_mi_bfs({0: ["b", "d"], 1: ["a", "c"], 2: ["b", "d"], 3: ["a", "c"]})
    Traceback (most recent call last):
        ...
    KeyError: 'b'
    """
    ziyaret_edildi: defaultdict[int, int] = defaultdict(lambda: -1)
    for dugum in graf:
        if ziyaret_edildi[dugum] == -1:
            kuyruk: deque[int] = deque()
            kuyruk.append(dugum)
            ziyaret_edildi[dugum] = 0
            while kuyruk:
                mevcut_dugum = kuyruk.popleft()
                for komsu in graf[mevcut_dugum]:
                    if ziyaret_edildi[komsu] == -1:
                        ziyaret_edildi[komsu] = 1 - ziyaret_edildi[mevcut_dugum]
                        kuyruk.append(komsu)
                    elif ziyaret_edildi[komsu] == ziyaret_edildi[mevcut_dugum]:
                        return False
    return True


if __name__ == "__main__":
    import doctest

    sonuc = doctest.testmod()
    if sonuc.failed:
        print(f"{sonuc.failed} test başarısız oldu.")
    else:
        print("Tüm testler geçti!")
