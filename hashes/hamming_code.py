# Yazar: João Gustavo A. Amorim & Gabriel Kunz
# Katkı: K. Umut Araz
# Yazar e-posta: joaogustavoamorim@gmail.com ve gabriel-kunz@uergs.edu.br
# Kodlama tarihi: Nisan 2019
# Katkıda Bulunma tarihi : 2024-10-07

"""
* Bu kod Hamming kodunu uygular:
    https://en.wikipedia.org/wiki/Hamming_code - Telekomünikasyonda,
Hamming kodları, doğrusal hata düzeltme kodları ailesidir. Hamming
kodları, iki bit hatasını tespit edebilir veya bir bit hatasını
düzeltir. Basit parite kodu ise hataları düzeltemez ve yalnızca tek
sayıda hatayı tespit edebilir. Hamming kodları mükemmel kodlardır,
yani blok uzunlukları ve minimum üç mesafeleri ile mümkün olan en yüksek
oranı elde ederler.

* Uygulanan kod şunlardan oluşur:
    * Mesajı kodlamaktan sorumlu bir fonksiyon (emitter_converter)
        * Kodlanmış mesajı döndürür
    * Mesajı çözmekten sorumlu bir fonksiyon (receptor_converter)
        * Kodlanmış mesajı ve veri bütünlüğü onayını döndürür

* Kullanım şekli:
        Kullanmak için, mesaja kaç tane parite biti (sizePari)
    eklemek istediğinizi belirtmelisiniz.
        (Test amaçlı) bir bitin hata olarak ayarlanmasını seçmek istenir.
    Bu, kodun doğru çalışıp çalışmadığını kontrol etmek içindir.
        Son olarak, kodlanması istenen mesaj/kelime değişkeni
    (text).

* Nasıl çalışır:
        Değişkenlerin tanımlanması (sizePari, be, text)

        Mesajı/kelimeyi (text) text_to_bits fonksiyonunu kullanarak
    ikiliye çevirir
        Mesajı Hamming kodlama kurallarını kullanarak kodlar
        Mesajı Hamming kodlama kurallarını kullanarak çözer
        Orijinal mesajı, kodlanmış mesajı ve
    çözülmüş mesajı yazdırır

        Kodlanmış metin değişkeninde bir hata zorlar
        Hata zorlanmış mesajı çözer
        Orijinal mesajı, kodlanmış mesajı, bit değiştirilmiş
    mesajı ve çözülmüş mesajı yazdırır
"""

# İthalatlar
import numpy as np


# İkili dönüşüm fonksiyonları--------------------------------------
def text_to_bits(text, encoding="utf-8", errors="surrogatepass"):
    """
    >>> text_to_bits("msg")
    '011011010111001101100111'
    """
    bits = bin(int.from_bytes(text.encode(encoding, errors), "big"))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))


def text_from_bits(bits, encoding="utf-8", errors="surrogatepass"):
    """
    >>> text_from_bits('011011010111001101100111')
    'msg'
    """
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, "big").decode(encoding, errors) or "\0"


# Hamming kodu fonksiyonları-------------------------------------------
def emitter_converter(size_par, data):
    """
    :param size_par: Mesajın kaç tane parite biti içermesi gerektiği
    :param data:  Bilgi bitleri
    :return: Güvenilmez ortam tarafından iletilecek mesaj
            - Parite bitleri ile birleştirilmiş bilgi bitleri

    >>> emitter_converter(4, "101010111111")
    ['1', '1', '1', '1', '0', '1', '0', '0', '1', '0', '1', '1', '1', '1', '1', '1']
    >>> emitter_converter(5, "101010111111")
    Traceback (most recent call last):
        ...
    ValueError: parite boyutu veri boyutuyla eşleşmiyor
    """
    if size_par + len(data) <= 2**size_par - (len(data) - 1):
        raise ValueError("parite boyutu veri boyutuyla eşleşmiyor")

    data_out = []
    parity = []
    bin_pos = [bin(x)[2:] for x in range(1, size_par + len(data) + 1)]

    # Çıktı verisinin boyutuna göre sıralanmış bilgi verisi
    data_ord = []
    # Veri pozisyon şablonu + parite
    data_out_gab = []
    # Parite bit sayacı
    qtd_bp = 0
    # Veri bitlerinin pozisyon sayacı
    cont_data = 0

    for x in range(1, size_par + len(data) + 1):
        # Bit pozisyonlarının bir şablonunu oluşturur - hangi bitlerin bilgi,
        # hangilerinin parite olması gerektiğini belirler
        if qtd_bp < size_par:
            if (np.log(x) / np.log(2)).is_integer():
                data_out_gab.append("P")
                qtd_bp = qtd_bp + 1
            else:
                data_out_gab.append("D")
        else:
            data_out_gab.append("D")

        # Veriyi yeni çıktı boyutuna göre sıralar
        if data_out_gab[-1] == "D":
            data_ord.append(data[cont_data])
            cont_data += 1
        else:
            data_ord.append(None)

    # Parite hesaplar
    qtd_bp = 0  # parite bit sayacı
    for bp in range(1, size_par + 1):
        # Belirli bir parite için bir bit sayacı
        cont_bo = 0
        # Döngü okuma kontrolü için sayaç
        for cont_loop, x in enumerate(data_ord):
            if x is not None:
                try:
                    aux = (bin_pos[cont_loop])[-1 * (bp)]
                except IndexError:
                    aux = "0"
                if aux == "1" and x == "1":
                    cont_bo += 1
        parity.append(cont_bo % 2)

        qtd_bp += 1

    # Mesajı oluştur
    cont_bp = 0  # parite bit sayacı
    for x in range(size_par + len(data)):
        if data_ord[x] is None:
            data_out.append(str(parity[cont_bp]))
            cont_bp += 1
        else:
            data_out.append(data_ord[x])

    return data_out


def receptor_converter(size_par, data):
    """
    >>> receptor_converter(4, "1111010010111111")
    (['1', '0', '1', '0', '1', '0', '1', '1', '1', '1', '1', '1'], True)
    """
    # Veri pozisyon şablonu + parite
    data_out_gab = []
    # Parite bit sayacı
    qtd_bp = 0
    # Veri bit okuma sayacı
    cont_data = 0
    # Alınan parite listesi
    parity_received = []
    data_output = []

    for i, item in enumerate(data, 1):
        # Bit pozisyonlarının bir şablonunu oluşturur - hangi bitlerin bilgi,
        # hangilerinin parite olması gerektiğini belirler
        if qtd_bp < size_par and (np.log(i) / np.log(2)).is_integer():
            data_out_gab.append("P")
            qtd_bp = qtd_bp + 1
        else:
            data_out_gab.append("D")

        # Veriyi yeni çıktı boyutuna göre sıralar
        if data_out_gab[-1] == "D":
            data_output.append(item)
        else:
            parity_received.append(item)

    # -----------veri ile pariteyi hesaplar
    data_out = []
    parity = []
    bin_pos = [bin(x)[2:] for x in range(1, size_par + len(data_output) + 1)]

    # Çıktı verisinin boyutuna göre sıralanmış bilgi verisi
    data_ord = []
    # Veri pozisyon şablonu + parite
    data_out_gab = []
    # Parite bit sayacı
    qtd_bp = 0
    # Veri bit okuma sayacı
    cont_data = 0

    for x in range(1, size_par + len(data_output) + 1):
        # Bit pozisyonlarının bir şablonunu oluşturur - hangi bitlerin bilgi,
        # hangilerinin parite olması gerektiğini belirler
        if qtd_bp < size_par and (np.log(x) / np.log(2)).is_integer():
            data_out_gab.append("P")
            qtd_bp = qtd_bp + 1
        else:
            data_out_gab.append("D")

        # Veriyi yeni çıktı boyutuna göre sıralar
        if data_out_gab[-1] == "D":
            data_ord.append(data_output[cont_data])
            cont_data += 1
        else:
            data_ord.append(None)

    # Parite hesaplar
    qtd_bp = 0  # parite bit sayacı
    for bp in range(1, size_par + 1):
        # Belirli bir parite için bir bit sayacı
        cont_bo = 0
        for cont_loop, x in enumerate(data_ord):
            if x is not None:
                try:
                    aux = (bin_pos[cont_loop])[-1 * (bp)]
                except IndexError:
                    aux = "0"
                if aux == "1" and x == "1":
                    cont_bo += 1
        parity.append(str(cont_bo % 2))

        qtd_bp += 1

    # Mesajı oluştur
    cont_bp = 0  # parite bit sayacı
    for x in range(size_par + len(data_output)):
        if data_ord[x] is None:
            data_out.append(str(parity[cont_bp]))
            cont_bp += 1
        else:
            data_out.append(data_ord[x])

    ack = parity_received == parity
    return data_output, ack


# ---------------------------------------------------------------------
"""
# Kullanım örneği

# Parite bitlerinin sayısı
sizePari = 4

# Hata olarak zorlanacak bitin konumu
be = 2

# Hamming ile kodlanacak ve çözülecek mesaj/kelime
# text = input("Okunacak kelimeyi girin: ")
text = "Message01"

# Mesajı ikiliye çevir
binaryText = text_to_bits(text)

# Dizgenin ikilisini yazdırır
print("İkili olarak girilen metin '" + binaryText + "'")

# Toplam iletilen bitler
totalBits = len(binaryText) + sizePari
print("Veri boyutu " + str(totalBits))

print("\n --Mesaj değişimi--")
print("Gönderilecek veri ------------> " + binaryText)
dataOut = emitter_converter(sizePari, binaryText)
print("Dönüştürülmüş veri ----------> " + "".join(dataOut))
dataReceiv, ack = receptor_converter(sizePari, dataOut)
print(
    "Alınan veri ------------> "
    + "".join(dataReceiv)
    + "\t\t -- Veri bütünlüğü: "
    + str(ack)
)


print("\n --Hata zorla--")
print("Gönderilecek veri ------------> " + binaryText)
dataOut = emitter_converter(sizePari, binaryText)
print("Dönüştürülmüş veri ----------> " + "".join(dataOut))

# Hata zorlar
dataOut[-be] = "1" * (dataOut[-be] == "0") + "0" * (dataOut[-be] == "1")
print("İletim sonrası veri -> " + "".join(dataOut))
dataReceiv, ack = receptor_converter(sizePari, dataOut)
print(
    "Alınan veri ------------> "
    + "".join(dataReceiv)
    + "\t\t -- Veri bütünlüğü: "
    + str(ack)
)
"""
