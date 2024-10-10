"""
Moleküler kimya için yararlı fonksiyonlar:
* molarite_normaliteye_dönüştür
* mol sayısını basınca dönüştür
* mol sayısını hacme dönüştür
* basınç ve hacmi sıcaklığa dönüştür

Organiser: K. Umut Araz
"""


def molarite_normaliteye_dönüştür(nfaktör: int, mol: float, hacim: float) -> float:
    """
    Molariteyi normaliteye dönüştür.
      Hacim litre cinsindendir.

      Wikipedia referansı: https://en.wikipedia.org/wiki/Equivalent_concentration
      Wikipedia referansı: https://en.wikipedia.org/wiki/Molar_concentration

      >>> molarite_normaliteye_dönüştür(2, 3.1, 0.31)
      20
      >>> molarite_normaliteye_dönüştür(4, 11.4, 5.7)
      8
    """
    return round(float(mol / hacim) * nfaktör)


def mol_sayısını_basınca_dönüştür(hacim: float, mol: float, sıcaklık: float) -> float:
    """
    Mol sayısını basınca dönüştür.
      Ideal gaz yasaları kullanılır.
      Sıcaklık kelvin cinsindendir.
      Hacim litre cinsindendir.
      Basınç SI birimi olarak atm cinsindendir.

      Wikipedia referansı: https://en.wikipedia.org/wiki/Gas_laws
      Wikipedia referansı: https://en.wikipedia.org/wiki/Pressure
      Wikipedia referansı: https://en.wikipedia.org/wiki/Temperature

      >>> mol_sayısını_basınca_dönüştür(0.82, 3, 300)
      90
      >>> mol_sayısını_basınca_dönüştür(8.2, 5, 200)
      10
    """
    return round(float((mol * 0.0821 * sıcaklık) / (hacim)))


def mol_sayısını_hacme_dönüştür(basınç: float, mol: float, sıcaklık: float) -> float:
    """
    Mol sayısını hacme dönüştür.
      Ideal gaz yasaları kullanılır.
      Sıcaklık kelvin cinsindendir.
      Hacim litre cinsindendir.
      Basınç SI birimi olarak atm cinsindendir.

      Wikipedia referansı: https://en.wikipedia.org/wiki/Gas_laws
      Wikipedia referansı: https://en.wikipedia.org/wiki/Pressure
      Wikipedia referansı: https://en.wikipedia.org/wiki/Temperature

      >>> mol_sayısını_hacme_dönüştür(0.82, 3, 300)
      90
      >>> mol_sayısını_hacme_dönüştür(8.2, 5, 200)
      10
    """
    return round(float((mol * 0.0821 * sıcaklık) / (basınç)))


def basınç_ve_hacmi_sıcaklığa_dönüştür(
    basınç: float, mol: float, hacim: float
) -> float:
    """
    Basınç ve hacmi sıcaklığa dönüştür.
      Ideal gaz yasaları kullanılır.
      Sıcaklık kelvin cinsindendir.
      Hacim litre cinsindendir.
      Basınç SI birimi olarak atm cinsindendir.

      Wikipedia referansı: https://en.wikipedia.org/wiki/Gas_laws
      Wikipedia referansı: https://en.wikipedia.org/wiki/Pressure
      Wikipedia referansı: https://en.wikipedia.org/wiki/Temperature

      >>> basınç_ve_hacmi_sıcaklığa_dönüştür(0.82, 1, 2)
      20
      >>> basınç_ve_hacmi_sıcaklığa_dönüştür(8.2, 5, 3)
      60
    """
    return round(float((basınç * hacim) / (0.0821 * mol)))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
