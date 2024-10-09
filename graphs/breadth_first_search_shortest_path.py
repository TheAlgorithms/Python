"""Genişlik Öncelikli Arama (BFS), ağırlıksız bir grafikte verilen bir kaynak düğümden hedef düğüme en kısa yolu bulmak için kullanılabilir.
"""

from __future__ import annotations

graf = {
    "A": ["B", "C", "E"],
    "B": ["A", "D", "E"],
    "C": ["A", "F", "G"],
    "D": ["B"],
    "E": ["A", "B", "D"],
    "F": ["C"],
    "G": ["C"],
}

#Produced by K. Umut Araz 
class Graf:
    def __init__(self, graf: dict[str, list[str]], kaynak_düğüm: str) -> None:
        """
        Graf, komşuluk listelerinin bir sözlüğü olarak uygulanmıştır. Ayrıca,
        Kaynak düğüm başlatma sırasında tanımlanmalıdır.
        """
        self.graf = graf
        # düğümü, genişlik öncelikli ağaçta ebeveynine eşler
        self.ebeveyn: dict[str, str | None] = {}
        self.kaynak_düğüm = kaynak_düğüm

    def genişlik_öncelikli_arama(self) -> None:
        """
        Bu fonksiyon, bu graf üzerinde genişlik öncelikli arama çalıştırmak için bir yardımcıdır.
        >>> g = Graf(graf, "G")
        >>> g.genişlik_öncelikli_arama()
        >>> g.ebeveyn
        {'G': None, 'C': 'G', 'A': 'C', 'F': 'C', 'B': 'A', 'E': 'A', 'D': 'B'}
        """
        ziyaret_edilen = {self.kaynak_düğüm}
        self.ebeveyn[self.kaynak_düğüm] = None
        kuyruk = [self.kaynak_düğüm]  # ilk giren ilk çıkar kuyruğu

        while kuyruk:
            düğüm = kuyruk.pop(0)
            for komşu_düğüm in self.graf[düğüm]:
                if komşu_düğüm not in ziyaret_edilen:
                    ziyaret_edilen.add(komşu_düğüm)
                    self.ebeveyn[komşu_düğüm] = düğüm
                    kuyruk.append(komşu_düğüm)

    def en_kısa_yol(self, hedef_düğüm: str) -> str:
        """
        Bu en kısa yol fonksiyonu bir string döndürür ve sonucu açıklar:
        1.) Yol bulunamazsa. String, bunu belirtmek için insan tarafından okunabilir bir mesajdır.
        2.) En kısa yol bulunursa. String, `v1(->v2->v3->...->vn)` formundadır, burada v1 kaynak düğüm ve vn hedef düğümdür.

        >>> g = Graf(graf, "G")
        >>> g.genişlik_öncelikli_arama()

        Durum 1 - Yol bulunamaz.
        >>> g.en_kısa_yol("Foo")
        Traceback (most recent call last):
            ...
        ValueError: G düğümünden Foo düğümüne yol yok

        Durum 2 - Yol bulunur.
        >>> g.en_kısa_yol("D")
        'G->C->A->B->D'
        >>> g.en_kısa_yol("G")
        'G'
        """
        if hedef_düğüm == self.kaynak_düğüm:
            return self.kaynak_düğüm

        hedef_düğüm_ebeveyni = self.ebeveyn.get(hedef_düğüm)
        if hedef_düğüm_ebeveyni is None:
            msg = (
                f"G düğümünden {hedef_düğüm} düğümüne yol yok"
            )
            raise ValueError(msg)

        return self.en_kısa_yol(hedef_düğüm_ebeveyni) + f"->{hedef_düğüm}"


if __name__ == "__main__":
    g = Graf(graf, "G")
    g.genişlik_öncelikli_arama()
    print(g.en_kısa_yol("D"))
    print(g.en_kısa_yol("G"))
    try:
        print(g.en_kısa_yol("Foo"))
    except ValueError as e:
        print(e)
