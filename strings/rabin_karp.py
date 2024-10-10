# Alfabedeki karakter sayısı
alfabe_boyutu = 256
# Bir dizenin hash'ini almak için modül
modül = 1000003

#Organiser: K. Umut Araz


def rabin_karp(desen: str, metin: str) -> bool:
    """
    Rabin-Karp Algoritması, bir metin içinde bir deseni bulmak için kullanılır.
    Zaman karmaşıklığı O(nm) olup, birden fazla desenle kullanıldığında en verimli
    hale gelir çünkü önceden hesaplanmış hash'ler ile metnin bir bölümünün
    herhangi bir desenle eşleşip eşleşmediğini O(1) sürede kontrol edebilir.

    Bu, yalnızca bir deseni aradığımız basit bir versiyonudur,
    ancak çoklu desen aramak için kolayca değiştirilebilir.

    1) Desenin hash'ini hesapla

    2) Metin üzerinde, desene eşit uzunlukta bir pencere ile
       bir karakter bir seferde geçerek ilerle
       Pencere içindeki metnin hash'ini hesapla ve bunu desenin hash'i ile karşılaştır.
       Sadece hash'ler eşleşirse eşitliği test et.
    """
    desen_uzunluğu = len(desen)
    metin_uzunluğu = len(metin)
    if desen_uzunluğu > metin_uzunluğu:
        return False

    desen_hash = 0
    metin_hash = 0
    modül_gücü = 1

    # Desenin ve metin alt dizisinin hash'ini hesaplama
    for i in range(desen_uzunluğu):
        desen_hash = (ord(desen[i]) + desen_hash * alfabe_boyutu) % modül
        metin_hash = (ord(metin[i]) + metin_hash * alfabe_boyutu) % modül
        if i == desen_uzunluğu - 1:
            continue
        modül_gücü = (modül_gücü * alfabe_boyutu) % modül

    for i in range(metin_uzunluğu - desen_uzunluğu + 1):
        if metin_hash == desen_hash and metin[i : i + desen_uzunluğu] == desen:
            return True
        if i == metin_uzunluğu - desen_uzunluğu:
            continue
        # Rolling hash hesaplama
        metin_hash = (
            (metin_hash - ord(metin[i]) * modül_gücü) * alfabe_boyutu
            + ord(metin[i + desen_uzunluğu])
        ) % modül
    return False


def test_rabin_karp() -> None:
    """
    >>> test_rabin_karp()
    Başarılı.
    """
    # Test 1)
    desen = "abc1abc12"
    metin1 = "alskfjaldsabc1abc1abc12k23adsfabcabc"
    metin2 = "alskfjaldsk23adsfabcabc"
    assert rabin_karp(desen, metin1)
    assert not rabin_karp(desen, metin2)

    # Test 2)
    desen = "ABABX"
    metin = "ABABZABABYABABX"
    assert rabin_karp(desen, metin)

    # Test 3)
    desen = "AAAB"
    metin = "ABAAAAAB"
    assert rabin_karp(desen, metin)

    # Test 4)
    desen = "abcdabcy"
    metin = "abcxabcdabxabcdabcdabcy"
    assert rabin_karp(desen, metin)

    # Test 5)
    desen = "Lü"
    metin = "Lüsai"
    assert rabin_karp(desen, metin)
    desen = "Lue"
    assert not rabin_karp(desen, metin)
    print("Başarılı.")


if __name__ == "__main__":
    test_rabin_karp()
