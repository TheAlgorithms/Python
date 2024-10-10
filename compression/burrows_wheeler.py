"""
https://tr.wikipedia.org/wiki/Burrows%E2%80%93Wheeler_dönüşümü

Burrows-Wheeler dönüşümü (BWT, ayrıca blok-sıralama sıkıştırması olarak da bilinir), bir karakter dizisini benzer karakterlerin grupları halinde yeniden düzenler. Bu, sıkıştırma için faydalıdır çünkü tekrar eden karakterlerin gruplarını içeren bir diziyi sıkıştırmak, öncelikle öncelik sırasına göre yer değiştirme ve koşullu uzunluk kodlaması gibi tekniklerle kolaydır. Daha da önemlisi, dönüşüm tersine çevrilebilir; ilk orijinal karakterin konumu dışında ek veri saklamaya gerek yoktur. Bu nedenle BWT, metin sıkıştırma algoritmalarının verimliliğini artırmanın "ücretsiz" bir yöntemidir ve yalnızca biraz ek hesaplama gerektirir.
"""

from __future__ import annotations

# Organiser: K. Umut Araz

from typing import TypedDict


class BWTTransformDict(TypedDict):
    bwt_string: str
    idx_original_string: int


def tum_dönüşümler(s: str) -> list[str]:
    """
    :param s: len(s) kez döndürülecek olan dize.
    :return: Dönüşümlerin listesini döndürür.
    :raises TypeError: Eğer s bir str örneği değilse.
    Örnekler:

    >>> tum_dönüşümler("^BANANA|") # doctest: +NORMALIZE_WHITESPACE
    ['^BANANA|', 'BANANA|^', 'ANANA|^B', 'NANA|^BA', 'ANA|^BAN', 'NA|^BANA',
    'A|^BANAN', '|^BANANA']
    >>> tum_dönüşümler("a_asa_da_casa") # doctest: +NORMALIZE_WHITESPACE
    ['a_asa_da_casa', '_asa_da_casaa', 'asa_da_casaa_', 'sa_da_casaa_a',
    'a_da_casaa_as', '_da_casaa_asa', 'da_casaa_asa_', 'a_casaa_asa_d',
    '_casaa_asa_da', 'casaa_asa_da_', 'asaa_asa_da_c', 'saa_asa_da_ca',
    'aa_asa_da_cas']
    >>> tum_dönüşümler("panamabanana") # doctest: +NORMALIZE_WHITESPACE
    ['panamabanana', 'anamabananap', 'namabananapa', 'amabananapan',
    'mabananapana', 'abananapanam', 'bananapanama', 'ananapanamab',
    'nanapanamaba', 'anapanamaban', 'napanamabana', 'apanamabanan']
    >>> tum_dönüşümler(5)
    Traceback (most recent call last):
        ...
    TypeError: Parametre s tipi str olmalıdır.
    """
    if not isinstance(s, str):
        raise TypeError("Parametre s tipi str olmalıdır.")

    return [s[i:] + s[:i] for i in range(len(s))]


def bwt_dönüşümü(s: str) -> BWTTransformDict:
    """
    :param s: BWT algoritmasında kullanılacak dize
    :return: Sıralı dönüşümlerin her satırının son karakterinden oluşan dize ve
    orijinal dizenin sıralı dönüşümler listesindeki indeksi
    :raises TypeError: Eğer s parametre tipi str değilse
    :raises ValueError: Eğer s parametresi boşsa
    Örnekler:

    >>> bwt_dönüşümü("^BANANA")
    {'bwt_string': 'BNN^AAA', 'idx_original_string': 6}
    >>> bwt_dönüşümü("a_asa_da_casa")
    {'bwt_string': 'aaaadss_c__aa', 'idx_original_string': 3}
    >>> bwt_dönüşümü("panamabanana")
    {'bwt_string': 'mnpbnnaaaaaa', 'idx_original_string': 11}
    >>> bwt_dönüşümü(4)
    Traceback (most recent call last):
        ...
    TypeError: Parametre s tipi str olmalıdır.
    >>> bwt_dönüşümü('')
    Traceback (most recent call last):
        ...
    ValueError: Parametre s boş olmamalıdır.
    """
    if not isinstance(s, str):
        raise TypeError("Parametre s tipi str olmalıdır.")
    if not s:
        raise ValueError("Parametre s boş olmamalıdır.")

    dönüşümler = tum_dönüşümler(s)
    dönüşümler.sort()  # Dönüşüm listesini alfabetik sıraya göre sırala
    # Her dönüşümün son karakterinden oluşan bir dize oluştur
    yanıt: BWTTransformDict = {
        "bwt_string": "".join([kelime[-1] for kelime in dönüşümler]),
        "idx_original_string": dönüşümler.index(s),
    }
    return yanıt


def ters_bwt(bwt_string: str, idx_original_string: int) -> str:
    """
    :param bwt_string: BWT algoritması çalıştırıldığında dönen dize
    :param idx_original_string: bwt_string'in oluşturulmasında kullanılan
    dizenin sıralı dönüşümler listesindeki 0 tabanlı indeksi
    :return: BWT çalıştırıldığında bwt_string'i oluşturmak için kullanılan dize
    :param bwt_string: The string returned from bwt algorithm execution
    :param idx_original_string: A 0-based index of the string that was used to
    generate bwt_string at ordered rotations list
    :return: The string used to generate bwt_string when bwt was executed
    :raises TypeError: If the bwt_string parameter type is not str
    :raises ValueError: If the bwt_string parameter is empty
    :raises TypeError: If the idx_original_string type is not int or if not
    possible to cast it to int
    :raises ValueError: If the idx_original_string value is lower than 0 or
    greater than len(bwt_string) - 1

    >>> reverse_bwt("BNN^AAA", 6)
    '^BANANA'
    >>> reverse_bwt("aaaadss_c__aa", 3)
    'a_asa_da_casa'
    >>> reverse_bwt("mnpbnnaaaaaa", 11)
    'panamabanana'
    >>> reverse_bwt(4, 11)
    Traceback (most recent call last):
        ...
    TypeError: The parameter bwt_string type must be str.
    >>> reverse_bwt("", 11)
    Traceback (most recent call last):
        ...
    ValueError: The parameter bwt_string must not be empty.
    >>> reverse_bwt("mnpbnnaaaaaa", "asd") # doctest: +NORMALIZE_WHITESPACE
    Traceback (most recent call last):
        ...
    TypeError: The parameter idx_original_string type must be int or passive
    of cast to int.
    >>> reverse_bwt("mnpbnnaaaaaa", -1)
    Traceback (most recent call last):
        ...
    ValueError: The parameter idx_original_string must not be lower than 0.
    >>> reverse_bwt("mnpbnnaaaaaa", 12) # doctest: +NORMALIZE_WHITESPACE
    Traceback (most recent call last):
        ...
    ValueError: The parameter idx_original_string must be lower than
    len(bwt_string).
    >>> reverse_bwt("mnpbnnaaaaaa", 11.0)
    'panamabanana'
    >>> reverse_bwt("mnpbnnaaaaaa", 11.4)
    'panamabanana'
    """
    if not isinstance(bwt_string, str):
        raise TypeError("The parameter bwt_string type must be str.")
    if not bwt_string:
        raise ValueError("The parameter bwt_string must not be empty.")
    try:
        idx_original_string = int(idx_original_string)
    except ValueError:
        raise TypeError(
            "The parameter idx_original_string type must be int or passive"
            " of cast to int."
        )
    if idx_original_string < 0:
        raise ValueError("The parameter idx_original_string must not be lower than 0.")
    if idx_original_string >= len(bwt_string):
        raise ValueError(
            "The parameter idx_original_string must be lower than len(bwt_string)."
        )

    ordered_rotations = [""] * len(bwt_string)
    for _ in range(len(bwt_string)):
        for i in range(len(bwt_string)):
            ordered_rotations[i] = bwt_string[i] + ordered_rotations[i]
        ordered_rotations.sort()
    return ordered_rotations[idx_original_string]


if __name__ == "__main__":
    entry_msg = "Provide a string that I will generate its BWT transform: "
    s = input(entry_msg).strip()
    result = bwt_transform(s)
    print(
        f"Burrows Wheeler transform for string '{s}' results "
        f"in '{result['bwt_string']}'"
    )
    original_string = reverse_bwt(result["bwt_string"], result["idx_original_string"])
    print(
        f"Reversing Burrows Wheeler transform for entry '{result['bwt_string']}' "
        f"we get original string '{original_string}'"
    )
