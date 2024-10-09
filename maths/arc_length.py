from math import pi

#Organised by K. Umut Araz

def yay_uzunlugu(acı: int, yaricap: int) -> float:
    """
    Bir çemberin yay uzunluğunu hesaplar.
    
    Örnekler:
    >>> yay_uzunlugu(45, 5)
    3.9269908169872414
    >>> yay_uzunlugu(120, 15)
    31.415926535897928
    >>> yay_uzunlugu(90, 10)
    15.707963267948966
    """
    return 2 * pi * yaricap * (acı / 360)


if __name__ == "__main__":
    print(yay_uzunlugu(90, 10))
