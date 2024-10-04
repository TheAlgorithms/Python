import string
from math import log10

"""
    tf-idf Wikipedia: https://en.wikipedia.org/wiki/Tf%E2%80%93idf
    tf-idf ve diğer kelime frekansı algoritmaları, bilgi erişimi ve metin madenciliğinde
    ağırlık faktörü olarak sıklıkla kullanılır. Metin tabanlı öneri sistemlerinin %83'ü
    terim ağırlığı için tf-idf kullanır. Basit bir ifadeyle, tf-idf bir kelimenin
    bir belgede ne kadar önemli olduğunu yansıtmayı amaçlayan bir istatistiktir.


    Burada bilgi erişiminde yaygın olarak kullanılan birkaç kelime frekansı algoritmasını
    uyguladım: Terim Frekansı, Belge Frekansı ve TF-IDF (Terim-Frekansı*Ters-Belge-Frekansı)
    dahildir.

    Terim Frekansı, bir belgedeki bir ifadenin ne sıklıkta
    geçtiğini temsil eden bir sayı döndüren istatistiksel bir işlevdir.
    Bu, belirli bir terimin bir belgede ne kadar önemli olduğunu gösterir.

    Belge Frekansı, bir terimin bir belgeler kümesinde kaç belgede
    geçtiğini temsil eden bir tamsayı döndüren istatistiksel bir işlevdir
    (dönen maksimum sayı, kümedeki belge sayısı olacaktır).

    Ters Belge Frekansı, matematiksel olarak log10(N/df) olarak yazılır, burada N
    kümenizdeki belge sayısı ve df Belge Frekansıdır. Eğer df 0 ise,
    ZeroDivisionError hatası atılacaktır.

    Terim-Frekansı*Ters-Belge-Frekansı, bir terimin özgünlüğünün bir ölçüsüdür.
    Matematiksel olarak tf*log10(N/df) olarak yazılır. Bir terimin
    bir belgede kaç kez geçtiğini, terimin kaç belgede geçtiğiyle karşılaştırır.
    Eğer df 0 ise, ZeroDivisionError hatası atılacaktır.
"""


def terim_frekansi(terim: str, belge: str) -> int:
    """
    Bir terimin belirli bir belgede kaç kez geçtiğini döndürür.
    @parametreler: terim, belgede aranacak terim ve belge,
            içinde aranacak belge
    @döndürür: bir terimin belgede kaç kez bulunduğunu temsil eden bir tamsayı

    @örnekler:
    >>> terim_frekansi("to", "To be, or not to be")
    2
    """
    # tüm noktalama işaretlerini ve yeni satırları kaldır ve yerine '' koy
    noktalama_olmayan_belge = belge.translate(
        str.maketrans("", "", string.punctuation)
    ).replace("\n", "")
    tokenize_belge = noktalama_olmayan_belge.split(" ")  # kelime tokenizasyonu
    return len([kelime for kelime in tokenize_belge if kelime.lower() == terim.lower()])


def belge_frekansi(terim: str, belge_kumesi: str) -> tuple[int, int]:
    """
    Bir terimin belirli bir belgeler kümesinde kaç belgede geçtiğini hesaplar
    @parametreler: terim, her belgede aranacak terim ve belge_kumesi, bir belge koleksiyonu.
             Her belge yeni bir satırla ayrılmalıdır.
    @döndürür: aradığınız terimin belge kümesinde kaç belgede geçtiğini ve
               belge kümesindeki belge sayısını döndürür
    @örnekler:
    >>> belge_frekansi("first", "This is the first document in the corpus.\\nThIs\
is the second document in the corpus.\\nTHIS is \
the third document in the corpus.")
    (1, 3)
    """
    noktalama_olmayan_belge_kumesi = belge_kumesi.lower().translate(
        str.maketrans("", "", string.punctuation)
    )  # tüm noktalama işaretlerini kaldır ve yerine '' koy
    belgeler = noktalama_olmayan_belge_kumesi.split("\n")
    terim = terim.lower()
    return (len([belge for belge in belgeler if terim in belge]), len(belgeler))


def ters_belge_frekansi(df: int, n: int, yumuşatma=False) -> float:
    """
    Bir kelimenin önemini belirten bir tamsayı döndürür.
    Bu önem ölçüsü log10(N/df) ile hesaplanır, burada N
    belge sayısı ve df Belge Frekansıdır.
    @parametreler: df, Belge Frekansı, N,
    belge kümesindeki belge sayısı ve
    yumuşatma, True ise idf-yumuşatılmış döndür
    @döndürür: log10(N/df) veya 1+log10(N/1+df)
    @örnekler:
    >>> ters_belge_frekansi(3, 0)
    Traceback (most recent call last):
     ...
    ValueError: log10(0) tanımsız.
    >>> ters_belge_frekansi(1, 3)
    0.477
    >>> ters_belge_frekansi(0, 3)
    Traceback (most recent call last):
     ...
    ZeroDivisionError: df > 0 olmalı
    >>> ters_belge_frekansi(0, 3, True)
    1.477
    """
    if yumuşatma:
        if n == 0:
            raise ValueError("log10(0) tanımsız.")
        return round(1 + log10(n / (1 + df)), 3)

    if df == 0:
        raise ZeroDivisionError("df > 0 olmalı")
    elif n == 0:
        raise ValueError("log10(0) tanımsız.")
    return round(log10(n / df), 3)


def tf_idf(tf: int, idf: int) -> float:
    """
    Terim frekansı ve ters belge frekansı fonksiyonlarını birleştirerek
    bir terimin özgünlüğünü hesaplar. Bu 'özgünlük', terim frekansı ve
    ters belge frekansının çarpılmasıyla hesaplanır: tf-idf = TF * IDF
    @parametreler: tf, terim frekansı ve idf, ters belge frekansı
    @örnekler:
    >>> tf_idf(2, 0.477)
    0.954
    """
    return round(tf * idf, 3)
