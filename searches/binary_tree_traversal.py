"""
Bu, ağaç gezinti algoritmalarının saf Python uygulamasıdır.

Organiser: K. Umut Araz
"""

from __future__ import annotations

import queue


class AgacDugumu:
    def __init__(self, veri):
        self.veri = veri
        self.sag = None
        self.sol = None


def agaci_olustur() -> AgacDugumu:
    print("\n********Herhangi bir anda girişi durdurmak için N'ye basın********\n")
    kontrol = input("Kök düğümün değerini girin: ").strip().lower()
    q: queue.Queue = queue.Queue()
    agac_dugumu = AgacDugumu(int(kontrol))
    q.put(agac_dugumu)
    while not q.empty():
        bulunan_dugum = q.get()
        mesaj = f"{bulunan_dugum.veri} düğümünün sol düğümünü girin: "
        kontrol = input(mesaj).strip().lower() or "n"
        if kontrol == "n":
            return agac_dugumu
        sol_dugum = AgacDugumu(int(kontrol))
        bulunan_dugum.sol = sol_dugum
        q.put(sol_dugum)
        mesaj = f"{bulunan_dugum.veri} düğümünün sağ düğümünü girin: "
        kontrol = input(mesaj).strip().lower() or "n"
        if kontrol == "n":
            return agac_dugumu
        sag_dugum = AgacDugumu(int(kontrol))
        bulunan_dugum.sag = sag_dugum
        q.put(sag_dugum)
    raise ValueError("Bir şeyler yanlış gitti")


def oncelikli_gezinme(dugum: AgacDugumu) -> None:
    """
    >>> kok = AgacDugumu(1)
    >>> agac_dugumu2 = AgacDugumu(2)
    >>> agac_dugumu3 = AgacDugumu(3)
    >>> agac_dugumu4 = AgacDugumu(4)
    >>> agac_dugumu5 = AgacDugumu(5)
    >>> agac_dugumu6 = AgacDugumu(6)
    >>> agac_dugumu7 = AgacDugumu(7)
    >>> kok.sol, kok.sag = agac_dugumu2, agac_dugumu3
    >>> agac_dugumu2.sol, agac_dugumu2.sag = agac_dugumu4 , agac_dugumu5
    >>> agac_dugumu3.sol, agac_dugumu3.sag = agac_dugumu6 , agac_dugumu7
    >>> oncelikli_gezinme(kok)
    1,2,4,5,3,6,7,
    """
    if not isinstance(dugum, AgacDugumu) or not dugum:
        return
    print(dugum.veri, end=",")
    oncelikli_gezinme(dugum.sol)
    oncelikli_gezinme(dugum.sag)


def sirali_gezinme(dugum: AgacDugumu) -> None:
    """
    >>> kok = AgacDugumu(1)
    >>> agac_dugumu2 = AgacDugumu(2)
    >>> agac_dugumu3 = AgacDugumu(3)
    >>> agac_dugumu4 = AgacDugumu(4)
    >>> agac_dugumu5 = AgacDugumu(5)
    >>> agac_dugumu6 = AgacDugumu(6)
    >>> agac_dugumu7 = AgacDugumu(7)
    >>> kok.sol, kok.sag = agac_dugumu2, agac_dugumu3
    >>> agac_dugumu2.sol, agac_dugumu2.sag = agac_dugumu4 , agac_dugumu5
    >>> agac_dugumu3.sol, agac_dugumu3.sag = agac_dugumu6 , agac_dugumu7
    >>> sirali_gezinme(kok)
    4,2,5,1,6,3,7,
    """
    if not isinstance(dugum, AgacDugumu) or not dugum:
        return
    sirali_gezinme(dugum.sol)
    print(dugum.veri, end=",")
    sirali_gezinme(dugum.sag)


def sonlu_gezinme(dugum: AgacDugumu) -> None:
    """
    >>> kok = AgacDugumu(1)
    >>> agac_dugumu2 = AgacDugumu(2)
    >>> agac_dugumu3 = AgacDugumu(3)
    >>> agac_dugumu4 = AgacDugumu(4)
    >>> agac_dugumu5 = AgacDugumu(5)
    >>> agac_dugumu6 = AgacDugumu(6)
    >>> agac_dugumu7 = AgacDugumu(7)
    >>> kok.sol, kok.sag = agac_dugumu2, agac_dugumu3
    >>> agac_dugumu2.sol, agac_dugumu2.sag = agac_dugumu4 , agac_dugumu5
    >>> agac_dugumu3.sol, agac_dugumu3.sag = agac_dugumu6 , agac_dugumu7
    >>> sonlu_gezinme(kok)
    4,5,2,6,7,3,1,
    """
    if not isinstance(dugum, AgacDugumu) or not dugum:
        return
    sonlu_gezinme(dugum.sol)
    sonlu_gezinme(dugum.sag)
    print(dugum.veri, end=",")


def seviye_gezinme(dugum: AgacDugumu) -> None:
    """
    >>> kok = AgacDugumu(1)
    >>> agac_dugumu2 = AgacDugumu(2)
    >>> agac_dugumu3 = AgacDugumu(3)
    >>> agac_dugumu4 = AgacDugumu(4)
    >>> agac_dugumu5 = AgacDugumu(5)
    >>> agac_dugumu6 = AgacDugumu(6)
    >>> agac_dugumu7 = AgacDugumu(7)
    >>> kok.sol, kok.sag = agac_dugumu2, agac_dugumu3
    >>> agac_dugumu2.sol, agac_dugumu2.sag = agac_dugumu4 , agac_dugumu5
    >>> agac_dugumu3.sol, agac_dugumu3.sag = agac_dugumu6 , agac_dugumu7
    >>> seviye_gezinme(kok)
    1,2,3,4,5,6,7,
    """
    if not isinstance(dugum, AgacDugumu) or not dugum:
        return
    q: queue.Queue = queue.Queue()
    q.put(dugum)
    while not q.empty():
        cikan_dugum = q.get()
        print(cikan_dugum.veri, end=",")
        if cikan_dugum.sol:
            q.put(cikan_dugum.sol)
        if cikan_dugum.sag:
            q.put(cikan_dugum.sag)


def gercek_seviye_gezinme(dugum: AgacDugumu) -> None:
    """
    >>> kok = AgacDugumu(1)
    >>> agac_dugumu2 = AgacDugumu(2)
    >>> agac_dugumu3 = AgacDugumu(3)
    >>> agac_dugumu4 = AgacDugumu(4)
    >>> agac_dugumu5 = AgacDugumu(5)
    >>> agac_dugumu6 = AgacDugumu(6)
    >>> agac_dugumu7 = AgacDugumu(7)
    >>> kok.sol, kok.sag = agac_dugumu2, agac_dugumu3
    >>> agac_dugumu2.sol, agac_dugumu2.sag = agac_dugumu4 , agac_dugumu5
    >>> agac_dugumu3.sol, agac_dugumu3.sag = agac_dugumu6 , agac_dugumu7
    >>> gercek_seviye_gezinme(kok)
    1,
    2,3,
    4,5,6,7,
    """
    if not isinstance(dugum, AgacDugumu) or not dugum:
        return
    q: queue.Queue = queue.Queue()
    q.put(dugum)
    while not q.empty():
        liste = []
        while not q.empty():
            cikan_dugum = q.get()
            print(cikan_dugum.veri, end=",")
            if cikan_dugum.sol:
                liste.append(cikan_dugum.sol)
            if cikan_dugum.sag:
                liste.append(cikan_dugum.sag)
        print()
        for ic_dugum in liste:
            q.put(ic_dugum)


# yineleme versiyonu
def oncelikli_gezinme_iter(dugum: AgacDugumu) -> None:
    """
    >>> kok = AgacDugumu(1)
    >>> agac_dugumu2 = AgacDugumu(2)
    >>> agac_dugumu3 = AgacDugumu(3)
    >>> agac_dugumu4 = AgacDugumu(4)
    >>> agac_dugumu5 = AgacDugumu(5)
    >>> agac_dugumu6 = AgacDugumu(6)
    >>> agac_dugumu7 = AgacDugumu(7)
    >>> kok.sol, kok.sag = agac_dugumu2, agac_dugumu3
    >>> agac_dugumu2.sol, agac_dugumu2.sag = agac_dugumu4 , agac_dugumu5
    >>> agac_dugumu3.sol, agac_dugumu3.sag = agac_dugumu6 , agac_dugumu7
    >>> oncelikli_gezinme_iter(kok)
    1,2,4,5,3,6,7,
    """
    if not isinstance(dugum, AgacDugumu) or not dugum:
        return
    yigin: list[AgacDugumu] = []
    n = dugum
    while n or yigin:
        while n:  # kök düğümden başlayarak sol çocuğu bul
            print(n.veri, end=",")
            yigin.append(n)
            n = n.sol
        # while döngüsünün sonu, mevcut düğümün sol çocuğu olmadığını gösterir
        n = yigin.pop()
        # sağ çocuğu gezmeye başla
        n = n.sag


def sirali_gezinme_iter(dugum: AgacDugumu) -> None:
    """
    >>> kok = AgacDugumu(1)
    >>> agac_dugumu2 = AgacDugumu(2)
    >>> agac_dugumu3 = AgacDugumu(3)
    >>> agac_dugumu4 = AgacDugumu(4)
    >>> agac_dugumu5 = AgacDugumu(5)
    >>> agac_dugumu6 = AgacDugumu(6)
    >>> agac_dugumu7 = AgacDugumu(7)
    >>> kok.sol, kok.sag = agac_dugumu2, agac_dugumu3
    >>> agac_dugumu2.sol, agac_dugumu2.sag = agac_dugumu4 , agac_dugumu5
    >>> agac_dugumu3.sol, agac_dugumu3.sag = agac_dugumu6 , agac_dugumu7
    >>> sirali_gezinme_iter(kok)
    4,2,5,1,6,3,7,
    """
    if not isinstance(dugum, AgacDugumu) or not dugum:
        return
    yigin: list[AgacDugumu] = []
    n = dugum
    while n or yigin:
        while n:
            yigin.append(n)
            n = n.sol
        n = yigin.pop()
        print(n.veri, end=",")
        n = n.sag


def sonlu_gezinme_iter(dugum: AgacDugumu) -> None:
    """
    >>> kok = AgacDugumu(1)
    >>> agac_dugumu2 = AgacDugumu(2)
    >>> agac_dugumu3 = AgacDugumu(3)
    >>> agac_dugumu4 = AgacDugumu(4)
    >>> agac_dugumu5 = AgacDugumu(5)
    >>> agac_dugumu6 = AgacDugumu(6)
    >>> agac_dugumu7 = AgacDugumu(7)
    >>> kok.sol, kok.sag = agac_dugumu2, agac_dugumu3
    >>> agac_dugumu2.sol, agac_dugumu2.sag = agac_dugumu4 , agac_dugumu5
    >>> agac_dugumu3.sol, agac_dugumu3.sag = agac_dugumu6 , agac_dugumu7
    >>> sonlu_gezinme_iter(kok)
    4,5,2,6,7,3,1,
    """
    if not isinstance(dugum, AgacDugumu) or not dugum:
        return
    yigin1, yigin2 = [], []
    n = dugum
    yigin1.append(n)
    while yigin1:  # sonlu gezintinin ters sırasını bulmak için yigin2'ye kaydet
        n = yigin1.pop()
        if n.sol:
            yigin1.append(n.sol)
        if n.sag:
            yigin1.append(n.sag)
        yigin2.append(n)
    while yigin2:  # yigin2'den çıkmak sonlu gezintiyi verecektir
        print(yigin2.pop().veri, end=",")


def istem(s: str = "", genislik=50, karakter="*") -> str:
    if not s:
        return "\n" + genislik * karakter
    sol, fazlalik = divmod(genislik - len(s) - 2, 2)
    return f"{sol * karakter} {s} {(sol + fazlalik) * karakter}"


