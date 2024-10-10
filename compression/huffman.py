from __future__ import annotations

import sys

# Organiser: K. Umut Araz


class Harf:
    def __init__(self, harf: str, frekans: int):
        self.harf: str = harf
        self.frekans: int = frekans
        self.bit_dizisi: dict[str, str] = {}

    def __repr__(self) -> str:
        return f"{self.harf}:{self.frekans}"


class AgacDugumu:
    def __init__(self, frekans: int, sol: Harf | AgacDugumu, sag: Harf | AgacDugumu):
        self.frekans: int = frekans
        self.sol: Harf | AgacDugumu = sol
        self.sag: Harf | AgacDugumu = sag


def dosyayi_parcala(dosya_yolu: str) -> list[Harf]:
    """
    Dosyayı oku ve tüm harflerin frekanslarını içeren bir sözlük oluştur,
    ardından bu sözlüğü Harf listesine dönüştür.
    """
    karakterler: dict[str, int] = {}
    with open(dosya_yolu) as f:
        while True:
            c = f.read(1)
            if not c:
                break
            karakterler[c] = karakterler[c] + 1 if c in karakterler else 1
    return sorted((Harf(c, f) for c, f in karakterler.items()), key=lambda x: x.frekans)


def agaci_olustur(harfler: list[Harf]) -> Harf | AgacDugumu:
    """
    Harfler listesini kullanarak Huffman Ağacı için minimum yığın oluştur.
    """
    yanit: list[Harf | AgacDugumu] = list(harfler)
    while len(yanit) > 1:
        sol = yanit.pop(0)
        sag = yanit.pop(0)
        toplam_frekans = sol.frekans + sag.frekans
        dugum = AgacDugumu(toplam_frekans, sol, sag)
        yanit.append(dugum)
        yanit.sort(key=lambda x: x.frekans)
    return yanit[0]


def agaci_gezin(root: Harf | AgacDugumu, bit_dizisi: str) -> list[Harf]:
    """
    Huffman Ağacını özyinelemeli olarak gezerek her Harf'in bit dizisi sözlüğünü ayarla
    ve Harfler listesini döndür.
    """
    if isinstance(root, Harf):
        root.bit_dizisi[root.harf] = bit_dizisi
        return [root]
    dugum: AgacDugumu = root
    harfler = []
    harfler += agaci_gezin(dugum.sol, bit_dizisi + "0")
    harfler += agaci_gezin(dugum.sag, bit_dizisi + "1")
    return harfler


def huffman(dosya_yolu: str) -> None:
    """
    Dosyayı parçala, ağacı oluştur, ardından dosyayı tekrar gezerek
    harfler sözlüğünü kullanarak her harf için bit dizisini bul ve yazdır.
    """
    harfler_listesi = dosyayi_parcala(dosya_yolu)
    root = agaci_olustur(harfler_listesi)
    harfler = {
        k: v for harf in agaci_gezin(root, "") for k, v in harf.bit_dizisi.items()
    }
    print(f"{dosya_yolu} için Huffman Kodlaması: ")
    with open(dosya_yolu) as f:
        while True:
            c = f.read(1)
            if not c:
                break
            print(harfler[c], end=" ")
    print()


if __name__ == "__main__":
    # huffman fonksiyonuna dosya yolunu geç
    huffman(sys.argv[1])
