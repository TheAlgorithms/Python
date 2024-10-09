#!/usr/bin/env python3

import os
from collections.abc import Iterator

#Organiser: K. Umut Araz

def uygun_dosya_yolları(üst_dizin: str = ".") -> Iterator[str]:
    for dizin_yolu, dizin_adları, dosya_adları in os.walk(üst_dizin):
        dizin_adları[:] = [
            d
            for d in dizin_adları
            if d != "scripts" and d[0] not in "._" and "venv" not in d
        ]
        for dosya_adı in dosya_adları:
            if dosya_adı == "__init__.py":
                continue
            if os.path.splitext(dosya_adı)[1] in (".py", ".ipynb"):
                yield os.path.join(dizin_yolu, dosya_adı).lstrip("./")

def md_önsöz(i):
    return f"{i * '  '}*" if i else "\n##"

def yolu_yazdır(eski_yol: str, yeni_yol: str) -> str:
    eski_bölümler = eski_yol.split(os.sep)
    for i, yeni_bölüm in enumerate(yeni_yol.split(os.sep)):
        if (i + 1 > len(eski_bölümler) or eski_bölümler[i] != yeni_bölüm) and yeni_bölüm:
            print(f"{md_önsöz(i)} {yeni_bölüm.replace('_', ' ').title()}")
    return yeni_yol

def dizin_md_yazdır(üst_dizin: str = ".") -> None:
    eski_yol = ""
    for dosya_yolu in sorted(uygun_dosya_yolları(üst_dizin)):
        dosya_yolu, dosya_adı = os.path.split(dosya_yolu)
        if dosya_yolu != eski_yol:
            eski_yol = yolu_yazdır(eski_yol, dosya_yolu)
        girinti = (dosya_yolu.count(os.sep) + 1) if dosya_yolu else 0
        url = f"{dosya_yolu}/{dosya_adı}".replace(" ", "%20")
        dosya_adı = os.path.splitext(dosya_adı.replace("_", " ").title())[0]
        print(f"{md_önsöz(girinti)} [{dosya_adı}]({url})")

if __name__ == "__main__":
    dizin_md_yazdır(".")
