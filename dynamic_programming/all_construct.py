"""
Bir hedef dizenin verilen alt dize listesinden
nasıl oluşturulabileceğini listeleyen program
"""

from __future__ import annotations


def tum_yapilar(target: str, kelime_bankasi: list[str] | None = None) -> list[list[str]]:
    """
        Bir dizenin (hedef) verilen alt dize listesinden (kelime_bankasi)
        nasıl oluşturulabileceğine dair tüm olası kombinasyonları içeren listeyi döndürür
    >>> tum_yapilar("hello", ["he", "l", "o"])
    [['he', 'l', 'l', 'o']]
    >>> tum_yapilar("purple",["purp","p","ur","le","purpl"])
    [['purp', 'le'], ['p', 'ur', 'p', 'le']]
    """

    kelime_bankasi = kelime_bankasi or []
    # bir tablo oluştur
    tablo_boyutu: int = len(target) + 1

    tablo: list[list[list[str]]] = []
    for _ in range(tablo_boyutu):
        tablo.append([])
    # başlangıç değeri
    tablo[0] = [[]]  # çünkü boş dizenin boş kombinasyonu vardır

    # indeksler boyunca yinele
    for i in range(tablo_boyutu):
        # koşul
        if tablo[i] != []:
            for kelime in kelime_bankasi:
                # dilim koşulu
                if target[i : i + len(kelime)] == kelime:
                    yeni_kombinasyonlar: list[list[str]] = [
                        [kelime, *yol] for yol in tablo[i]
                    ]
                    # kelimeyi mevcut konumun tuttuğu her kombinasyona ekler
                    # şimdi, bu kombinasyonu tablo[i+len(kelime)]'ye ekle
                    tablo[i + len(kelime)] += yeni_kombinasyonlar

    # kombinasyonlar ters sıradadır, bu yüzden daha iyi çıktı için ters çevir
    for kombinasyon in tablo[len(target)]:
        kombinasyon.reverse()

    return tablo[len(target)]


if __name__ == "__main__":
    print(tum_yapilar("jwajalapa", ["jwa", "j", "w", "a", "la", "lapa"]))
    print(tum_yapilar("rajamati", ["s", "raj", "amat", "raja", "ma", "i", "t"]))
    print(
        tum_yapilar(
            "hexagonosaurus",
            ["h", "ex", "hex", "ag", "ago", "ru", "auru", "rus", "go", "no", "o", "s"],
        )
    )
