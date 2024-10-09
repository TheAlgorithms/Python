"""

Bu, görevlerin insanlar arasında atanmasını içeren sorular için bir Python uygulamasıdır.
Bu sorunu çözmek için Bitmasking ve DP kullanılmıştır.

Soru :-
N görevimiz ve M kişimiz var. M'deki her kişi yalnızca bu görevlerden bazılarını yapabilir.
Ayrıca bir kişi yalnızca bir görev yapabilir ve bir görev yalnızca bir kişi tarafından yapılır.
Görevlerin dağıtılabileceği toplam yol sayısını bulun.
"""

from collections import defaultdict


class BitmaskKullanarakAtama:
    def __init__(self, yapilan_gorevler, toplam):
        self.toplam_gorevler = toplam  # toplam görev sayısı (N)

        # DP tablosu (2^M)*N boyutunda olacak
        # başlangıçta tüm değerler -1 olarak ayarlanır
        self.dp = [
            [-1 for i in range(toplam + 1)] for j in range(2 ** len(yapilan_gorevler))
        ]

        self.gorev = defaultdict(list)  # her görev için kişilerin listesini saklar

        # final_mask, tüm kişilerin dahil edilip edilmediğini kontrol etmek için
        # tüm bitleri 1 olarak ayarlayarak kullanılır
        self.final_mask = (1 << len(yapilan_gorevler)) - 1

    def belirli_bir_zamana_kadar_yollari_say(self, mask, gorev_no):
        # eğer mask == self.final_mask ise tüm kişilere görevler dağıtılmıştır, 1 döndür
        if mask == self.final_mask:
            return 1

        # eğer herkes görev almazsa ve daha fazla görev yoksa, 0 döndür
        if gorev_no > self.toplam_gorevler:
            return 0

        # eğer durum zaten düşünülmüşse
        if self.dp[mask][gorev_no] != -1:
            return self.dp[mask][gorev_no]

        # Bu görevi düzenlemeye dahil etmediğimizde yolların sayısı
        toplam_yollar_util = self.belirli_bir_zamana_kadar_yollari_say(mask, gorev_no + 1)

        # şimdi görevleri tek tek tüm olası kişilere atayın ve kalan görevler için
        # özyinelemeli olarak atayın.
        if gorev_no in self.gorev:
            for p in self.gorev[gorev_no]:
                # eğer p zaten bir görev aldıysa
                if mask & (1 << p):
                    continue

                # bu görevi p'ye atayın ve mask değerini değiştirin. Ve yeni mask
                # değeriyle özyinelemeli olarak görevleri atayın.
                toplam_yollar_util += self.belirli_bir_zamana_kadar_yollari_say(mask | (1 << p), gorev_no + 1)

        # değeri kaydet.
        self.dp[mask][gorev_no] = toplam_yollar_util

        return self.dp[mask][gorev_no]

    def toplam_yol_sayisini_bul(self, yapilan_gorevler):
        # Her görev için kişilerin listesini saklayın
        for i in range(len(yapilan_gorevler)):
            for j in yapilan_gorevler[i]:
                self.gorev[j].append(i)

        # DP tablosunu doldurmak için fonksiyonu çağırın, nihai cevap dp[0][1]'de saklanır
        return self.belirli_bir_zamana_kadar_yollari_say(0, 1)


if __name__ == "__main__":
    toplam_gorevler = 5  # toplam görev sayısı (N değeri)

    # M kişisi tarafından yapılabilecek görevlerin listesi.
    yapilan_gorevler = [[1, 3, 4], [1, 2, 5], [3, 4]]
    print(
        BitmaskKullanarakAtama(yapilan_gorevler, toplam_gorevler).toplam_yol_sayisini_bul(
            yapilan_gorevler
        )
    )
    """
    Belirli bir örnek için görevler şu şekilde dağıtılabilir
    (1,2,3), (1,2,4), (1,5,3), (1,5,4), (3,1,4),
    (3,2,4), (3,5,4), (4,1,3), (4,2,3), (4,5,3)
    toplam 10
    """
