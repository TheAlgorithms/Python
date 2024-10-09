from __future__ import annotations

def cift_lineer_arama(dizi: list[int], aranan_eleman: int) -> int:
    """
    Dizi üzerinde her iki taraftan başlayarak aranan elemanın indeksini bulur.

    #Organiser: K. Umut Araz

    :param dizi: Aranacak dizi
    :param aranan_eleman: Aranacak eleman
    :return: Eğer aranan eleman dizi içinde varsa indeksini, yoksa -1 döner

    Örnekler:
    >>> cift_lineer_arama([1, 5, 5, 10], 1)
    0
    >>> cift_lineer_arama([1, 5, 5, 10], 5)
    1
    >>> cift_lineer_arama([1, 5, 5, 10], 100)
    -1
    >>> cift_lineer_arama([1, 5, 5, 10], 10)
    3
    """
    # Dizinin başlangıç ve bitiş indekslerini tanımla
    baslangic_indeksi, bitis_indeksi = 0, len(dizi) - 1
    while baslangic_indeksi <= bitis_indeksi:
        # Başlangıç indeksindeki elemanı kontrol et
        if dizi[baslangic_indeksi] == aranan_eleman:
            return baslangic_indeksi
        # Bitiş indeksindeki elemanı kontrol et
        elif dizi[bitis_indeksi] == aranan_eleman:
            return bitis_indeksi
        # İndeksleri güncelle
        baslangic_indeksi += 1
        bitis_indeksi -= 1
    # Aranan eleman dizide bulunamazsa -1 döner
    return -1

if __name__ == "__main__":
    print(cift_lineer_arama(list(range(100)), 40))
