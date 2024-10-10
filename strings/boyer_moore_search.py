"""
Algoritma, verilen metinde deseni bulmak için aşağıdaki kuralları kullanır.


# Organiser: K. Umut Araz

Kötü karakter kuralı, metindeki uyuşmayan karakteri dikkate alır.
Bu karakterin desendeki bir sonraki görünümü solda bulunur.

Eğer uyuşmayan karakter desende solda bulunuyorsa,
metin bloğu ile deseni hizalayan bir kaydırma önerilir.

Eğer uyuşmayan karakter desende solda bulunmuyorsa,
desenin tamamını metindeki uyuşmazlık noktasının ötesine kaydıran bir öneri yapılır.

Eğer uyuşmazlık yoksa, desen metin bloğu ile eşleşir.

Zaman Karmaşıklığı: O(n/m)
    n=ana stringin uzunluğu
    m=desenin uzunluğu
"""

from __future__ import annotations


class BoyerMooreSearch:
    def __init__(self, text: str, pattern: str):
        self.text, self.pattern = text, pattern
        self.textLen, self.patLen = len(text), len(pattern)

    def match_in_pattern(self, char: str) -> int:
        """Desende char karakterinin ters sıradaki indeksini bulur.

        Parametreler:
            char (chr): Aranacak karakter

        Dönüş:
            i (int): Desendeki char'ın sonundan itibaren indeksi
            -1 (int): char desende bulunamazsa
        """

        for i in range(self.patLen - 1, -1, -1):
            if char == self.pattern[i]:
                return i
        return -1

    def mismatch_in_text(self, current_pos: int) -> int:
        """
        Desen ile metin karşılaştırıldığında, metindeki uyuşmayan karakterin indeksini bulur.

        Parametreler:
            current_pos (int): Metindeki mevcut indeks pozisyonu

        Dönüş:
            i (int): Metindeki uyuşmayan karakterin sonundan itibaren indeksi
            -1 (int): Desen ile metin bloğu arasında uyuşmazlık yoksa
        """

        for i in range(self.patLen - 1, -1, -1):
            if self.pattern[i] != self.text[current_pos + i]:
                return current_pos + i
        return -1

    def bad_character_heuristic(self) -> list[int]:
        # Deseni metinde arar ve indeks pozisyonlarını döner
        positions = []
        for i in range(self.textLen - self.patLen + 1):
            mismatch_index = self.mismatch_in_text(i)
            if mismatch_index == -1:
                positions.append(i)
            else:
                match_index = self.match_in_pattern(self.text[mismatch_index])
                i = (
                    mismatch_index - match_index
                )  # indeks kaydırma
        return positions


text = "ABAABA"
pattern = "AB"
bms = BoyerMooreSearch(text, pattern)
positions = bms.bad_character_heuristic()

if len(positions) == 0:
    print("Eşleşme bulunamadı")
else:
    print("Desen aşağıdaki pozisyonlarda bulundu: ")
    print(positions)
