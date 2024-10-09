"""Genişlik-öncelikli arama ile en kısa yol bulma uygulamaları.
doctest:
python -m doctest -v bfs_shortest_path.py
Manuel test:
python bfs_shortest_path.py
"""

demo_graf = {
    "A": ["B", "C", "E"],
    "B": ["A", "D", "E"],
    "C": ["A", "F", "G"],
    "D": ["B"],
    "E": ["A", "B", "D"],
    "F": ["C"],
    "G": ["C"],
}

#Produced by K. Umut Araz 


def genişlik_öncelikli_en_kısa_yol(graf: dict, başlangıç, hedef) -> list[str]:
    """`başlangıç` ve `hedef` düğümleri arasındaki en kısa yolu bulur.
    Argümanlar:
        graf (dict): düğüm/komşu düğümler listesi anahtar/değer çiftleri.
        başlangıç: başlangıç düğümü.
        hedef: hedef düğüm.
    Döndürür:
        `başlangıç` ve `hedef` düğümleri arasındaki en kısa yolu düğüm listesi olarak döndürür.
        Eğer yol bulunamazsa 'Not found' stringi döner.
    Örnek:
        >>> genişlik_öncelikli_en_kısa_yol(demo_graf, "G", "D")
        ['G', 'C', 'A', 'B', 'D']
        >>> genişlik_öncelikli_en_kısa_yol(demo_graf, "G", "G")
        ['G']
        >>> genişlik_öncelikli_en_kısa_yol(demo_graf, "G", "Bilinmeyen")
        []
    """
    # keşfedilen düğümleri takip et
    keşfedilen = set()
    # kontrol edilecek tüm yolları takip et
    kuyruk = [[başlangıç]]

    # başlangıç hedefse yolu döndür
    if başlangıç == hedef:
        return [başlangıç]

    # tüm olası yollar kontrol edilene kadar döngüye devam et
    while kuyruk:
        # kuyruğun ilk yolunu çıkar
        yol = kuyruk.pop(0)
        # yolun son düğümünü al
        düğüm = yol[-1]
        if düğüm not in keşfedilen:
            komşular = graf[düğüm]
            # tüm komşu düğümleri kontrol et, yeni bir yol oluştur ve kuyruğa ekle
            for komşu in komşular:
                yeni_yol = list(yol)
                yeni_yol.append(komşu)
                kuyruk.append(yeni_yol)
                # komşu hedefse yolu döndür
                if komşu == hedef:
                    return yeni_yol

            # düğümü keşfedilen olarak işaretle
            keşfedilen.add(düğüm)

    # iki düğüm arasında yol yoksa
    return []


def genişlik_öncelikli_en_kısa_yol_mesafesi(graf: dict, başlangıç, hedef) -> int:
    """`başlangıç` ve `hedef` düğümleri arasındaki en kısa yol mesafesini bulur.
    Argümanlar:
        graf: düğüm/komşu düğümler listesi anahtar/değer çiftleri.
        başlangıç: aramaya başlanacak düğüm.
        hedef: aranacak düğüm.
    Döndürür:
        `başlangıç` ve `hedef` düğümleri arasındaki en kısa yolun kenar sayısını döndürür.
        Eğer yol yoksa -1 döner.
    Örnek:
        >>> genişlik_öncelikli_en_kısa_yol_mesafesi(demo_graf, "G", "D")
        4
        >>> genişlik_öncelikli_en_kısa_yol_mesafesi(demo_graf, "A", "A")
        0
        >>> genişlik_öncelikli_en_kısa_yol_mesafesi(demo_graf, "A", "Bilinmeyen")
        -1
    """
    if not graf or başlangıç not in graf or hedef not in graf:
        return -1
    if başlangıç == hedef:
        return 0
    kuyruk = [başlangıç]
    ziyaret_edilen = set(başlangıç)
    # `başlangıç` düğümünden mesafeleri takip et
    mesafe = {başlangıç: 0, hedef: -1}
    while kuyruk:
        düğüm = kuyruk.pop(0)
        if düğüm == hedef:
            mesafe[hedef] = (
                mesafe[düğüm] if mesafe[hedef] == -1 else min(mesafe[hedef], mesafe[düğüm])
            )
        for komşu in graf[düğüm]:
            if komşu not in ziyaret_edilen:
                ziyaret_edilen.add(komşu)
                kuyruk.append(komşu)
                mesafe[komşu] = mesafe[düğüm] + 1
    return mesafe[hedef]


if __name__ == "__main__":
    print(genişlik_öncelikli_en_kısa_yol(demo_graf, "G", "D"))  # ['G', 'C', 'A', 'B', 'D'] döner
    print(genişlik_öncelikli_en_kısa_yol_mesafesi(demo_graf, "G", "D"))  # 4 döner
