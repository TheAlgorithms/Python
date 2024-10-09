"""
Bu algoritma, sdbm (ndbm'nin kamu malı yeniden uygulaması) veritabanı kütüphanesi için oluşturulmuştur.
Bitleri karıştırmada iyi olduğu, anahtarların daha iyi dağılımına ve daha az bölünmeye neden olduğu bulunmuştur.
Ayrıca, iyi dağılıma sahip genel bir karma işlevi olduğu ortaya çıkmıştır.
Gerçek işlev (sözde kod) şudur:
    for i in i..len(str):
        hash(i) = hash(i - 1) * 65599 + str[i];

Aşağıda yer alan, gawk'ta kullanılan daha hızlı versiyondur. [daha da hızlı bir duff-device versiyonu vardır]
65599 sihirli sabiti, farklı sabitlerle deney yaparken rastgele seçilmiştir.
Aslında bir asal sayıdır.
Bu, berkeley db (sleepycat'e bakın) ve başka yerlerde kullanılan algoritmalardan biridir.

kaynak: http://www.cse.yorku.ca/~oz/hash.html
"""


def sdbm(duz_metin: str) -> int:
    """
    Bu fonksiyon sdbm hash'ini uygular, kullanımı kolaydır, bitleri karıştırmada harikadır.
    Verilen stringdeki her karakteri iterasyonla dolaşır ve her birine fonksiyonu uygular.

    >>> sdbm('Algoritmalar')
    1462174910723540325254304520539387479031000036

    >>> sdbm('bitleri karıştır')
    730247649148944819640658295400555317318720608290373040936089
    """
    hash_degeri = 0
    for duz_karakter in duz_metin:
        hash_degeri = (
            ord(duz_karakter) + (hash_degeri << 6) + (hash_degeri << 16) - hash_degeri
        )
    return hash_degeri
