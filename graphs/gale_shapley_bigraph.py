from __future__ import annotations


def kararlı_eslestirme(
    bagisci_tercihleri: list[list[int]], alici_tercihleri: list[list[int]]
) -> list[int]:
    """
    İki parçalı herhangi bir grafikte kararlı eşleşmeyi bulur, yani hiçbir 2 nesne
    birbirini partnerine tercih etmez. Fonksiyon, organ bağışçılarının ve alıcılarının
    tercihlerini (her ikisi de 0'dan n-1'e kadar numaralandırılmıştır) kabul eder ve
    bağışçının indeks pozisyonuna karşılık gelen ve değeri organ alıcısı olan bir liste
    döndürür.

    Algoritmayı daha iyi anlamak için ayrıca bakınız:
    https://github.com/akashvshroff/Gale_Shapley_Stable_Matching (README).
    https://www.youtube.com/watch?v=Qcv1IqHWAzg&t=13s (Numberphile YouTube).

    >>> bagisci_tercihleri = [[0, 1, 3, 2], [0, 2, 3, 1], [1, 0, 2, 3], [0, 3, 1, 2]]
    >>> alici_tercihleri = [[3, 1, 2, 0], [3, 1, 0, 2], [0, 3, 1, 2], [1, 0, 3, 2]]
    >>> kararlı_eslestirme(bagisci_tercihleri, alici_tercihleri)
    [1, 2, 3, 0]
    """
    assert len(bagisci_tercihleri) == len(alici_tercihleri)

    n = len(bagisci_tercihleri)
    eslesmemis_bagiscilar = list(range(n))
    bagisci_kaydi = [-1] * n  # bağışçının kime bağış yaptığı
    alici_kaydi = [-1] * n  # alıcının kimden bağış aldığı
    bagis_sayisi = [0] * n

    while eslesmemis_bagiscilar:
        bagisci = eslesmemis_bagiscilar[0]
        bagisci_tercihi = bagisci_tercihleri[bagisci]
        alici = bagisci_tercihi[bagis_sayisi[bagisci]]
        bagis_sayisi[bagisci] += 1
        alici_tercihi = alici_tercihleri[alici]
        onceki_bagisci = alici_kaydi[alici]

        if onceki_bagisci != -1:
            if alici_tercihi.index(onceki_bagisci) > alici_tercihi.index(bagisci):
                alici_kaydi[alici] = bagisci
                bagisci_kaydi[bagisci] = alici
                eslesmemis_bagiscilar.append(onceki_bagisci)
                eslesmemis_bagiscilar.remove(bagisci)
        else:
            alici_kaydi[alici] = bagisci
            bagisci_kaydi[bagisci] = alici
            eslesmemis_bagiscilar.remove(bagisci)
    return bagisci_kaydi
