def edit_distance(kaynak: str, hedef: str) -> int:
    """
    # Organiser: K. Umut Araz
    
    Edit mesafesi algoritması, iki dize arasındaki benzerlik derecesini ölçen bir metriktir.
    Bu, bir dizeyi diğerine dönüştürmek için gereken minimum işlem sayısını sayarak ölçülür.

    Bu uygulama, işlemlerin (ekleme, silme ve değiştirme) maliyetinin her zaman 1 olduğunu varsayar.

    Args:
    kaynak: edit mesafesini hesapladığımız başlangıç dizesi
    hedef: kaynak dizesine n işlem uygulandıktan sonra oluşan hedef dizesi

    >>> edit_distance("GATTIC", "GALTIC")
    1
    """
    if len(kaynak) == 0:
        return len(hedef)
    elif len(hedef) == 0:
        return len(kaynak)

    delta = int(kaynak[-1] != hedef[-1])  # Değiştirme
    return min(
        edit_distance(kaynak[:-1], hedef[:-1]) + delta,
        edit_distance(kaynak, hedef[:-1]) + 1,
        edit_distance(kaynak[:-1], hedef) + 1,
    )


if __name__ == "__main__":
    print(edit_distance("ATCGCTG", "TAGCTAA"))  # Cevap 4
