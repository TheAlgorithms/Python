from collections import deque
from math import floor
from random import random
from time import time

# varsayılan ağırlık atanmazsa 1'dir, ancak tüm uygulama ağırlıklıdır


class YonluGrafik:
    def __init__(self):
        self.grafik = {}

    # düğümler ve kenarlar ekleme
    # ağırlık eklemek isteğe bağlıdır
    # tekrarları yönetir
    def cift_ekle(self, u, v, w=1):
        if self.grafik.get(u):
            if self.grafik[u].count([w, v]) == 0:
                self.grafik[u].append([w, v])
        else:
            self.grafik[u] = [[w, v]]
        if not self.grafik.get(v):
            self.grafik[v] = []

    def tum_dugumler(self):
        return list(self.grafik)

    # giriş yoksa yönetir
    def cift_sil(self, u, v):
        if self.grafik.get(u):
            for _ in self.grafik[u]:
                if _[1] == v:
                    self.grafik[u].remove(_)

    # eğer hedef belirtilmemişse varsayılan değer -1'dir
    def dfs(self, s=-2, d=-1):
        if s == d:
            return []
        yigin = []
        ziyaret_edilen = []
        if s == -2:
            s = next(iter(self.grafik))
        yigin.append(s)
        ziyaret_edilen.append(s)
        ss = s

        while True:
            # izole olmayan düğümler olup olmadığını kontrol et
            if len(self.grafik[s]) != 0:
                ss = s
                for dugum in self.grafik[s]:
                    if ziyaret_edilen.count(dugum[1]) < 1:
                        if dugum[1] == d:
                            ziyaret_edilen.append(d)
                            return ziyaret_edilen
                        else:
                            yigin.append(dugum[1])
                            ziyaret_edilen.append(dugum[1])
                            ss = dugum[1]
                            break

            # tüm çocukların ziyaret edilip edilmediğini kontrol et
            if s == ss:
                yigin.pop()
                if len(yigin) != 0:
                    s = yigin[len(yigin) - 1]
            else:
                s = ss

            # başlangıç noktasına ulaşıp ulaşmadığımızı kontrol et
            if len(yigin) == 0:
                return ziyaret_edilen

    # c, istediğiniz düğüm sayısıdır ve eğer bırakır veya fonksiyona -1 geçirirseniz
    # sayı rastgele 10 ile 10000 arasında olacaktır
    def grafiği_rastgele_doldur(self, c=-1):
        if c == -1:
            c = floor(random() * 10000) + 10
        for i in range(c):
            # her düğümün maksimum 100 kenarı vardır
            for _ in range(floor(random() * 102) + 1):
                n = floor(random() * c) + 1
                if n != i:
                    self.cift_ekle(i, n, 1)

    def bfs(self, s=-2):
        d = deque()
        ziyaret_edilen = []
        if s == -2:
            s = next(iter(self.grafik))
        d.append(s)
        ziyaret_edilen.append(s)
        while d:
            s = d.popleft()
            if len(self.grafik[s]) != 0:
                for dugum in self.grafik[s]:
                    if ziyaret_edilen.count(dugum[1]) < 1:
                        d.append(dugum[1])
                        ziyaret_edilen.append(dugum[1])
        return ziyaret_edilen

    def giris_derecesi(self, u):
        sayac = 0
        for x in self.grafik:
            for y in self.grafik[x]:
                if y[1] == u:
                    sayac += 1
        return sayac

    def cikis_derecesi(self, u):
        return len(self.grafik[u])

    def topolojik_siralama(self, s=-2):
        yigin = []
        ziyaret_edilen = []
        if s == -2:
            s = next(iter(self.grafik))
        yigin.append(s)
        ziyaret_edilen.append(s)
        ss = s
        sirali_dugumler = []

        while True:
            # izole olmayan düğümler olup olmadığını kontrol et
            if len(self.grafik[s]) != 0:
                ss = s
                for dugum in self.grafik[s]:
                    if ziyaret_edilen.count(dugum[1]) < 1:
                        yigin.append(dugum[1])
                        ziyaret_edilen.append(dugum[1])
                        ss = dugum[1]
                        break

            # tüm çocukların ziyaret edilip edilmediğini kontrol et
            if s == ss:
                sirali_dugumler.append(yigin.pop())
                if len(yigin) != 0:
                    s = yigin[len(yigin) - 1]
            else:
                s = ss

            # başlangıç noktasına ulaşıp ulaşmadığımızı kontrol et
            if len(yigin) == 0:
                return sirali_dugumler

    def dongu_dugumleri(self):
        yigin = []
        ziyaret_edilen = []
        s = next(iter(self.grafik))
        yigin.append(s)
        ziyaret_edilen.append(s)
        ebeveyn = -2
        dolayli_ebeveynler = []
        ss = s
        geri_donuste = False
        beklenen_dugumler = set()

        while True:
            # izole olmayan düğümler olup olmadığını kontrol et
            if len(self.grafik[s]) != 0:
                ss = s
                for dugum in self.grafik[s]:
                    if (
                        ziyaret_edilen.count(dugum[1]) > 0
                        and dugum[1] != ebeveyn
                        and dolayli_ebeveynler.count(dugum[1]) > 0
                        and not geri_donuste
                    ):
                        yigin_uzunluk = len(yigin) - 1
                        while yigin_uzunluk >= 0:
                            if yigin[yigin_uzunluk] == dugum[1]:
                                beklenen_dugumler.add(dugum[1])
                                break
                            else:
                                beklenen_dugumler.add(yigin[yigin_uzunluk])
                                yigin_uzunluk -= 1
                    if ziyaret_edilen.count(dugum[1]) < 1:
                        yigin.append(dugum[1])
                        ziyaret_edilen.append(dugum[1])
                        ss = dugum[1]
                        break

            # tüm çocukların ziyaret edilip edilmediğini kontrol et
            if s == ss:
                yigin.pop()
                geri_donuste = True
                if len(yigin) != 0:
                    s = yigin[len(yigin) - 1]
            else:
                geri_donuste = False
                dolayli_ebeveynler.append(ebeveyn)
                ebeveyn = s
                s = ss

            # başlangıç noktasına ulaşıp ulaşmadığımızı kontrol et
            if len(yigin) == 0:
                return list(beklenen_dugumler)

    def dongu_var_mi(self):
        yigin = []
        ziyaret_edilen = []
        s = next(iter(self.grafik))
        yigin.append(s)
        ziyaret_edilen.append(s)
        ebeveyn = -2
        dolayli_ebeveynler = []
        ss = s
        geri_donuste = False

        while True:
            # izole olmayan düğümler olup olmadığını kontrol et
            if len(self.grafik[s]) != 0:
                ss = s
                for dugum in self.grafik[s]:
                    if (
                        ziyaret_edilen.count(dugum[1]) > 0
                        and dugum[1] != ebeveyn
                        and dolayli_ebeveynler.count(dugum[1]) > 0
                        and not geri_donuste
                    ):
                        yigin_uzunluk_eksi_bir = len(yigin) - 1
                        while yigin_uzunluk_eksi_bir >= 0:
                            if yigin[yigin_uzunluk_eksi_bir] == dugum[1]:
                                return True
                    if ziyaret_edilen.count(dugum[1]) < 1:
                        yigin.append(dugum[1])
                        ziyaret_edilen.append(dugum[1])
                        ss = dugum[1]
                        break

            # tüm çocukların ziyaret edilip edilmediğini kontrol et
            if s == ss:
                yigin.pop()
                geri_donuste = True
                if len(yigin) != 0:
                    s = yigin[len(yigin) - 1]
            else:
                geri_donuste = False
                dolayli_ebeveynler.append(ebeveyn)
                ebeveyn = s
                s = ss

            # başlangıç noktasına ulaşıp ulaşmadığımızı kontrol et
            if len(yigin) == 0:
                return False

    def dfs_suresi(self, s=-2, e=-1):
        baslangic = time()
        self.dfs(s, e)
        bitis = time()
        return bitis - baslangic

    def bfs_suresi(self, s=-2):
        baslangic = time()
        self.bfs(s)
        bitis = time()
        return bitis - baslangic


class Grafik:
    def __init__(self):
        self.grafik = {}

    # düğümler ve kenarlar ekleme
    # ağırlık eklemek isteğe bağlıdır
    # tekrarları yönetir
    def cift_ekle(self, u, v, w=1):
        # u'nun var olup olmadığını kontrol et
        if self.grafik.get(u):
            # zaten bir kenar varsa
            if self.grafik[u].count([w, v]) == 0:
                self.grafik[u].append([w, v])
        else:
            # u yoksa
            self.grafik[u] = [[w, v]]
        # diğer yolu ekle
        if self.grafik.get(v):
            # zaten bir kenar varsa
            if self.grafik[v].count([w, u]) == 0:
                self.grafik[v].append([w, u])
        else:
            # u yoksa
            self.grafik[v] = [[w, u]]

    # giriş yoksa yönetir
    def cift_sil(self, u, v):
        if self.grafik.get(u):
            for _ in self.grafik[u]:
                if _[1] == v:
                    self.grafik[u].remove(_)
        # diğer yolu da sil
        if self.grafik.get(v):
            for _ in self.grafik[v]:
                if _[1] == u:
                    self.grafik[v].remove(_)

    # eğer hedef belirtilmemişse varsayılan değer -1'dir
    def dfs(self, s=-2, d=-1):
        if s == d:
            return []
        yigin = []
        ziyaret_edilen = []
        if s == -2:
            s = next(iter(self.grafik))
        yigin.append(s)
        ziyaret_edilen.append(s)
        ss = s

        while True:
            # izole olmayan düğümler olup olmadığını kontrol et
            if len(self.grafik[s]) != 0:
                ss = s
                for dugum in self.grafik[s]:
                    if ziyaret_edilen.count(dugum[1]) < 1:
                        if dugum[1] == d:
                            ziyaret_edilen.append(d)
                            return ziyaret_edilen
                        else:
                            yigin.append(dugum[1])
                            ziyaret_edilen.append(dugum[1])
                            ss = dugum[1]
                            break

            # tüm çocukların ziyaret edilip edilmediğini kontrol et
            if s == ss:
                yigin.pop()
                if len(yigin) != 0:
                    s = yigin[len(yigin) - 1]
            else:
                s = ss

            # başlangıç noktasına ulaşıp ulaşmadığımızı kontrol et
            if len(yigin) == 0:
                return ziyaret_edilen

    # c, istediğiniz düğüm sayısıdır ve eğer bırakır veya fonksiyona -1 geçirirseniz
    # sayı rastgele 10 ile 10000 arasında olacaktır
    def grafiği_rastgele_doldur(self, c=-1):
        if c == -1:
            c = floor(random() * 10000) + 10
        for i in range(c):
            # her düğümün maksimum 100 kenarı vardır
            for _ in range(floor(random() * 102) + 1):
                n = floor(random() * c) + 1
                if n != i:
                    self.cift_ekle(i, n, 1)

    def bfs(self, s=-2):
        d = deque()
        ziyaret_edilen = []
        if s == -2:
            s = next(iter(self.grafik))
        d.append(s)
        ziyaret_edilen.append(s)
        while d:
            s = d.popleft()
            if len(self.grafik[s]) != 0:
                for dugum in self.grafik[s]:
                    if ziyaret_edilen.count(dugum[1]) < 1:
                        d.append(dugum[1])
                        ziyaret_edilen.append(dugum[1])
        return ziyaret_edilen

    def derece(self, u):
        return len(self.grafik[u])

    def dongu_dugumleri(self):
        yigin = []
        ziyaret_edilen = []
        s = next(iter(self.grafik))
        yigin.append(s)
        ziyaret_edilen.append(s)
        ebeveyn = -2
        dolayli_ebeveynler = []
        ss = s
        geri_donuste = False
        beklenen_dugumler = set()

        while True:
            # izole olmayan düğümler olup olmadığını kontrol et
            if len(self.grafik[s]) != 0:
                ss = s
                for dugum in self.grafik[s]:
                    if (
                        ziyaret_edilen.count(dugum[1]) > 0
                        and dugum[1] != ebeveyn
                        and dolayli_ebeveynler.count(dugum[1]) > 0
                        and not geri_donuste
                    ):
                        yigin_uzunluk = len(yigin) - 1
                        while yigin_uzunluk >= 0:
                            if yigin[yigin_uzunluk] == dugum[1]:
                                beklenen_dugumler.add(dugum[1])
                                break
                            else:
                                beklenen_dugumler.add(yigin[yigin_uzunluk])
                                yigin_uzunluk -= 1
                    if ziyaret_edilen.count(dugum[1]) < 1:
                        yigin.append(dugum[1])
                        ziyaret_edilen.append(dugum[1])
                        ss = dugum[1]
                        break

            # tüm çocukların ziyaret edilip edilmediğini kontrol et
            if s == ss:
                yigin.pop()
                geri_donuste = True
                if len(yigin) != 0:
                    s = yigin[len(yigin) - 1]
            else:
                geri_donuste = False
                dolayli_ebeveynler.append(ebeveyn)
                ebeveyn = s
                s = ss

            # başlangıç noktasına ulaşıp ulaşmadığımızı kontrol et
            if len(yigin) == 0:
                return list(beklenen_dugumler)

    def dongu_var_mi(self):
        yigin = []
        ziyaret_edilen = []
        s = next(iter(self.grafik))
        yigin.append(s)
        ziyaret_edilen.append(s)
        ebeveyn = -2
        dolayli_ebeveynler = []
        ss = s
        geri_donuste = False

        while True:
            # izole olmayan düğümler olup olmadığını kontrol et
            if len(self.grafik[s]) != 0:
                ss = s
                for dugum in self.grafik[s]:
                    if (
                        ziyaret_edilen.count(dugum[1]) > 0
                        and dugum[1] != ebeveyn
                        and dolayli_ebeveynler.count(dugum[1]) > 0
                        and not geri_donuste
                    ):
                        yigin_uzunluk_eksi_bir = len(yigin) - 1
                        while yigin_uzunluk_eksi_bir >= 0:
                            if yigin[yigin_uzunluk_eksi_bir] == dugum[1]:
                                return True
                    if ziyaret_edilen.count(dugum[1]) < 1:
                        yigin.append(dugum[1])
                        ziyaret_edilen.append(dugum[1])
                        ss = dugum[1]
                        break

            # tüm çocukların ziyaret edilip edilmediğini kontrol et
            if s == ss:
                yigin.pop()
                geri_donuste = True
                if len(yigin) != 0:
                    s = yigin[len(yigin) - 1]
            else:
                geri_donuste = False
                dolayli_ebeveynler.append(ebeveyn)
                ebeveyn = s
                s = ss

            # başlangıç noktasına ulaşıp ulaşmadığımızı kontrol et
            if len(yigin) == 0:
                return False

    def tum_dugumler(self):
        return list(self.grafik)

    def dfs_suresi(self, s=-2, e=-1):
        baslangic = time()
        self.dfs(s, e)
        bitis = time()
        return bitis - baslangic

    def bfs_suresi(self, s=-2):
        baslangic = time()
        self.bfs(s)
        bitis = time()
        return bitis - baslangic
