"""Basit bir kaos makinesi örneği"""

# Kaos Makinesi (K, t, m)
K = [0.33, 0.44, 0.55, 0.44, 0.33]
t = 3
m = 5

# Tampon Alanı (Parametreler Alanı ile)
tampon_alani: list[float] = []
parametreler_alani: list[float] = []

# Makine Zamanı
makine_zamani = 0


def ekle(tohum):
    global tampon_alani, parametreler_alani, makine_zamani, K, m, t

    # Dinamik Sistemlerin Seçilmesi (Hepsi)
    for anahtar, deger in enumerate(tampon_alani):
        # Evrim Parametresi
        e = float(tohum / deger)

        # Kontrol Teorisi: Yörünge Değişimi
        deger = (tampon_alani[(anahtar + 1) % m] + e) % 1

        # Kontrol Teorisi: Trajektori Değişimi
        r = (parametreler_alani[anahtar] + e) % 1 + 3

        # Modifikasyon (Geçiş Fonksiyonu) - Sıçramalar
        tampon_alani[anahtar] = round(float(r * deger * (1 - deger)), 10)
        parametreler_alani[anahtar] = r  # Parametreler Alanına Kaydetme

    # Lojistik Harita
    assert max(tampon_alani) < 1
    assert max(parametreler_alani) < 4

    # Makine Zamanı
    makine_zamani += 1


def cek():
    global tampon_alani, parametreler_alani, makine_zamani, K, m, t

    # PRNG (George Marsaglia tarafından Xorshift)
    def xorshift(x, y):
        x ^= y >> 13
        y ^= x << 17
        x ^= y >> 5
        return x

    # Dinamik Sistemlerin Seçilmesi (Artış)
    anahtar = makine_zamani % m

    # Evrim (Zaman Uzunluğu)
    for _ in range(t):
        # Değişkenler (Pozisyon + Parametreler)
        r = parametreler_alani[anahtar]
        deger = tampon_alani[anahtar]

        # Modifikasyon (Geçiş Fonksiyonu) - Akış
        tampon_alani[anahtar] = round(float(r * deger * (1 - deger)), 10)
        parametreler_alani[anahtar] = (makine_zamani * 0.01 + r * 1.01) % 1 + 3

    # Kaotik Verilerin Seçilmesi
    x = int(tampon_alani[(anahtar + 2) % m] * (10**10))
    y = int(tampon_alani[(anahtar - 2) % m] * (10**10))

    # Makine Zamanı
    makine_zamani += 1

    return xorshift(x, y) % 0xFFFFFFFF


def sifirla():
    global tampon_alani, parametreler_alani, makine_zamani, K, m, t

    tampon_alani = K
    parametreler_alani = [0] * m
    makine_zamani = 0


if __name__ == "__main__":
    # Başlatma
    sifirla()

    # Veri Ekleme (Girdi)
    import random

    mesaj = random.sample(range(0xFFFFFFFF), 100)
    for parca in mesaj:
        ekle(parca)

    # Kontrol için
    giris = ""

    # Veri Çekme (Çıktı)
    while giris not in ("e", "E"):
        print(f"{format(cek(), '#04x')}")
        print(tampon_alani)
        print(parametreler_alani)
        giris = input("(e)çıkış? ").strip()
