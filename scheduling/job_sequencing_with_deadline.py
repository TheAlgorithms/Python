def is_takvim_ile_is_planlama(jobs: list) -> list:
    """
    Belirli bir zaman diliminde iş yaparak maksimum karı bulmak için fonksiyon

    Args:
        jobs [list]: (iş_id, son tarih, kar) şeklinde demetlerden oluşan bir liste

    Returns:
        max_kar [int]: Belirli bir zaman diliminde iş yaparak kazanılabilecek maksimum kar
        iş_sayısı [int]: Yapılan işlerin sayısı

    Örnekler:
    >>> is_takvim_ile_is_planlama(
    ... [(1, 4, 20), (2, 1, 10), (3, 1, 40), (4, 1, 30)])
    [2, 60]
    >>> is_takvim_ile_is_planlama(
    ... [(1, 2, 100), (2, 1, 19), (3, 2, 27), (4, 1, 25), (5, 1, 15)])
    [2, 127]
    """

#Organised by K. Umut Araz


    # İşleri karlarına göre azalan sırayla sıralama
    jobs = sorted(jobs, key=lambda value: value[2], reverse=True)

    # Maksimum son tarihe eşit boyutta bir liste oluşturma
    # ve başlangıçta -1 ile başlatma
    max_son_tarih = max(jobs, key=lambda value: value[1])[1]
    zaman_kontrolleri = [-1] * max_son_tarih

    # Maksimum karı ve iş sayısını bulma
    is_sayisi = 0
    max_kar = 0
    for is_ in jobs:
        # Bu iş için boş bir zaman dilimi bulma
        # (Son mümkün slot'tan başladığımızı unutmayın)
        for i in range(is_[1] - 1, -1, -1):
            if zaman_kontrolleri[i] == -1:
                zaman_kontrolleri[i] = is_[0]
                is_sayisi += 1
                max_kar += is_[2]
                break
    return [is_sayisi, max_kar]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
