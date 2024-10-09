alfabeler = [chr(i) for i in range(32, 126)]
dişli_bir = list(range(len(alfabeler)))
dişli_iki = list(range(len(alfabeler)))
dişli_üç = list(range(len(alfabeler)))
reflektör = list(reversed(range(len(alfabeler))))
kod = []
dişli_bir_pos = dişli_iki_pos = dişli_üç_pos = 0


def döndürücü():
    global dişli_bir_pos
    global dişli_iki_pos
    global dişli_üç_pos
    i = dişli_bir[0]
    dişli_bir.append(i)
    del dişli_bir[0]
    dişli_bir_pos += 1
    if dişli_bir_pos % int(len(alfabeler)) == 0:
        i = dişli_iki[0]
        dişli_iki.append(i)
        del dişli_iki[0]
        dişli_iki_pos += 1
        if dişli_iki_pos % int(len(alfabeler)) == 0:
            i = dişli_üç[0]
            dişli_üç.append(i)
            del dişli_üç[0]
            dişli_üç_pos += 1


def motor(girdi_karakteri):
    hedef = alfabeler.index(girdi_karakteri)
    hedef = dişli_bir[hedef]
    hedef = dişli_iki[hedef]
    hedef = dişli_üç[hedef]
    hedef = reflektör[hedef]
    hedef = dişli_üç.index(hedef)
    hedef = dişli_iki.index(hedef)
    hedef = dişli_bir.index(hedef)
    kod.append(alfabeler[hedef])
    döndürücü()


if __name__ == "__main__":
    çöz = list(input("Mesajınızı yazın:\n"))
    while True:
        try:
            jeton = int(input("Lütfen jeton ayarlayın:(sadece rakamlar olmalı)\n"))
            break
        except Exception as hata:
            print(hata)
    for _ in range(jeton):
        döndürücü()
    for j in çöz:
        motor(j)
    print("\n" + "".join(kod))
    print(
        f"\nJetonunuz {jeton} lütfen not edin.\nBu mesajı tekrar çözmek isterseniz aynı rakamları jeton olarak girmelisiniz!"
    )
