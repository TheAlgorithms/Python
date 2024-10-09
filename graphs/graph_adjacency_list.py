#!/usr/bin/env python3
"""
Yazar: Vikram Nithyanandam

Açıklama:
Aşağıdaki uygulama, bir komşuluk listesi kullanılarak uygulanmış sağlam bir ağırlıksız Grafik veri yapısıdır.
Bu grafiğin düğümleri ve kenarları, her düğümde seçtiğiniz genel değeri saklarken etkili bir şekilde başlatılabilir ve değiştirilebilir.

Komşuluk Listesi: https://en.wikipedia.org/wiki/Adjacency_list

Gelecekteki Potansiyel Fikirler:
- Kenar ağırlıklarını ayarlamak ve kenar ağırlıklarını belirlemek için bir bayrak ekleyin
- Kenar ağırlıklarını ve düğüm değerlerini, müşterinin istediği herhangi bir şeyi saklayacak şekilde özelleştirilebilir hale getirin
- Müşteri isterse çoklu grafik işlevselliğini destekleyin
"""

from __future__ import annotations

import random
import unittest
from pprint import pformat
from typing import Generic, TypeVar

import pytest

T = TypeVar("T")


class KomşulukListesiGrafiği(Generic[T]):
    def __init__(
        self, düğümler: list[T], kenarlar: list[list[T]], yönlü: bool = True
    ) -> None:
        """
        Parametreler:
         - düğümler: (list[T]) Müşterinin geçirmek istediği düğüm adlarının listesi. Varsayılan boş.
         - kenarlar: (list[list[T]]) Müşterinin geçirmek istediği kenarların listesi. Her kenar 2 elemanlı bir listedir. Varsayılan boş.
         - yönlü: (bool) Grafiğin yönlü veya yönsüz olduğunu belirtir. Varsayılan True.
        """
        self.komşuluk_listesi: dict[T, list[T]] = {}  # T türünde listelerin sözlüğü
        self.yönlü = yönlü

        # Boşluk kontrolleri
        kenarlar = kenarlar or []
        düğümler = düğümler or []

        for düğüm in düğümler:
            self.düğüm_ekle(düğüm)

        for kenar in kenarlar:
            if len(kenar) != 2:
                msg = f"Geçersiz giriş: {kenar} yanlış uzunlukta."
                raise ValueError(msg)
            self.kenar_ekle(kenar[0], kenar[1])

    def düğüm_ekle(self, düğüm: T) -> None:
        """
        Grafa bir düğüm ekler. Verilen düğüm zaten mevcutsa, bir ValueError fırlatılır.
        """
        if self.düğüm_var_mı(düğüm):
            msg = f"Yanlış giriş: {düğüm} zaten grafikte mevcut."
            raise ValueError(msg)
        self.komşuluk_listesi[düğüm] = []

    def kenar_ekle(self, kaynak_düğüm: T, hedef_düğüm: T) -> None:
        """
        Kaynak düğümden hedef düğüme bir kenar oluşturur. Verilen herhangi bir düğüm mevcut değilse veya kenar zaten mevcutsa, bir ValueError fırlatılır.
        """
        if not (
            self.düğüm_var_mı(kaynak_düğüm)
            and self.düğüm_var_mı(hedef_düğüm)
        ):
            msg = (
                f"Yanlış giriş: {kaynak_düğüm} veya "
                f"{hedef_düğüm} mevcut değil"
            )
            raise ValueError(msg)
        if self.kenar_var_mı(kaynak_düğüm, hedef_düğüm):
            msg = (
                "Yanlış giriş: "
                f"{kaynak_düğüm} ve {hedef_düğüm} arasında kenar zaten mevcut"
            )
            raise ValueError(msg)

        # kaynak düğümle ilişkili listeye hedef düğümü ekleyin
        # ve yönlü değilse tersi
        self.komşuluk_listesi[kaynak_düğüm].append(hedef_düğüm)
        if not self.yönlü:
            self.komşuluk_listesi[hedef_düğüm].append(kaynak_düğüm)

    def düğüm_sil(self, düğüm: T) -> None:
        """
        Verilen düğümü grafikten kaldırır ve verilen düğümden gelen ve giden tüm kenarları siler. Verilen düğüm mevcut değilse, bir ValueError fırlatılır.
        """
        if not self.düğüm_var_mı(düğüm):
            msg = f"Yanlış giriş: {düğüm} bu grafikte mevcut değil."
            raise ValueError(msg)

        if not self.yönlü:
            # Yönlü değilse, tüm komşu düğümleri bulun ve verilen düğüme bağlanan tüm kenarların referanslarını silin
            for komşu in self.komşuluk_listesi[düğüm]:
                self.komşuluk_listesi[komşu].remove(düğüm)
        else:
            # Yönlü ise, tüm düğümlerin tüm komşularını arayın ve verilen düğüme bağlanan tüm kenarların referanslarını silin
            for kenar_listesi in self.komşuluk_listesi.values():
                if düğüm in kenar_listesi:
                    kenar_listesi.remove(düğüm)

        # Son olarak, verilen düğümü ve tüm giden kenar referanslarını silin
        self.komşuluk_listesi.pop(düğüm)

    def kenar_sil(self, kaynak_düğüm: T, hedef_düğüm: T) -> None:
        """
        İki düğüm arasındaki kenarı kaldırır. Verilen herhangi bir düğüm mevcut değilse veya kenar mevcut değilse, bir ValueError fırlatılır.
        """
        if not (
            self.düğüm_var_mı(kaynak_düğüm)
            and self.düğüm_var_mı(hedef_düğüm)
        ):
            msg = (
                f"Yanlış giriş: {kaynak_düğüm} veya "
                f"{hedef_düğüm} mevcut değil"
            )
            raise ValueError(msg)
        if not self.kenar_var_mı(kaynak_düğüm, hedef_düğüm):
            msg = (
                "Yanlış giriş: "
                f"{kaynak_düğüm} ve {hedef_düğüm} arasında kenar mevcut değil"
            )
            raise ValueError(msg)

        # kaynak düğümle ilişkili listeden hedef düğümü kaldırın
        # ve yönlü değilse tersi
        self.komşuluk_listesi[kaynak_düğüm].remove(hedef_düğüm)
        if not self.yönlü:
            self.komşuluk_listesi[hedef_düğüm].remove(kaynak_düğüm)

    def düğüm_var_mı(self, düğüm: T) -> bool:
        """
        Grafikte düğüm varsa True, yoksa False döner.
        """
        return düğüm in self.komşuluk_listesi

    def kenar_var_mı(self, kaynak_düğüm: T, hedef_düğüm: T) -> bool:
        """
        Grafikte kaynak_düğümden hedef_düğüme kenar varsa True, yoksa False döner. Verilen herhangi bir düğüm mevcut değilse, bir ValueError fırlatılır.
        """
        if not (
            self.düğüm_var_mı(kaynak_düğüm)
            and self.düğüm_var_mı(hedef_düğüm)
        ):
            msg = (
                f"Yanlış giriş: {kaynak_düğüm} "
                f"veya {hedef_düğüm} mevcut değil."
            )
            raise ValueError(msg)

        return hedef_düğüm in self.komşuluk_listesi[kaynak_düğüm]

    def grafiği_temizle(self) -> None:
        """
        Tüm düğümleri ve kenarları temizler.
        """
        self.komşuluk_listesi = {}

    def __repr__(self) -> str:
        return pformat(self.komşuluk_listesi)


class TestKomşulukListesiGrafiği(unittest.TestCase):
    def __kenar_var_mı_kontrol(
        self,
        yönsüz_grafik: KomşulukListesiGrafiği,
        yönlü_grafik: KomşulukListesiGrafiği,
        kenar: list[int],
    ) -> None:
        assert yönsüz_grafik.kenar_var_mı(kenar[0], kenar[1])
        assert yönsüz_grafik.kenar_var_mı(kenar[1], kenar[0])
        assert yönlü_grafik.kenar_var_mı(kenar[0], kenar[1])

    def __kenar_yok_kontrol(
        self,
        yönsüz_grafik: KomşulukListesiGrafiği,
        yönlü_grafik: KomşulukListesiGrafiği,
        kenar: list[int],
    ) -> None:
        assert not yönsüz_grafik.kenar_var_mı(kenar[0], kenar[1])
        assert not yönsüz_grafik.kenar_var_mı(kenar[1], kenar[0])
        assert not yönlü_grafik.kenar_var_mı(kenar[0], kenar[1])

    def __düğüm_var_mı_kontrol(
        self,
        yönsüz_grafik: KomşulukListesiGrafiği,
        yönlü_grafik: KomşulukListesiGrafiği,
        düğüm: int,
    ) -> None:
        assert yönsüz_grafik.düğüm_var_mı(düğüm)
        assert yönlü_grafik.düğüm_var_mı(düğüm)

    def __düğüm_yok_kontrol(
        self,
        yönsüz_grafik: KomşulukListesiGrafiği,
        yönlü_grafik: KomşulukListesiGrafiği,
        düğüm: int,
    ) -> None:
        assert not yönsüz_grafik.düğüm_var_mı(düğüm)
        assert not yönlü_grafik.düğüm_var_mı(düğüm)

    def __rastgele_kenarlar_oluştur(
        self, düğümler: list[int], kenar_sayısı: int
    ) -> list[list[int]]:
        assert kenar_sayısı <= len(düğümler)

        rastgele_kaynak_düğümler: list[int] = random.sample(
            düğümler[0 : int(len(düğümler) / 2)], kenar_sayısı
        )
        rastgele_hedef_düğümler: list[int] = random.sample(
            düğümler[int(len(düğümler) / 2) :], kenar_sayısı
        )
        rastgele_kenarlar: list[list[int]] = []

        for kaynak in rastgele_kaynak_düğümler:
            for hedef in rastgele_hedef_düğümler:
                rastgele_kenarlar.append([kaynak, hedef])

        return rastgele_kenarlar

    def __grafikler_oluştur(
        self, düğüm_sayısı: int, min_değer: int, max_değer: int, kenar_sayısı: int
    ) -> tuple[KomşulukListesiGrafiği, KomşulukListesiGrafiği, list[int], list[list[int]]]:
        if max_değer - min_değer + 1 < düğüm_sayısı:
            raise ValueError(
                "Yinelenen düğümler oluşacak. Ya min_değer ve max_değer arasındaki aralığı artırın ya da düğüm sayısını azaltın."
            )

        # grafik girişi oluştur
        rastgele_düğümler: list[int] = random.sample(
            range(min_değer, max_değer + 1), düğüm_sayısı
        )
        rastgele_kenarlar: list[list[int]] = self.__rastgele_kenarlar_oluştur(
            rastgele_düğümler, kenar_sayısı
        )

        # grafikler oluştur
        yönsüz_grafik = KomşulukListesiGrafiği(
            düğümler=rastgele_düğümler, kenarlar=rastgele_kenarlar, yönlü=False
        )
        yönlü_grafik = KomşulukListesiGrafiği(
            düğümler=rastgele_düğümler, kenarlar=rastgele_kenarlar, yönlü=True
        )

        return yönsüz_grafik, yönlü_grafik, rastgele_düğümler, rastgele_kenarlar

    def test_başlangıç_kontrol(self) -> None:
        (
            yönsüz_grafik,
            yönlü_grafik,
            rastgele_düğümler,
            rastgele_kenarlar,
        ) = self.__grafikler_oluştur(20, 0, 100, 4)

        # düğümler ve kenarlarla grafik başlatma testi
        for num in rastgele_düğümler:
            self.__düğüm_var_mı_kontrol(
                yönsüz_grafik, yönlü_grafik, num
            )

        for kenar in rastgele_kenarlar:
            self.__kenar_var_mı_kontrol(
                yönsüz_grafik, yönlü_grafik, kenar
            )
        assert not yönsüz_grafik.yönlü
        assert yönlü_grafik.yönlü

    def test_düğüm_var_mı(self) -> None:
        rastgele_düğümler: list[int] = random.sample(range(101), 20)

        # Kenar OLMADAN grafikler oluştur
        yönsüz_grafik = KomşulukListesiGrafiği(
            düğümler=rastgele_düğümler, kenarlar=[], yönlü=False
        )
        yönlü_grafik = KomşulukListesiGrafiği(
            düğümler=rastgele_düğümler, kenarlar=[], yönlü=True
        )

        # düğüm_var_mı test et
        for num in range(101):
            assert (num in rastgele_düğümler) == yönsüz_grafik.düğüm_var_mı(num)
            assert (num in rastgele_düğümler) == yönlü_grafik.düğüm_var_mı(num)

    def test_düğüm_ekle(self) -> None:
        rastgele_düğümler: list[int] = random.sample(range(101), 20)

        # boş grafikler oluştur
        yönsüz_grafik: KomşulukListesiGrafiği = KomşulukListesiGrafiği(
            düğümler=[], kenarlar=[], yönlü=False
        )
        yönlü_grafik: KomşulukListesiGrafiği = KomşulukListesiGrafiği(
            düğümler=[], kenarlar=[], yönlü=True
        )

        # düğüm_ekle çalıştır
        for num in rastgele_düğümler:
            yönsüz_grafik.düğüm_ekle(num)

        for num in rastgele_düğümler:
            yönlü_grafik.düğüm_ekle(num)

        # düğüm_ekle çalıştı mı test et
        for num in rastgele_düğümler:
            self.__düğüm_var_mı_kontrol(
                yönsüz_grafik, yönlü_grafik, num
            )

    def test_düğüm_sil(self) -> None:
        rastgele_düğümler: list[int] = random.sample(range(101), 20)

        # Kenar OLMADAN grafikler oluştur
        yönsüz_grafik = KomşulukListesiGrafiği(
            düğümler=rastgele_düğümler, kenarlar=[], yönlü=False
        )
        yönlü_grafik = KomşulukListesiGrafiği(
            düğümler=rastgele_düğümler, kenarlar=[], yönlü=True
        )

        # düğüm_sil çalıştı mı test et
        for num in rastgele_düğümler:
            self.__düğüm_var_mı_kontrol(
                yönsüz_grafik, yönlü_grafik, num
            )

            yönsüz_grafik.düğüm_sil(num)
            yönlü_grafik.düğüm_sil(num)

            self.__düğüm_yok_kontrol(
                yönsüz_grafik, yönlü_grafik, num
            )

    def test_düğüm_ekle_ve_sil_tekrar(self) -> None:
        rastgele_düğümler1: list[int] = random.sample(range(51), 20)
        rastgele_düğümler2: list[int] = random.sample(range(51, 101), 20)

        # Kenar OLMADAN grafikler oluştur
        yönsüz_grafik = KomşulukListesiGrafiği(
            düğümler=rastgele_düğümler1, kenarlar=[], yönlü=False
        )
        yönlü_grafik = KomşulukListesiGrafiği(
            düğümler=rastgele_düğümler1, kenarlar=[], yönlü=True
        )

        # düğüm ekleme ve silme testi
        for i, _ in enumerate(rastgele_düğümler1):
            yönsüz_grafik.düğüm_ekle(rastgele_düğümler2[i])
            yönlü_grafik.düğüm_ekle(rastgele_düğümler2[i])

            self.__düğüm_var_mı_kontrol(
                yönsüz_grafik, yönlü_grafik, rastgele_düğümler2[i]
            )

            yönsüz_grafik.düğüm_sil(rastgele_düğümler1[i])
            yönlü_grafik.düğüm_sil(rastgele_düğümler1[i])

            self.__düğüm_yok_kontrol(
                yönsüz_grafik, yönlü_grafik, rastgele_düğümler1[i]
            )

        # tüm düğümleri sil
        for i, _ in enumerate(rastgele_düğümler1):
            yönsüz_grafik.düğüm_sil(rastgele_düğümler2[i])
            yönlü_grafik.düğüm_sil(rastgele_düğümler2[i])

            self.__düğüm_yok_kontrol(
                yönsüz_grafik, yönlü_grafik, rastgele_düğümler2[i]
            )

    def test_kenar_var_mı(self) -> None:
        # grafikler ve grafik girişi oluştur
        düğüm_sayısı = 20
        (
            yönsüz_grafik,
            yönlü_grafik,
            rastgele_düğümler,
            rastgele_kenarlar,
        ) = self.__grafikler_oluştur(düğüm_sayısı, 0, 100, 4)

        # test için tüm olası kenarları oluştur
        tüm_olası_kenarlar: list[list[int]] = []
    def test_contains_edge(self) -> None:
        # generate graphs and graph input
        vertex_count = 20
        (
            undirected_graph,
            directed_graph,
            random_vertices,
            random_edges,
        ) = self.__generate_graphs(vertex_count, 0, 100, 4)

        # generate all possible edges for testing
        all_possible_edges: list[list[int]] = []
        for i in range(vertex_count - 1):
            for j in range(i + 1, vertex_count):
                all_possible_edges.append([random_vertices[i], random_vertices[j]])
                all_possible_edges.append([random_vertices[j], random_vertices[i]])

        # test contains_edge function
        for edge in all_possible_edges:
            if edge in random_edges:
                self.__assert_graph_edge_exists_check(
                    undirected_graph, directed_graph, edge
                )
            elif [edge[1], edge[0]] in random_edges:
                # since this edge exists for undirected but the reverse
                # may not exist for directed
                self.__assert_graph_edge_exists_check(
                    undirected_graph, directed_graph, [edge[1], edge[0]]
                )
            else:
                self.__assert_graph_edge_does_not_exist_check(
                    undirected_graph, directed_graph, edge
                )

    def test_add_edge(self) -> None:
        # generate graph input
        random_vertices: list[int] = random.sample(range(101), 15)
        random_edges: list[list[int]] = self.__generate_random_edges(random_vertices, 4)

        # build graphs WITHOUT edges
        undirected_graph = GraphAdjacencyList(
            vertices=random_vertices, edges=[], directed=False
        )
        directed_graph = GraphAdjacencyList(
            vertices=random_vertices, edges=[], directed=True
        )

        # run and test add_edge
        for edge in random_edges:
            undirected_graph.add_edge(edge[0], edge[1])
            directed_graph.add_edge(edge[0], edge[1])
            self.__assert_graph_edge_exists_check(
                undirected_graph, directed_graph, edge
            )

    def test_remove_edge(self) -> None:
        # generate graph input and graphs
        (
            undirected_graph,
            directed_graph,
            random_vertices,
            random_edges,
        ) = self.__generate_graphs(20, 0, 100, 4)

        # run and test remove_edge
        for edge in random_edges:
            self.__assert_graph_edge_exists_check(
                undirected_graph, directed_graph, edge
            )
            undirected_graph.remove_edge(edge[0], edge[1])
            directed_graph.remove_edge(edge[0], edge[1])
            self.__assert_graph_edge_does_not_exist_check(
                undirected_graph, directed_graph, edge
            )

    def test_add_and_remove_edges_repeatedly(self) -> None:
        (
            undirected_graph,
            directed_graph,
            random_vertices,
            random_edges,
        ) = self.__generate_graphs(20, 0, 100, 4)

        # make some more edge options!
        more_random_edges: list[list[int]] = []

        while len(more_random_edges) != len(random_edges):
            edges: list[list[int]] = self.__generate_random_edges(random_vertices, 4)
            for edge in edges:
                if len(more_random_edges) == len(random_edges):
                    break
                elif edge not in more_random_edges and edge not in random_edges:
                    more_random_edges.append(edge)

        for i, _ in enumerate(random_edges):
            undirected_graph.add_edge(more_random_edges[i][0], more_random_edges[i][1])
            directed_graph.add_edge(more_random_edges[i][0], more_random_edges[i][1])

            self.__assert_graph_edge_exists_check(
                undirected_graph, directed_graph, more_random_edges[i]
            )

            undirected_graph.remove_edge(random_edges[i][0], random_edges[i][1])
            directed_graph.remove_edge(random_edges[i][0], random_edges[i][1])

            self.__assert_graph_edge_does_not_exist_check(
                undirected_graph, directed_graph, random_edges[i]
            )

    def test_add_vertex_exception_check(self) -> None:
        (
            undirected_graph,
            directed_graph,
            random_vertices,
            random_edges,
        ) = self.__generate_graphs(20, 0, 100, 4)

        for vertex in random_vertices:
            with pytest.raises(ValueError):
                undirected_graph.add_vertex(vertex)
            with pytest.raises(ValueError):
                directed_graph.add_vertex(vertex)

    def test_remove_vertex_exception_check(self) -> None:
        (
            undirected_graph,
            directed_graph,
            random_vertices,
            random_edges,
        ) = self.__generate_graphs(20, 0, 100, 4)

        for i in range(101):
            if i not in random_vertices:
                with pytest.raises(ValueError):
                    undirected_graph.remove_vertex(i)
                with pytest.raises(ValueError):
                    directed_graph.remove_vertex(i)

    def test_add_edge_exception_check(self) -> None:
        (
            undirected_graph,
            directed_graph,
            random_vertices,
            random_edges,
        ) = self.__generate_graphs(20, 0, 100, 4)

        for edge in random_edges:
            with pytest.raises(ValueError):
                undirected_graph.add_edge(edge[0], edge[1])
            with pytest.raises(ValueError):
                directed_graph.add_edge(edge[0], edge[1])

    def test_remove_edge_exception_check(self) -> None:
        (
            undirected_graph,
            directed_graph,
            random_vertices,
            random_edges,
        ) = self.__generate_graphs(20, 0, 100, 4)

        more_random_edges: list[list[int]] = []

        while len(more_random_edges) != len(random_edges):
            edges: list[list[int]] = self.__generate_random_edges(random_vertices, 4)
            for edge in edges:
                if len(more_random_edges) == len(random_edges):
                    break
                elif edge not in more_random_edges and edge not in random_edges:
                    more_random_edges.append(edge)

        for edge in more_random_edges:
            with pytest.raises(ValueError):
                undirected_graph.remove_edge(edge[0], edge[1])
            with pytest.raises(ValueError):
                directed_graph.remove_edge(edge[0], edge[1])

    def test_contains_edge_exception_check(self) -> None:
        (
            undirected_graph,
            directed_graph,
            random_vertices,
            random_edges,
        ) = self.__generate_graphs(20, 0, 100, 4)

        for vertex in random_vertices:
            with pytest.raises(ValueError):
                undirected_graph.contains_edge(vertex, 102)
            with pytest.raises(ValueError):
                directed_graph.contains_edge(vertex, 102)

        with pytest.raises(ValueError):
            undirected_graph.contains_edge(103, 102)
        with pytest.raises(ValueError):
            directed_graph.contains_edge(103, 102)


if __name__ == "__main__":
    unittest.main()
