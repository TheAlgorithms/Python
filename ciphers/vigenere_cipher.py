HARFLER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Organiser: K. Umut Araz

def ana_fonksiyonu() -> None:
    mesaj = input("Mesajı girin: ")
    anahtar = input("Anahtarı girin [alfa sayısal]: ")
    mod = input("Şifrele/Şifre Çöz [s/c]: ")

    if mod.lower().startswith("s"):
        mod = "şifrele"
        çevrilen = mesajı_şifrele(anahtar, mesaj)
    elif mod.lower().startswith("c"):
        mod = "şifre çöz"
        çevrilen = mesajı_şifre_çöz(anahtar, mesaj)

    print(f"\n{mod.title()} edilmiş mesaj:")
    print(çevrilen)

def mesajı_şifrele(anahtar: str, mesaj: str) -> str:
    """
    >>> mesajı_şifrele('HDarji', 'Bu Harshil Darji\'den Dharmaj\'a bir mesajdır.')
    'Akij ra Odrjqqs Gaisq muod Mphumrs.'
    """
    return mesajı_çevir(anahtar, mesaj, "şifrele")

def mesajı_şifre_çöz(anahtar: str, mesaj: str) -> str:
    """
    >>> mesajı_şifre_çöz('HDarji', 'Akij ra Odrjqqs Gaisq muod Mphumrs.')
    'Bu Harshil Darji\'den Dharmaj\'a bir mesajdır.'
    """
    return mesajı_çevir(anahtar, mesaj, "şifre çöz")

def mesajı_çevir(anahtar: str, mesaj: str, mod: str) -> str:
    çevrilen = []
    anahtar_indeksi = 0
    anahtar = anahtar.upper()

    for sembol in mesaj:
        num = HARFLER.find(sembol.upper())
        if num != -1:
            if mod == "şifrele":
                num += HARFLER.find(anahtar[anahtar_indeksi])
            elif mod == "şifre çöz":
                num -= HARFLER.find(anahtar[anahtar_indeksi])

            num %= len(HARFLER)

            if sembol.isupper():
                çevrilen.append(HARFLER[num])
            elif sembol.islower():
                çevrilen.append(HARFLER[num].lower())

            anahtar_indeksi += 1
            if anahtar_indeksi == len(anahtar):
                anahtar_indeksi = 0
        else:
            çevrilen.append(sembol)
    return "".join(çevrilen)

if __name__ == "__main__":
    ana_fonksiyonu()
