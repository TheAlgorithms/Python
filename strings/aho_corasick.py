from __future__ import annotations

from collections import deque

# Organiser: K. Umut Araz


class Otomaton:
    def __init__(self, anahtar_kelimeler: list[str]):
        self.ad_list: list[dict] = []
        self.ad_list.append(
            {"değer": "", "sonraki_durumlar": [], "başarısız_durum": 0, "çıktı": []}
        )

        for anahtar_kelime in anahtar_kelimeler:
            self.anahtar_kelime_ekle(anahtar_kelime)
        self.başarısız_geçişleri_belirle()

    def sonraki_durumu_bul(self, mevcut_durum: int, karakter: str) -> int | None:
        for durum in self.ad_list[mevcut_durum]["sonraki_durumlar"]:
            if karakter == self.ad_list[durum]["değer"]:
                return durum
        return None

    def anahtar_kelime_ekle(self, anahtar_kelime: str) -> None:
        mevcut_durum = 0
        for karakter in anahtar_kelime:
            sonraki_durum = self.sonraki_durumu_bul(mevcut_durum, karakter)
            if sonraki_durum is None:
                self.ad_list.append(
                    {
                        "değer": karakter,
                        "sonraki_durumlar": [],
                        "başarısız_durum": 0,
                        "çıktı": [],
                    }
                )
                self.ad_list[mevcut_durum]["sonraki_durumlar"].append(len(self.ad_list) - 1)
                mevcut_durum = len(self.ad_list) - 1
            else:
                mevcut_durum = sonraki_durum
        self.ad_list[mevcut_durum]["çıktı"].append(anahtar_kelime)

    def başarısız_geçişleri_belirle(self) -> None:
        kuyruk: deque = deque()
        for düğüm in self.ad_list[0]["sonraki_durumlar"]:
            kuyruk.append(düğüm)
            self.ad_list[düğüm]["başarısız_durum"] = 0
        while kuyruk:
            r = kuyruk.popleft()
            for çocuk in self.ad_list[r]["sonraki_durumlar"]:
                kuyruk.append(çocuk)
                durum = self.ad_list[r]["başarısız_durum"]
                while (
                    self.sonraki_durumu_bul(durum, self.ad_list[çocuk]["değer"]) is None
                    and durum != 0
                ):
                    durum = self.ad_list[durum]["başarısız_durum"]
                self.ad_list[çocuk]["başarısız_durum"] = self.sonraki_durumu_bul(
                    durum, self.ad_list[çocuk]["değer"]
                )
                if self.ad_list[çocuk]["başarısız_durum"] is None:
                    self.ad_list[çocuk]["başarısız_durum"] = 0
                self.ad_list[çocuk]["çıktı"] = (
                    self.ad_list[çocuk]["çıktı"]
                    + self.ad_list[self.ad_list[çocuk]["başarısız_durum"]]["çıktı"]
                )

    def ara(self, metin: str) -> dict[str, list[int]]:
        """
        >>> A = Otomaton(["ne", "şapka", "gör", "ör"])
        >>> A.ara("ne şapka, örneğin ... , nerede")
        {'ne': [0], 'şapka': [1], 'gör': [5, 25], 'ör': [6, 10, 22, 26]}
        """
        sonuç: dict = {}  # anahtar kelimeleri ve bunların geçişlerinin listesini döndürür
        mevcut_durum = 0
        for i in range(len(metin)):
            while (
                self.sonraki_durumu_bul(mevcut_durum, metin[i]) is None
                and mevcut_durum != 0
            ):
                mevcut_durum = self.ad_list[mevcut_durum]["başarısız_durum"]
            sonraki_durum = self.sonraki_durumu_bul(mevcut_durum, metin[i])
            if sonraki_durum is None:
                mevcut_durum = 0
            else:
                mevcut_durum = sonraki_durum
                for anahtar in self.ad_list[mevcut_durum]["çıktı"]:
                    if anahtar not in sonuç:
                        sonuç[anahtar] = []
                    sonuç[anahtar].append(i - len(anahtar) + 1)
        return sonuç


if __name__ == "__main__":
    import doctest

    doctest.testmod()
