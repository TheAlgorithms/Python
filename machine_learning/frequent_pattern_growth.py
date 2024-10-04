"""
Sık Kullanılan Örüntü Büyüme algoritması (FP-Growth), büyük işlem veritabanlarında
sık kullanılan öğe kümelerini keşfetmek için yaygın olarak kullanılan bir veri madenciliği
tekniğidir.

Apriori gibi geleneksel yöntemlerin bazı sınırlamalarını aşarak FP-Tree'yi verimli bir şekilde oluşturur.

WIKI: https://athena.ecs.csus.edu/~mei/associationcw/FpGrowth.html

Örnekler: https://www.javatpoint.com/fp-growth-algorithm-in-data-mining
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class AgacDugumu:
    """
    Sık Kullanılan Örüntü ağacında bir düğüm.

    Args:
        isim: Bu düğümün adı.
        sayi: Düğümün oluşum sayısı.
        ebeveyn_dugum: Ebeveyn düğüm.

    Örnek:
    >>> ebeveyn = AgacDugumu("Ebeveyn", 1, None)
    >>> cocuk = AgacDugumu("Cocuk", 2, ebeveyn)
    >>> cocuk.isim
    'Cocuk'
    >>> cocuk.sayi
    2
    """

    isim: str
    sayi: int
    ebeveyn: AgacDugumu | None = None
    cocuklar: dict[str, AgacDugumu] = field(default_factory=dict)
    dugum_baglantisi: AgacDugumu | None = None

    def __repr__(self) -> str:
        return f"AgacDugumu({self.isim!r}, {self.sayi!r}, {self.ebeveyn!r})"

    def arttir(self, sayi: int) -> None:
        self.sayi += sayi

    def goster(self, ind: int = 1) -> None:
        print(f"{'  ' * ind} {self.isim}  {self.sayi}")
        for cocuk in self.cocuklar.values():
            cocuk.goster(ind + 1)


def agac_olustur(veri_seti: list, min_destek: int = 1) -> tuple[AgacDugumu, dict]:
    """
    Sık Kullanılan Örüntü ağacı oluştur

    Args:
        veri_seti: Her işlem bir öğe listesi olan işlemler listesi.
        min_destek: Minimum destek eşiği.
        Desteği bu değerden az olan öğeler budanacaktır. Varsayılan 1'dir.

    Returns:
        FP-Tree'nin kökü.
        başlık_tablosu: Öğeler hakkında bilgi içeren başlık tablosu sözlüğü.

    Örnek:
    >>> veri_seti = [
    ...    ['A', 'B', 'C'],
    ...    ['A', 'C'],
    ...    ['A', 'B', 'E'],
    ...    ['A', 'B', 'C', 'E'],
    ...    ['B', 'E']
    ... ]
    >>> min_destek = 2
    >>> fp_agaci, baslik_tablosu = agac_olustur(veri_seti, min_destek)
    >>> fp_agaci
    AgacDugumu('Null Set', 1, None)
    >>> len(baslik_tablosu)
    4
    >>> baslik_tablosu["A"]
    [[4, None], AgacDugumu('A', 4, AgacDugumu('Null Set', 1, None))]
    >>> baslik_tablosu["E"][1]  # doctest: +NORMALIZE_WHITESPACE
    AgacDugumu('E', 1, AgacDugumu('B', 3, AgacDugumu('A', 4, AgacDugumu('Null Set', 1, None))))
    >>> sorted(baslik_tablosu)
    ['A', 'B', 'C', 'E']
    >>> fp_agaci.isim
    'Null Set'
    >>> sorted(fp_agaci.cocuklar)
    ['A', 'B']
    >>> fp_agaci.cocuklar['A'].isim
    'A'
    >>> sorted(fp_agaci.cocuklar['A'].cocuklar)
    ['B', 'C']
    """
    baslik_tablosu: dict = {}
    for islem in veri_seti:
        for oge in islem:
            baslik_tablosu[oge] = baslik_tablosu.get(oge, [0, None])
            baslik_tablosu[oge][0] += 1

    for k in list(baslik_tablosu):
        if baslik_tablosu[k][0] < min_destek:
            del baslik_tablosu[k]

    if not (sik_oge_kumesi := set(baslik_tablosu)):
        return AgacDugumu("Null Set", 1, None), {}

    for k in baslik_tablosu:
        baslik_tablosu[k] = [baslik_tablosu[k], None]

    fp_agaci = AgacDugumu("Null Set", 1, None)  # Kök düğüm için ebeveyn None
    for islem_kumesi in veri_seti:
        yerel_d = {
            oge: baslik_tablosu[oge][0] for oge in islem_kumesi if oge in sik_oge_kumesi
        }
        if yerel_d:
            sirali_ogeler = sorted(
                yerel_d.items(), key=lambda oge_bilgi: oge_bilgi[1], reverse=True
            )
            sirali_ogeler = [oge[0] for oge in sirali_ogeler]
            agaci_guncelle(sirali_ogeler, fp_agaci, baslik_tablosu, 1)

    return fp_agaci, baslik_tablosu


def agaci_guncelle(ogeler: list, ic_agac: AgacDugumu, baslik_tablosu: dict, sayi: int) -> None:
    """
    FP-Tree'yi bir işlemle güncelle.

    Args:
        ogeler: İşlemdeki öğeler listesi.
        ic_agac: FP-Tree'deki mevcut düğüm.
        baslik_tablosu: Öğeler hakkında bilgi içeren başlık tablosu sözlüğü.
        sayi: İşlemin sayısı.

    Örnek:
    >>> veri_seti = [
    ...    ['A', 'B', 'C'],
    ...    ['A', 'C'],
    ...    ['A', 'B', 'E'],
    ...    ['A', 'B', 'C', 'E'],
    ...    ['B', 'E']
    ... ]
    >>> min_destek = 2
    >>> fp_agaci, baslik_tablosu = agac_olustur(veri_seti, min_destek)
    >>> fp_agaci
    AgacDugumu('Null Set', 1, None)
    >>> islem = ['A', 'B', 'E']
    >>> agaci_guncelle(islem, fp_agaci, baslik_tablosu, 1)
    >>> fp_agaci
    AgacDugumu('Null Set', 1, None)
    >>> fp_agaci.cocuklar['A'].cocuklar['B'].cocuklar['E'].cocuklar
    {}
    >>> fp_agaci.cocuklar['A'].cocuklar['B'].cocuklar['E'].sayi
    2
    >>> baslik_tablosu['E'][1].isim
    'E'
    """
    if ogeler[0] in ic_agac.cocuklar:
        ic_agac.cocuklar[ogeler[0]].arttir(sayi)
    else:
        ic_agac.cocuklar[ogeler[0]] = AgacDugumu(ogeler[0], sayi, ic_agac)
        if baslik_tablosu[ogeler[0]][1] is None:
            baslik_tablosu[ogeler[0]][1] = ic_agac.cocuklar[ogeler[0]]
        else:
            basligi_guncelle(baslik_tablosu[ogeler[0]][1], ic_agac.cocuklar[ogeler[0]])
    if len(ogeler) > 1:
        agaci_guncelle(ogeler[1:], ic_agac.cocuklar[ogeler[0]], baslik_tablosu, sayi)


def basligi_guncelle(test_edilecek_dugum: AgacDugumu, hedef_dugum: AgacDugumu) -> AgacDugumu:
    """
    Başlık tablosunu bir düğüm bağlantısıyla güncelle.

    Args:
        test_edilecek_dugum: Başlık tablosunda güncellenecek düğüm.
        hedef_dugum: Bağlanacak düğüm.

    Örnek:
    >>> veri_seti = [
    ...    ['A', 'B', 'C'],
    ...    ['A', 'C'],
    ...    ['A', 'B', 'E'],
    ...    ['A', 'B', 'C', 'E'],
    ...    ['B', 'E']
    ... ]
    >>> min_destek = 2
    >>> fp_agaci, baslik_tablosu = agac_olustur(veri_seti, min_destek)
    >>> fp_agaci
    AgacDugumu('Null Set', 1, None)
    >>> dugum1 = AgacDugumu("A", 3, None)
    >>> dugum2 = AgacDugumu("B", 4, None)
    >>> dugum1
    AgacDugumu('A', 3, None)
    >>> dugum1 = basligi_guncelle(dugum1, dugum2)
    >>> dugum1
    AgacDugumu('A', 3, None)
    >>> dugum1.dugum_baglantisi
    AgacDugumu('B', 4, None)
    >>> dugum2.dugum_baglantisi is None
    True
    """
    while test_edilecek_dugum.dugum_baglantisi is not None:
        test_edilecek_dugum = test_edilecek_dugum.dugum_baglantisi
    if test_edilecek_dugum.dugum_baglantisi is None:
        test_edilecek_dugum.dugum_baglantisi = hedef_dugum
    # Güncellenmiş düğümü döndür
    return test_edilecek_dugum


def agaci_yuksel(yaprak_dugum: AgacDugumu, on_ek_yolu: list[str]) -> None:
    """
    Bir yaprak düğümden köküne kadar FP-Tree'yi yükselt, öğe adlarını ön ek yoluna ekle.

    Args:
        yaprak_dugum: Yükselmeye başlanacak yaprak düğüm.
        on_ek_yolu: Öğelerin yükselirken saklanacağı liste.

    Örnek:
    >>> veri_seti = [
    ...    ['A', 'B', 'C'],
    ...    ['A', 'C'],
    ...    ['A', 'B', 'E'],
    ...    ['A', 'B', 'C', 'E'],
    ...    ['B', 'E']
    ... ]
    >>> min_destek = 2
    >>> fp_agaci, baslik_tablosu = agac_olustur(veri_seti, min_destek)

    >>> yol = []
    >>> agaci_yuksel(fp_agaci.cocuklar['A'], yol)
    >>> yol # bir yaprak düğüm 'A' dan yükseliyor
    ['A']
    """
    if yaprak_dugum.ebeveyn is not None:
        on_ek_yolu.append(yaprak_dugum.isim)
        agaci_yuksel(yaprak_dugum.ebeveyn, on_ek_yolu)


def on_ek_yolu_bul(temel_oge: frozenset, agac_dugumu: AgacDugumu | None) -> dict:  # noqa: ARG001
    """
    Belirli bir temel öğe için koşullu örüntü tabanını bulun.

    Args:
        temel_oge: Koşullu örüntü tabanı bulunacak temel öğe.
        agac_dugumu: FP-Tree'deki düğüm.

    Örnek:
    >>> veri_seti = [
    ...    ['A', 'B', 'C'],
    ...    ['A', 'C'],
    ...    ['A', 'B', 'E'],
    ...    ['A', 'B', 'C', 'E'],
    ...    ['B', 'E']
    ... ]
    >>> min_destek = 2
    >>> fp_agaci, baslik_tablosu = agac_olustur(veri_seti, min_destek)
    >>> fp_agaci
    AgacDugumu('Null Set', 1, None)
    >>> len(baslik_tablosu)
    4
    >>> temel_oge = frozenset(['A'])
    >>> sorted(on_ek_yolu_bul(temel_oge, fp_agaci.cocuklar['A']))
    []
    """
    kosullu_ogeler: dict = {}
    while agac_dugumu is not None:
        on_ek_yolu: list = []
        agaci_yuksel(agac_dugumu, on_ek_yolu)
        if len(on_ek_yolu) > 1:
            kosullu_ogeler[frozenset(on_ek_yolu[1:])] = agac_dugumu.sayi
        agac_dugumu = agac_dugumu.dugum_baglantisi
    return kosullu_ogeler


def agaci_madencilik(
    ic_agac: AgacDugumu,  # noqa: ARG001
    baslik_tablosu: dict,
    min_destek: int,
    on_ek: set,
    sik_oge_listesi: list,
) -> None:
    """
    Sık kullanılan öğe kümelerini keşfetmek için FP-Tree'yi özyinelemeli olarak madencilik yapın.

    Args:
        ic_agac: Madencilik yapılacak FP-Tree.
        baslik_tablosu: Öğeler hakkında bilgi içeren başlık tablosu sözlüğü.
        min_destek: Minimum destek eşiği.
        on_ek: Madencilik yapılan öğe kümeleri için bir ön ek öğe kümesi.
        sik_oge_listesi: Sık kullanılan öğe kümelerini saklamak için bir liste.

    Örnek:
    >>> veri_seti = [
    ...    ['A', 'B', 'C'],
    ...    ['A', 'C'],
    ...    ['A', 'B', 'E'],
    ...    ['A', 'B', 'C', 'E'],
    ...    ['B', 'E']
    ... ]
    >>> min_destek = 2
    >>> fp_agaci, baslik_tablosu = agac_olustur(veri_seti, min_destek)
    >>> fp_agaci
    AgacDugumu('Null Set', 1, None)
    >>> sik_oge_kumeleri = []
    >>> agaci_madencilik(fp_agaci, baslik_tablosu, min_destek, set([]), sik_oge_kumeleri)
    >>> beklenen_ogeler = [{'C'}, {'C', 'A'}, {'E'}, {'A', 'E'}, {'E', 'B'}, {'A'}, {'B'}]
    >>> all(expected in sik_oge_kumeleri for expected in beklenen_ogeler)
    True
    """
    sirali_ogeler = sorted(baslik_tablosu.items(), key=lambda oge_bilgi: oge_bilgi[1][0])
    buyuk_l = [oge[0] for oge in sirali_ogeler]
    for temel_oge in buyuk_l:
        yeni_sik_kume = on_ek.copy()
        yeni_sik_kume.add(temel_oge)
        sik_oge_listesi.append(yeni_sik_kume)
        kosullu_oge_tabanlari = on_ek_yolu_bul(temel_oge, baslik_tablosu[temel_oge][1])
        kosullu_agac, kosullu_baslik = agac_olustur(list(kosullu_oge_tabanlari), min_destek)
        if kosullu_baslik is not None:
            # Başlık tablosundaki temel öğeyi güncelle
            baslik_tablosu[temel_oge][1] = basligi_guncelle(
                baslik_tablosu[temel_oge][1], kosullu_agac
            )
            agaci_madencilik(kosullu_agac, kosullu_baslik, min_destek, yeni_sik_kume, sik_oge_listesi)


if __name__ == "__main__":
    from doctest import testmod

    testmod()
    veri_seti: list[frozenset] = [
        frozenset(["ekmek", "sut", "peynir"]),
        frozenset(["ekmek", "sut"]),
        frozenset(["ekmek", "bebek_bezi"]),
        frozenset(["ekmek", "sut", "bebek_bezi"]),
        frozenset(["sut", "bebek_bezi"]),
        frozenset(["sut", "peynir"]),
        frozenset(["bebek_bezi", "peynir"]),
        frozenset(["ekmek", "sut", "peynir", "bebek_bezi"]),
    ]
    print(f"{len(veri_seti) = }")
    fp_agaci, baslik_tablosu = agac_olustur(veri_seti, min_destek=3)
    print(f"{fp_agaci = }")
    print(f"{len(baslik_tablosu) = }")
    sik_ogeler: list = []
    agaci_madencilik(fp_agaci, baslik_tablosu, 3, set(), sik_ogeler)
    print(f"{sik_ogeler = }")
