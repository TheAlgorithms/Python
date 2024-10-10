from __future__ import annotations

from string import ascii_letters


"""
Organiser: K. Umut Araz

"""

def şifrele(girdi: str, anahtar: int, alfabe: str | None = None) -> str:
    """
    şifrele
    =======
    Verilen bir dizeyi Sezar şifresi ile şifreler ve şifrelenmiş mesajı döndürür.

    Parametreler:
    -----------
    *   girdi: şifrelenmesi gereken düz metin
    *   anahtar: mesajı kaydırmak için kullanılan harf sayısı

    Opsiyonel:
    *   alfabe (None): şifreleme için kullanılan alfabe, belirtilmezse
        standart İngiliz alfabesi (büyük ve küçük harfler) kullanılır.

    Döndürür:
    *   Şifrelenmiş metni içeren bir dize

    Sezar şifresi hakkında daha fazla bilgi
    =========================
    Sezar şifresi, Julius Caesar'ın askeri mesajlarını göndermek için kullandığı bir şifreleme yöntemidir.
    Bu, düz metindeki her karakterin belirli bir sayı kadar kaydırıldığı basit bir yer değiştirme şifresidir.

    Örnek:
    Aşağıdaki mesajımız olsun:
    "Merhaba, kaptan"

    Ve alfabemiz büyük ve küçük harflerden oluşsun:
    "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    Ve kaydırmamız "2" olsun.

    Mesajı bir harf bir harf şifreleyebiliriz. "M" "O" olur, çünkü "O" iki harf ileri, ve devam ederiz.
    Eğer kaydırma çok büyükse veya harf alfabede sona gelirse, baştan başlarız
    ("Z" "a" ve sonra "b" olur).

    Son mesajımız "Opjctc, mcvqpc" olur.

    Daha fazla okuma
    ===============
    *   https://en.m.wikipedia.org/wiki/Caesar_cipher

    Doctestler
    ========
    >>> şifrele('Hızlı kahverengi tilki, tembel köpeği atlar.', 8)
    'pçqvç qöqvçqvç qöqvç, vçqvçqvç qöqvçqvç.'

    >>> şifrele('Büyük bir anahtar', 8000)
    's nWjq dSjYW cWq'

    >>> şifrele('küçük harf alfabesi', 5, 'abcdefghijklmnopqrstuvwxyz')
    'f qtbjwhfxj fqumfgjy'
    """
    # Varsayılan alfabe büyük ve küçük İngiliz harfleri
    alfabe = alfabe or ascii_letters

    # Sonuç dizesi
    sonuç = ""

    for karakter in girdi:
        if karakter not in alfabe:
            # Alfabe içinde değilse şifrelemeden ekle
            sonuç += karakter
        else:
            # Yeni anahtarın indeksini al ve çok büyük olmadığından emin ol
            yeni_anahtar = (alfabe.index(karakter) + anahtar) % len(alfabe)

            # Şifrelenmiş karakteri sonuca ekle
            sonuç += alfabe[yeni_anahtar]

    return sonuç


def çöz(girdi: str, anahtar: int, alfabe: str | None = None) -> str:
    """
    çöz
    =======
    Verilen bir şifreli metni çözer ve düz metni döndürür.

    Parametreler:
    -----------
    *   girdi: çözülmesi gereken şifreli metin
    *   anahtar: mesajı geriye kaydırmak için kullanılan harf sayısı

    Opsiyonel:
    *   alfabe (None): şifreyi çözmek için kullanılan alfabe, belirtilmezse
        standart İngiliz alfabesi (büyük ve küçük harfler) kullanılır.

    Döndürür:
    *   Çözülmüş düz metni içeren bir dize

    Sezar şifresi hakkında daha fazla bilgi
    =========================
    Sezar şifresi, Julius Caesar'ın askeri mesajlarını göndermek için kullandığı bir şifreleme yöntemidir.
    Bu, düz metindeki her karakterin belirli bir sayı kadar kaydırıldığı basit bir yer değiştirme şifresidir.
    Burada, şifre çözmeye odaklanacağız.

    Örnek:
    Aşağıdaki şifreli metnimiz olsun:
    "Opjctc, mcvqpc"

    Ve alfabemiz büyük ve küçük harflerden oluşsun:
    "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    Ve kaydırmamız "2" olsun.

    Mesajı çözmek için, şifreleme ile aynı şeyi yaparız, ama tersine.
    İlk harf "O" "M" olur (unutmayın: çözüyoruz) çünkü "M" "O"dan iki harf geridedir.
    Devam ederiz. "a" harfi alfabede sona geri döner ve "Z" veya "Y" olur.

    Son mesajımız "Merhaba, kaptan" olur.

    Daha fazla okuma
    ===============
    *   https://en.m.wikipedia.org/wiki/Caesar_cipher

    Doctestler
    ========
    >>> çöz('pçqvç qöqvçqvç qöqvç, vçqvçqvç qöqvçqvç.', 8)
    'Hızlı kahverengi tilki, tembel köpeği atlar.'

    >>> çöz('s nWjq dSjYW cWq', 8000)
    'Büyük bir anahtar'

    >>> çöz('f qtbjwhfxj fqumfgjy', 5, 'abcdefghijklmnopqrstuvwxyz')
    'küçük harf alfabesi'
    """
    # Çözme modunu açmak için anahtarı negatif yap
    anahtar *= -1

    return şifrele(girdi, anahtar, alfabe)


def kaba_güç(girdi: str, alfabe: str | None = None) -> dict[int, str]:
    """
    kaba_güç
    ===========
    Tüm olası anahtar kombinasyonlarını ve çözülen dizeleri bir sözlük şeklinde döndürür.

    Parametreler:
    -----------
    *   girdi: kaba güç sırasında kullanılacak şifreli metin

    Opsiyonel:
    *   alfabe: (None): şifreyi çözmek için kullanılan alfabe, belirtilmezse
        standart İngiliz alfabesi (büyük ve küçük harfler) kullanılır.

    Kaba güç hakkında daha fazla bilgi
    ======================
    Kaba güç, bir kişinin bir mesajı veya şifreyi ele geçirmesi, anahtarı bilmeden
    her bir kombinasyonu denemesi anlamına gelir. Bu, Sezar şifresi ile kolaydır
    çünkü sadece alfabedeki tüm harfler vardır. Şifre ne kadar karmaşık olursa,
    kaba güç uygulamak o kadar fazla zaman alır.

    Örnek:
    5 harfli bir alfabemiz (abcde) olduğunu varsayalım ve aşağıdaki mesajı ele geçirdik:

    "dbc"

    O zaman her kombinasyonu yazabiliriz:
    ecd... ve devam ederiz, mantıklı bir kombinasyona ulaşana kadar:
    "cab"

    Daha fazla okuma
    ===============
    *   https://en.wikipedia.org/wiki/Brute_force

    Doctestler
    ========
    >>> kaba_güç("jFyuMy xIH'N vLONy zILwy Gy!")[20]
    "Lütfen beni kaba güçle çözmeyin!"

    >>> kaba_güç(1)
    Traceback (most recent call last):
    TypeError: 'int' nesnesi yineleyici değil
    """
    # Varsayılan alfabe büyük ve küçük İngiliz harfleri
    alfabe = alfabe or ascii_letters

    # Tüm kombinasyonların verilerini saklamak için
    kaba_güç_verisi = {}

    # Her kombinasyonu döngüye al
    for anahtar in range(1, len(alfabe) + 1):
        # Mesajı çöz ve sonucu veriye kaydet
        kaba_güç_verisi[anahtar] = çöz(girdi, anahtar, alfabe)

    return kaba_güç_verisi


if __name__ == "__main__":
    while True:
        print(f'\n{"-" * 10}\n Menü\n{"-" * 10}')
        print(*["1. Şifrele", "2. Çöz", "3. Kaba Güç", "4. Çıkış"], sep="\n")

        # Kullanıcıdan girdi al
        seçim = input("\nNe yapmak istersiniz?: ").strip() or "4"

        # Kullanıcının seçimine göre fonksiyonları çalıştır
        if seçim not in ("1", "2", "3", "4"):
            print("Geçersiz seçim, lütfen geçerli bir seçim yapın.")
        elif seçim == "1":
            girdi = input("Şifrelenecek dizeyi girin: ")
            anahtar = int(input("Kaydırma değerini girin: ").strip())

            print(şifrele(girdi, anahtar))
        elif seçim == "2":
            girdi = input("Çözülecek dizeyi girin: ")
            anahtar = int(input("Kaydırma değerini girin: ").strip())

            print(çöz(girdi, anahtar))
        elif seçim == "3":
            girdi = input("Çözülecek dizeyi girin: ")
            kaba_güç_verisi = kaba_güç(girdi)

            for anahtar, değer in kaba_güç_verisi.items():
                print(f"Anahtar: {anahtar} | Mesaj: {değer}")

        elif seçim == "4":
            print("Hoşça kal.")
            break
