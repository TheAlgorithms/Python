from collections import deque


def tarjan(g: list[list[int]]) -> list[list[int]]:
    """
    Tarjan'ın algoritması, yönlendirilmiş bir grafikte güçlü bağlı bileşenleri bulmak için kullanılır.

    Produced By. K. Umut Araz

    Her düğümün erişilebilirliğini izlemek için iki ana özelliği kullanır: bir bileşen içindeki düğümün indeksi (index)
    ve o düğümden erişilebilen en düşük indeks (lowlink).

    Daha sonra her bileşenin derinlemesine aramasını (DFS) yaparız, bu parametreleri her düğüm için güncelleyerek
    ve ziyaret ettiğimiz düğümleri kaydederek.

    Eğer bir düğümden erişilebilen en düşük düğümün indeksi, o düğümün indeksine eşitse, bu düğüm güçlü bağlı bir bileşenin
    kökü olmalıdır ve bu nedenle onu ve eş erişilebilir düğümlerini güçlü bağlı bileşen olarak kaydederiz.

    Karmaşıklık: strong_connect() her düğüm için en fazla bir kez çağrılır ve O(|E|) karmaşıklığına sahiptir çünkü bu bir DFS'dir.
    Bu nedenle, bu algoritmanın karmaşıklığı bir grafik G = (V, E) için O(|V| + |E|) dir.

    >>> tarjan([[2, 3, 4], [2, 3, 4], [0, 1, 3], [0, 1, 2], [1]])
    [[4, 3, 1, 2, 0]]
    >>> tarjan([[], [], [], []])
    [[0], [1], [2], [3]]
    >>> a = [0, 1, 2, 3, 4, 5, 4]
    >>> b = [1, 0, 3, 2, 5, 4, 0]
    >>> n = 7
    >>> sorted(tarjan(create_graph(n, list(zip(a, b))))) == sorted(
    ...     tarjan(create_graph(n, list(zip(a[::-1], b[::-1])))))
    True
    >>> a = [0, 1, 2, 3, 4, 5, 6]
    >>> b = [0, 1, 2, 3, 4, 5, 6]
    >>> sorted(tarjan(create_graph(n, list(zip(a, b)))))
    [[0], [1], [2], [3], [4], [5], [6]]
    """

    n = len(g)
    stack: deque[int] = deque()
    yigin_ustunde = [False for _ in range(n)]
    indeks = [-1 for _ in range(n)]
    en_dusuk_indeks = indeks[:]

    def strong_connect(v: int, index: int, bileşenler: list[list[int]]) -> int:
        indeks[v] = index  # bu düğüm görüldüğünde numarası
        en_dusuk_indeks[v] = index  # buradan erişilebilen en düşük sıralı düğüm
        index += 1
        stack.append(v)
        yigin_ustunde[v] = True

        for w in g[v]:
            if indeks[w] == -1:
                index = strong_connect(w, index, bileşenler)
                en_dusuk_indeks[v] = (
                    en_dusuk_indeks[w] if en_dusuk_indeks[w] < en_dusuk_indeks[v] else en_dusuk_indeks[v]
                )
            elif yigin_ustunde[w]:
                en_dusuk_indeks[v] = (
                    en_dusuk_indeks[w] if en_dusuk_indeks[w] < en_dusuk_indeks[v] else en_dusuk_indeks[v]
                )

        if en_dusuk_indeks[v] == indeks[v]:
            bileşen = []
            w = stack.pop()
            yigin_ustunde[w] = False
            bileşen.append(w)
            while w != v:
                w = stack.pop()
                yigin_ustunde[w] = False
                bileşen.append(w)
            bileşenler.append(bileşen)
        return index

    bileşenler: list[list[int]] = []
    for v in range(n):
        if indeks[v] == -1:
            strong_connect(v, 0, bileşenler)

    return bileşenler


def create_graph(n: int, edges: list[tuple[int, int]]) -> list[list[int]]:
    """
    >>> n = 7
    >>> source = [0, 0, 1, 2, 3, 3, 4, 4, 6]
    >>> target = [1, 3, 2, 0, 1, 4, 5, 6, 5]
    >>> edges = list(zip(source, target))
    >>> create_graph(n, edges)
    [[1, 3], [2], [0], [1, 4], [5, 6], [], [5]]
    """
    g: list[list[int]] = [[] for _ in range(n)]
    for u, v in edges:
        g[u].append(v)
    return g


if __name__ == "__main__":
    # Test
    n_vertices = 7
    source = [0, 0, 1, 2, 3, 3, 4, 4, 6]
    target = [1, 3, 2, 0, 1, 4, 5, 6, 5]
    edges = list(zip(source, target))
    g = create_graph(n_vertices, edges)

    assert tarjan(g) == [[5], [6], [4], [3, 2, 1, 0]]
