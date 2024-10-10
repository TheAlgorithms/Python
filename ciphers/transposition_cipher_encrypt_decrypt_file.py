import os
import sys
import time

from . import transposition_cipher as trans_cipher

def main() -> None:
    girdi_dosyasi = "./prehistoric_men.txt"
    cikti_dosyasi = "./Output.txt"

    #Organiser: K. Umut Araz
    
    try:
        anahtar = int(input("Anahtar girin (tam sayı): "))
    except ValueError:
        print("Geçersiz anahtar. Lütfen bir tam sayı girin.")
        sys.exit()

    mod = input("Şifrele/Şifre Çöz [e/d]: ").strip().lower()
    if mod not in ['e', 'd']:
        print("Geçersiz mod. Lütfen 'e' ile şifrele veya 'd' ile şifre çöz girin.")
        sys.exit()

    if not os.path.exists(girdi_dosyasi):
        print(f"{girdi_dosyasi} dosyası mevcut değil. Çıkılıyor...")
        sys.exit()

    if os.path.exists(cikti_dosyasi):
        cevap = input(f"{cikti_dosyasi} dosyasını üzerine yazmak istiyor musunuz? [y/n]: ").strip().lower()
        if not cevap.startswith("y"):
            print("İşlem iptal edildi.")
            sys.exit()

    baslangic_zamani = time.time()

    try:
        if mod == "e":
            with open(girdi_dosyasi, 'r') as f:
                icerik = f.read()
            cevrilen = trans_cipher.encrypt_message(anahtar, icerik)
        elif mod == "d":
            with open(cikti_dosyasi, 'r') as f:
                icerik = f.read()
            cevrilen = trans_cipher.decrypt_message(anahtar, icerik)
    except IOError as e:
        print(f"Dosya okuma hatası: {e}")
        sys.exit()

    try:
        with open(cikti_dosyasi, "w") as cikti_obj:
            cikti_obj.write(cevrilen)
    except IOError as e:
        print(f"Dosyaya yazma hatası: {e}")
        sys.exit()

    toplam_zaman = round(time.time() - baslangic_zamani, 2)
    print(f"Tamamlandı, süre: {toplam_zaman} saniye.")

if __name__ == "__main__":
    main()