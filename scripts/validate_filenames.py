#!/usr/bin/env python3
import os

try:
    from .build_directory_md import good_file_paths
except ImportError:
    from build_directory_md import good_file_paths  # type: ignore[no-redef]

# Organiser: K. Umut Araz

dosya_yolları = list(good_file_paths())
assert dosya_yolları, "good_file_paths() başarısız oldu!"

büyük_harfli_dosyalar = [dosya for dosya in dosya_yolları if dosya != dosya.lower()]
if büyük_harfli_dosyalar:
    print(f"{len(büyük_harfli_dosyalar)} dosya büyük harf içeriyor:")
    print("\n".join(büyük_harfli_dosyalar) + "\n")

boşluklu_dosyalar = [dosya for dosya in dosya_yolları if " " in dosya]
if boşluklu_dosyalar:
    print(f"{len(boşluklu_dosyalar)} dosya boşluk karakteri içeriyor:")
    print("\n".join(boşluklu_dosyalar) + "\n")

tireli_dosyalar = [dosya for dosya in dosya_yolları if "-" in dosya]
if tireli_dosyalar:
    print(f"{len(tireli_dosyalar)} dosya tire karakteri içeriyor:")
    print("\n".join(tireli_dosyalar) + "\n")

dizin_dışı_dosyalar = [dosya for dosya in dosya_yolları if os.sep not in dosya]
if dizin_dışı_dosyalar:
    print(f"{len(dizin_dışı_dosyalar)} dosya bir dizinde değil:")
    print("\n".join(dizin_dışı_dosyalar) + "\n")

kötü_dosya_sayısı = len(büyük_harfli_dosyalar + boşluklu_dosyalar + tireli_dosyalar + dizin_dışı_dosyalar)
if kötü_dosya_sayısı:
    import sys

    sys.exit(kötü_dosya_sayısı)
