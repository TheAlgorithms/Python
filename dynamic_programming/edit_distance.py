"""
Yazar  : Turfa Auliarachman
Tarih  : 12 Ekim 2016

Bu, edit mesafesi problemine Dinamik Programlama çözümünün saf Python uygulamasıdır.

Problem :
İki dize A ve B verildiğinde, A = B olacak şekilde B dizisine minimum sayıda işlem
bulun. İzin verilen işlemler çıkarma, ekleme ve değiştirmedir.
"""


class EditMesafesi:
    """
    Kullanım :
    cozumleyici          = EditMesafesi()
    editMesafesiSonucu   = cozumleyici.coz(firstString, secondString)
    """

    def __init__(self):
        self.kelime1 = ""
        self.kelime2 = ""
        self.dp = []

    def __min_mesafe_ustten_inis_dp(self, m: int, n: int) -> int:
        if m == -1:
            return n + 1
        elif n == -1:
            return m + 1
        elif self.dp[m][n] > -1:
            return self.dp[m][n]
        else:
            if self.kelime1[m] == self.kelime2[n]:
                self.dp[m][n] = self.__min_mesafe_ustten_inis_dp(m - 1, n - 1)
            else:
                ekle = self.__min_mesafe_ustten_inis_dp(m, n - 1)
                sil = self.__min_mesafe_ustten_inis_dp(m - 1, n)
                degistir = self.__min_mesafe_ustten_inis_dp(m - 1, n - 1)
                self.dp[m][n] = 1 + min(ekle, sil, degistir)

            return self.dp[m][n]

    def min_mesafe_ustten_inis(self, kelime1: str, kelime2: str) -> int:
        """
        >>> EditMesafesi().min_mesafe_ustten_inis("intention", "execution")
        5
        >>> EditMesafesi().min_mesafe_ustten_inis("intention", "")
        9
        >>> EditMesafesi().min_mesafe_ustten_inis("", "")
        0
        """
        self.kelime1 = kelime1
        self.kelime2 = kelime2
        self.dp = [[-1 for _ in range(len(kelime2))] for _ in range(len(kelime1))]

        return self.__min_mesafe_ustten_inis_dp(len(kelime1) - 1, len(kelime2) - 1)

    def min_mesafe_alttan_yukari(self, kelime1: str, kelime2: str) -> int:
        """
        >>> EditMesafesi().min_mesafe_alttan_yukari("intention", "execution")
        5
        >>> EditMesafesi().min_mesafe_alttan_yukari("intention", "")
        9
        >>> EditMesafesi().min_mesafe_alttan_yukari("", "")
        0
        """
        self.kelime1 = kelime1
        self.kelime2 = kelime2
        m = len(kelime1)
        n = len(kelime2)
        self.dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0:  # ilk dize boş
                    self.dp[i][j] = j
                elif j == 0:  # ikinci dize boş
                    self.dp[i][j] = i
                elif kelime1[i - 1] == kelime2[j - 1]:  # son karakterler eşit
                    self.dp[i][j] = self.dp[i - 1][j - 1]
                else:
                    ekle = self.dp[i][j - 1]
                    sil = self.dp[i - 1][j]
                    degistir = self.dp[i - 1][j - 1]
                    self.dp[i][j] = 1 + min(ekle, sil, degistir)
        return self.dp[m][n]


if __name__ == "__main__":
    cozumleyici = EditMesafesi()

    print("****************** Edit Mesafesi DP Algoritmasını Test Ediyor ******************")
    print()

    S1 = input("İlk diziyi girin: ").strip()
    S2 = input("İkinci diziyi girin: ").strip()

    print()
    print(f"Minimum edit mesafesi: {cozumleyici.min_mesafe_ustten_inis(S1, S2)}")
    print(f"Minimum edit mesafesi: {cozumleyici.min_mesafe_alttan_yukari(S1, S2)}")
    print()
    print("*************** Edit Mesafesi DP Algoritmasının Testi Bitti ***************")
