"""
https://tr.wikipedia.org/wiki/Genişlik-öncelikli_arama
pseudo-kod:
genişlik_öncelikli_arama(graf G, başlangıç düğümü s):
// tüm düğümler başlangıçta keşfedilmemiştir
s'yi keşfedilmiş olarak işaretle
Q adında bir kuyruk veri yapısı oluştur ve s ile başlat
Q boş olmadığı sürece:
    Q'nun ilk düğümünü çıkar, buna v diyelim
    her bir kenar(v, w) için:  // w graf[v]'de
        eğer w keşfedilmemişse:
            w'yi keşfedilmiş olarak işaretle
            w'yi Q'ya ekle (sonuna)
"""

from __future__ import annotations

from collections import deque
from queue import Queue
from timeit import timeit

G = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"],
}

#Produced by K. Umut Araz (https://github.com/arazumut)

def genişlik_öncelikli_arama(graf: dict, başlangıç: str) -> list[str]:
    """
    queue.Queue kullanarak genişlik öncelikli arama uygulaması.

    >>> ''.join(genişlik_öncelikli_arama(G, 'A'))
    'ABCDEF'
    """
    keşfedilen = {başlangıç}
    sonuç = [başlangıç]
    kuyruk: Queue = Queue()
    kuyruk.put(başlangıç)
    while not kuyruk.empty():
        v = kuyruk.get()
        for w in graf[v]:
            if w not in keşfedilen:
                keşfedilen.add(w)
                sonuç.append(w)
                kuyruk.put(w)
    return sonuç


def deque_ile_genişlik_öncelikli_arama(graf: dict, başlangıç: str) -> list[str]:
    """
    collection.deque kullanarak genişlik öncelikli arama uygulaması.

    >>> ''.join(deque_ile_genişlik_öncelikli_arama(G, 'A'))
    'ABCDEF'
    """
    ziyaret_edilen = {başlangıç}
    sonuç = [başlangıç]
    kuyruk = deque([başlangıç])
    while kuyruk:
        v = kuyruk.popleft()
        for çocuk in graf[v]:
            if çocuk not in ziyaret_edilen:
                ziyaret_edilen.add(çocuk)
                sonuç.append(çocuk)
                kuyruk.append(çocuk)
    return sonuç


def fonksiyon_benchmark(name: str) -> None:
    setup = f"from __main__ import G, {name}"
    number = 10000
    res = timeit(f"{name}(G, 'A')", setup=setup, number=number)
    print(f"{name:<35} {number} çalıştırmada {res:.5f} saniyede tamamlandı")


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    fonksiyon_benchmark("genişlik_öncelikli_arama")
    fonksiyon_benchmark("deque_ile_genişlik_öncelikli_arama")
    # genişlik_öncelikli_arama                10000 çalıştırmada 0.20999 saniyede tamamlandı
    # deque_ile_genişlik_öncelikli_arama     10000 çalıştırmada 0.01421 saniyede tamamlandı
