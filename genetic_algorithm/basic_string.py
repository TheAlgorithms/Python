"""
Genetik algoritmanın 4 aşamasının nasıl çalıştığını göstermek için basit çok iş parçacıklı algoritma
(Değerlendirme, Seçim, Çaprazlama ve Mutasyon)
https://en.wikipedia.org/wiki/Genetic_algorithm

Produced By K. Umut Araz
"""

from __future__ import annotations

import random

# Popülasyonun maksimum boyutu. Daha büyük olabilir ancak daha fazla bellek gerektirir.
N_POPULATION = 200
# Her evrim neslinde seçilen eleman sayısı. Seçim, o neslin en iyisinden en kötüsüne doğru yapılır ve N_POPULATION'dan küçük olmalıdır.
N_SELECTED = 50
# Bir neslin bir elemanının mutasyona uğrama olasılığı, genlerinden birini değiştirme olasılığı.
# Bu, evrim sırasında tüm genlerin kullanılmasını garanti eder.
MUTATION_PROBABILITY = 0.4
# Algoritmanın gerektirdiği rastgeleliği artırmak için sadece bir tohum.
random.seed(random.randint(0, 1000))


def değerlendir(eleman: str, ana_hedef: str) -> tuple[str, float]:
    """
    Elemanın hedefle ne kadar benzer olduğunu, sadece doğru pozisyondaki her karakteri sayarak değerlendir
    >>> değerlendir("Helxo Worlx", "Hello World")
    ('Helxo Worlx', 9.0)
    """
    puan = len([g for pozisyon, g in enumerate(eleman) if g == ana_hedef[pozisyon]])
    return (eleman, float(puan))


def çaprazla(ebeveyn_1: str, ebeveyn_2: str) -> tuple[str, str]:
    """
    İki dizeyi rastgele bir noktada dilimleyip birleştir.
    >>> random.seed(42)
    >>> çaprazla("123456", "abcdef")
    ('12345f', 'abcde6')
    """
    rastgele_dilim = random.randint(0, len(ebeveyn_1) - 1)
    çocuk_1 = ebeveyn_1[:rastgele_dilim] + ebeveyn_2[rastgele_dilim:]
    çocuk_2 = ebeveyn_2[:rastgele_dilim] + ebeveyn_1[rastgele_dilim:]
    return (çocuk_1, çocuk_2)


def mutasyon(çocuk: str, genler: list[str]) -> str:
    """
    Bir çocuğun rastgele bir genini listedeki başka bir genle değiştir.
    >>> random.seed(123)
    >>> mutasyon("123456", list("ABCDEF"))
    '12345A'
    """
    çocuk_listesi = list(çocuk)
    if random.uniform(0, 1) < MUTATION_PROBABILITY:
        çocuk_listesi[random.randint(0, len(çocuk)) - 1] = random.choice(genler)
    return "".join(çocuk_listesi)


# Yeni bir popülasyon seç, çaprazla ve mutasyona uğrat.
def seç(
    ebeveyn_1: tuple[str, float],
    popülasyon_puanı: list[tuple[str, float]],
    genler: list[str],
) -> list[str]:
    """
    İkinci ebeveyni seç ve yeni popülasyon oluştur

    >>> random.seed(42)
    >>> ebeveyn_1 = ("123456", 8.0)
    >>> popülasyon_puanı = [("abcdef", 4.0), ("ghijkl", 5.0), ("mnopqr", 7.0)]
    >>> genler = list("ABCDEF")
    >>> çocuk_sayısı = int(min(ebeveyn_1[1] + 1, 10))
    >>> popülasyon = []
    >>> for _ in range(çocuk_sayısı):
    ...     ebeveyn_2 = popülasyon_puanı[random.randrange(len(popülasyon_puanı))][0]
    ...     çocuk_1, çocuk_2 = çaprazla(ebeveyn_1[0], ebeveyn_2)
    ...     popülasyon.extend((mutasyon(çocuk_1, genler), mutasyon(çocuk_2, genler)))
    >>> len(popülasyon) == (int(ebeveyn_1[1]) + 1) * 2
    True
    """
    pop = []
    # Uygunluk puanına orantılı olarak daha fazla çocuk üret.
    çocuk_sayısı = int(ebeveyn_1[1] * 100) + 1
    çocuk_sayısı = 10 if çocuk_sayısı >= 10 else çocuk_sayısı
    for _ in range(çocuk_sayısı):
        ebeveyn_2 = popülasyon_puanı[random.randint(0, N_SELECTED)][0]

        çocuk_1, çocuk_2 = çaprazla(ebeveyn_1[0], ebeveyn_2)
        # Yeni dizeyi popülasyon listesine ekle.
        pop.append(mutasyon(çocuk_1, genler))
        pop.append(mutasyon(çocuk_2, genler))
    return pop


def temel(hedef: str, genler: list[str], debug: bool = True) -> tuple[int, int, str]:
    """
    Hedefin, genler değişkeninin içindeki genler dışında gen içermediğini doğrula.

    >>> from string import ascii_lowercase
    >>> temel("doctest", ascii_lowercase, debug=False)[2]
    'doctest'
    >>> genler = list(ascii_lowercase)
    >>> genler.remove("e")
    >>> temel("test", genler)
    Traceback (most recent call last):
        ...
    ValueError: ['e'] is not in genes list, evolution cannot converge
    >>> genler.remove("s")
    >>> temel("test", genler)
    Traceback (most recent call last):
        ...
    ValueError: ['e', 's'] is not in genes list, evolution cannot converge
    >>> genler.remove("t")
    >>> temel("test", genler)
    Traceback (most recent call last):
        ...
    ValueError: ['e', 's', 't'] is not in genes list, evolution cannot converge
    """

    # N_POPULATION'ın N_SELECTED'dan büyük olduğunu doğrula
    if N_POPULATION < N_SELECTED:
        msg = f"{N_POPULATION} must be bigger than {N_SELECTED}"
        raise ValueError(msg)
    # Hedefin, genler değişkeninin içindeki genler dışında gen içermediğini doğrula.
    gen_listesinde_olmayanlar = sorted({c for c in hedef if c not in genler})
    if gen_listesinde_olmayanlar:
        msg = f"{gen_listesinde_olmayanlar} is not in genes list, evolution cannot converge"
        raise ValueError(msg)

    # Rastgele başlangıç popülasyonu oluştur.
    popülasyon = []
    for _ in range(N_POPULATION):
        popülasyon.append("".join([random.choice(genler) for i in range(len(hedef))]))

    # Algoritmanın ne yaptığını bilmek için sadece bazı günlükler.
    nesil, toplam_popülasyon = 0, 0

    # Bu döngü, hedefimiz için mükemmel bir eşleşme bulduğumuzda sona erecek.
    while True:
        nesil += 1
        toplam_popülasyon += len(popülasyon)

        # Rastgele popülasyon oluşturuldu. Şimdi değerlendirme zamanı.

        # Biraz eşzamanlılık eklemek her şeyi daha hızlı hale getirebilir,
        #
        # import concurrent.futures
        # popülasyon_puanı: list[tuple[str, float]] = []
        # with concurrent.futures.ThreadPoolExecutor(
        #                                   max_workers=NUM_WORKERS) as executor:
        #     futures = {executor.submit(değerlendir, eleman) for eleman in popülasyon}
        #     concurrent.futures.wait(futures)
        #     popülasyon_puanı = [eleman.result() for eleman in futures]
        #
        # ancak bu kadar basit bir algoritma ile muhtemelen daha yavaş olacaktır.
        # Sadece popülasyon içindeki her eleman için değerlendir'i çağırmamız gerekiyor.
        popülasyon_puanı = [değerlendir(eleman, hedef) for eleman in popülasyon]

        # Eşleşen bir evrim olup olmadığını kontrol et.
        popülasyon_puanı = sorted(popülasyon_puanı, key=lambda x: x[1], reverse=True)
        if popülasyon_puanı[0][0] == hedef:
            return (nesil, toplam_popülasyon, popülasyon_puanı[0][0])

        # Her 10 nesilde bir en iyi sonucu yazdır.
        # Algoritmanın çalıştığını bilmek için.
        if debug and nesil % 10 == 0:
            print(
                f"\nNesil: {nesil}"
                f"\nToplam Popülasyon:{toplam_popülasyon}"
                f"\nEn iyi puan: {popülasyon_puanı[0][1]}"
                f"\nEn iyi dize: {popülasyon_puanı[0][0]}"
            )

        # Eski popülasyonu temizle, en iyi evrimlerden bazılarını sakla.
        # Bu, evrimin gerilemesini önler.
        en_iyi_popülasyon = popülasyon[: int(N_POPULATION / 3)]
        popülasyon.clear()
        popülasyon.extend(en_iyi_popülasyon)
        # Popülasyon puanını 0 ile 1 arasında normalize et.
        popülasyon_puanı = [
            (eleman, puan / len(hedef)) for eleman, puan in popülasyon_puanı
        ]

        # Bu seçimdir
        for i in range(N_SELECTED):
            popülasyon.extend(seç(popülasyon_puanı[int(i)], popülasyon_puanı, genler))
            # Popülasyonun maksimum değere ulaşıp ulaşmadığını kontrol et ve eğer öyleyse,
            # döngüyü kır. Bu kontrol devre dışı bırakılırsa, algoritma
            # büyük dizeleri hesaplamak sonsuza kadar sürecektir, ancak küçük dizeleri de
            # çok daha az nesilde hesaplayacaktır.
            if len(popülasyon) > N_POPULATION:
                break


if __name__ == "__main__":
    hedef_dize = (
        "Bu, bir dizeyi değerlendirmek, birleştirmek, evrimleştirmek ve mutasyona uğratmak için bir genetik algoritmadır!"
    )
    genler_listesi = list(
        " ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklm"
        "nopqrstuvwxyz.,;!?+-*#@^'èéòà€ù=)(&%$£/\\"
    )
    nesil, popülasyon, hedef = temel(hedef_dize, genler_listesi)
    print(
        f"\nNesil: {nesil}\nToplam Popülasyon: {popülasyon}\nHedef: {hedef}"
    )
