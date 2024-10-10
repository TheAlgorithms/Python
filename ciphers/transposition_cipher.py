import math

"""
Kriptografide, TRANSPOZİSYON şifrelemesi, düz metin pozisyonlarının belirli bir sayıda (anahtar tarafından belirlenen) kaydırıldığı bir şifreleme yöntemidir. Bu işlem, permütasyon metni olarak bilinen şifreli metni oluşturur. Aşağıda gösterilen transpozisyon şifreleme türü ROUTE şifresidir.

Kodu düzenle, çıkarman gereken yerleri çıkar eklemen gereken yerleri ekle, mantıklı ve anlaşılabilir bir şekilde türkçeye çevir 
"""

def main() -> None:
    mesaj = input("Mesajı girin: ").strip()
    if not mesaj:
        print("Mesaj boş olamaz.")
        return

    try:
        anahtar = int(input(f"Anahtar girin [2-{len(mesaj) - 1}]: "))
        if anahtar < 2 or anahtar >= len(mesaj):
            raise ValueError
    except ValueError:
        print("Geçersiz anahtar. Lütfen belirtilen aralıkta bir tam sayı girin.")
        return

    mod = input("Şifreleme/Şifre Çözme [e/d]: ").strip().lower()
    if mod not in ['e', 'd']:
        print("Geçersiz mod. Lütfen 'e' ile şifreleme veya 'd' ile şifre çözme girin.")
        return

    if mod == "e":
        metin = encrypt_message(anahtar, mesaj)
    else:
        metin = decrypt_message(anahtar, mesaj)

    # Sonunda boşlukları tanımlamak için boru sembolü ekleniyor.
    print(f"Çıktı:\n{metin + '|'}")

def encrypt_message(anahtar: int, mesaj: str) -> str:
    """
    >>> encrypt_message(6, 'Harshil Darji')
    'Hlia rDsahrij'
    """
    sifreli_metin = [""] * anahtar
    for sutun in range(anahtar):
        işaretçi = sutun
        while işaretçi < len(mesaj):
            sifreli_metin[sutun] += mesaj[işaretçi]
            işaretçi += anahtar
    return "".join(sifreli_metin)

def decrypt_message(anahtar: int, mesaj: str) -> str:
    """
    >>> decrypt_message(6, 'Hlia rDsahrij')
    'Harshil Darji'
    """
    sutun_sayisi = math.ceil(len(mesaj) / anahtar)
    satir_sayisi = anahtar
    gölgeli_kutular = (sutun_sayisi * satir_sayisi) - len(mesaj)
    düz_metin = [""] * sutun_sayisi
    sutun = 0
    satir = 0

    for sembol in mesaj:
        düz_metin[sutun] += sembol
        sutun += 1

        if (
            (sutun == sutun_sayisi)
            or (sutun == sutun_sayisi - 1)
            and (satir >= satir_sayisi - gölgeli_kutular)
        ):
            sutun = 0
            satir += 1

    return "".join(düz_metin)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()