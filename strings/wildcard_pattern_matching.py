"""

Organiser: K. Umut Araz

Düzenli ifade eşleştirmesi uygulaması, '.' ve '*' desteği ile.
'.' Herhangi bir tek karakterle eşleşir.
'*' Önceki öğeden sıfır veya daha fazla eşleşir.
Eşleşme, tüm giriş dizesini kapsamalıdır (kısmi değil).

"""


def match_pattern(input_string: str, pattern: str) -> bool:
    """
    Verilen bir deseni giriş dizesi ile eşleştirmek için aşağıdan yukarıya dinamik programlama çözümü kullanır.

    Zaman Karmaşıklığı: O(len(input_string)*len(pattern))

    Argümanlar
    --------
    input_string: str, desene karşılaştırılacak herhangi bir dize
    pattern: str, bir deseni temsil eden ve '.' ile tek karakter eşleşmeleri ve '*' ile sıfır veya daha fazla önceki karakter eşleşmeleri içerebilen bir dize

    Not
    ----
    Desen '*' ile başlayamaz, çünkü '*' öncesinde en az bir karakter olmalıdır.

    Dönüş
    -------
    Verilen dize deseni takip ediyorsa bir Boolean değeri döner.

    Örnekler
    -------
    >>> match_pattern("aab", "c*a*b")
    True
    >>> match_pattern("dabc", "*abc")
    False
    >>> match_pattern("aaa", "aa")
    False
    >>> match_pattern("aaa", "a.a")
    True
    >>> match_pattern("aaab", "aa*")
    False
    >>> match_pattern("aaab", ".*")
    True
    >>> match_pattern("a", "bbbb")
    False
    >>> match_pattern("", "bbbb")
    False
    >>> match_pattern("a", "")
    False
    >>> match_pattern("", "")
    True
    """

    len_string = len(input_string) + 1
    len_pattern = len(pattern) + 1

    # dp, dp[i][j]'nin input_string'in i uzunluğundaki ön ekinin
    # verilen desenin j uzunluğundaki ön eki ile eşleşip eşleşmediğini belirttiği 2 boyutlu bir matristir.
    # "dp" dinamik programlamayı temsil eder.
    dp = [[0 for i in range(len_pattern)] for j in range(len_string)]

    # Sıfır uzunluğundaki dize, sıfır uzunluğundaki desenle eşleşir
    dp[0][0] = 1

    # Sıfır uzunluğundaki desen, sıfırdan uzun bir dize ile asla eşleşmeyecektir
    for i in range(1, len_string):
        dp[i][0] = 0

    # Sıfır uzunluğundaki dize, en az bir '*' içeren desenle eşleşir
    for j in range(1, len_pattern):
        dp[0][j] = dp[0][j - 2] if pattern[j - 1] == "*" else 0

    # Şimdi, tüm kalan uzunluklar için aşağıdan yukarıya yaklaşım kullanarak buluyoruz
    for i in range(1, len_string):
        for j in range(1, len_pattern):
            if input_string[i - 1] == pattern[j - 1] or pattern[j - 1] == ".":
                dp[i][j] = dp[i - 1][j - 1]

            elif pattern[j - 1] == "*":
                if dp[i][j - 2] == 1:
                    dp[i][j] = 1
                elif pattern[j - 2] in (input_string[i - 1], "."):
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = 0
            else:
                dp[i][j] = 0

    return bool(dp[-1][-1])


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    # Dize girişi
    # input_string = input("Bir dize girin:")
    # pattern = input("Bir desen girin:")

    input_string = "aab"
    pattern = "c*a*b"

    # Verilen dize ile verilen deseni kontrol etmek için fonksiyonu kullanma
    if match_pattern(input_string, pattern):
        print(f"{input_string} verilen desen {pattern} ile eşleşiyor.")
    else:
        print(f"{input_string} verilen desen {pattern} ile eşleşmiyor.")
