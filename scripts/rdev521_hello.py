def kaprekar_routine(number: int) -> int:
    """
    4 basamaklı sayıları alıp Kaprekar sabitine (6174) kaç adımda ulaştığını buluyorum.
    >>> kaprekar_routine(3524)
    3
    >>> kaprekar_routine(6174)
    0
    """
    # Sayı 4 basamaklı değilse direkt hata fırlatıyorum
    if not (1000 <= number <= 9999):
        raise ValueError("Sayı kesinlikle 4 basamaklı olmalı!")
        
    # Herkes aynı rakamı girerse (1111 gibi) döngü patlar, o yüzden engelliiyorum
    if len(set(str(number))) < 2:
        raise ValueError("Rakamların hepsi aynı olamaz! , en az ikisi farklı olmalı")

    kaprekar_target = 6174
    steps = 0

    # Sayı 6174 olana kadar buradayız , döngü dönüyor
    while number != kaprekar_target:
        # Sayıyı 4 basamağa tamamlayıp stringe çeviriyom
        digits = f"{number:04d}"
        
        # Rakamları büyükten küçüğe dizip birleştiriyorum
        descending = int("".join(sorted(digits, reverse=True)))
        
        # Rakamları küçükten büyüğe dizip birleştiriyom
        ascending = int("".join(sorted(digits)))
        
        # Büyükten küçüğü çıkarıp yeni sayıyı buluyom ve adımı arttırıyorum
        number = descending - ascending
        steps += 1

        # Olur da patlarsak diye sonsuz döngü koruması koydum, en fazla 7 döner
        if steps > 7:
            break

    return steps

if __name__ == "__main__":
    import doctest
    # Botların kontrol ettiği test motorunu çalıştırıyom bro
    doctest.testmod()
    
    # Kendim test etmek için de şuraya bir örnek bıraktım
    print(f"Bizim sayı tam {kaprekar_routine(3524)} adımda kilitlendi!")
