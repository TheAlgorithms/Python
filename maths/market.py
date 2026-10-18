para = 40
toplam = ()
print("Adınız nedir?")
ad = input()
print("Soyadınız nedir?")
soyad = input()
print("Merhaba, {0} {1}!, Kaç tane kitap almak istiyosunuz?".format(ad, soyad))
tane = int(input())
if tane > 50:
    print("İndirimimiz var %50 indirim kazandınız,50 den fazla kitap alana %50 indirim uygulanır.")
    toplam = (para * tane) - (para * tane * 50 / 100)
    print("Toplam ödemeniz gereken miktar: " + str(toplam) + " TL")
else:
    toplam = para * tane
    print("Toplam ödemeniz gereken miktar: " + str(toplam) + " TL")