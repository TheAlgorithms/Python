#!/usr/bin/env python3
"""
Yazar: K. Umut Araz

Açıklama:
Aşağıdaki uygulama, komşuluk matrisi kullanılarak uygulanmış sağlam bir ağırlıksız Grafik veri yapısıdır.
Bu grafiğin köşeleri ve kenarları, her köşede seçtiğiniz genel değeri saklarken etkili bir şekilde başlatılabilir ve değiştirilebilir.

Komşuluk Matrisi: https://mathworld.wolfram.com/AdjacencyMatrix.html

Gelecekteki Potansiyel Fikirler:
- Kenar ağırlıklarını ayarlamak ve kenar ağırlıklarını ayarlamak için bir bayrak ekleyin
- Kenar ağırlıklarını ve köşe değerlerini, müşterinin istediği herhangi bir şeyi saklayacak şekilde özelleştirilebilir hale getirin
- Müşteri isterse çoklu grafik işlevselliğini destekleyin
"""

from __future__ import annotations

import random
import unittest
from pprint import pformat
from typing import Generic, TypeVar

import pytest

T = TypeVar("T")


class GraphAdjacencyMatrix(Generic[T]):
    def __init__(
        self, vertices: list[T], edges: list[list[T]], directed: bool = True
    ) -> None:
        """
        Parametreler:
        - vertices: (list[T]) Müşterinin girmek istediği köşe isimlerinin listesi. Varsayılan boş.
        - edges: (list[list[T]]) Müşterinin girmek istediği kenarların listesi. Her kenar 2 elemanlı bir listedir. Varsayılan boş.
        - directed: (bool) Grafiğin yönlendirilmiş veya yönlendirilmemiş olduğunu belirtir. Varsayılan True.
        """
        self.directed = directed
        self.vertex_to_index: dict[T, int] = {}
        self.adj_matrix: list[list[int]] = []

        # Boşluk kontrolleri
        edges = edges or []
        vertices = vertices or []

        for vertex in vertices:
            self.add_vertex(vertex)

        for edge in edges:
            if len(edge) != 2:
                msg = f"Geçersiz giriş: {edge} uzunluğu 2 olmalıdır."
                raise ValueError(msg)
            self.add_edge(edge[0], edge[1])

    def add_edge(self, source_vertex: T, destination_vertex: T) -> None:
        """
        Kaynak köşeden hedef köşeye bir kenar oluşturur. Verilen herhangi bir köşe yoksa veya kenar zaten mevcutsa, bir ValueError fırlatılır.
        """
        if not (
            self.contains_vertex(source_vertex)
            and self.contains_vertex(destination_vertex)
        ):
            msg = (
                f"Yanlış giriş: {source_vertex} veya "
                f"{destination_vertex} mevcut değil"
            )
            raise ValueError(msg)
        if self.contains_edge(source_vertex, destination_vertex):
            msg = (
                "Yanlış giriş: Kenar zaten mevcut "
                f"{source_vertex} ve {destination_vertex} arasında"
            )
            raise ValueError(msg)

        # İlgili köşelerin indekslerini alın ve kenar değerlerini 1 olarak ayarlayın.
        u: int = self.vertex_to_index[source_vertex]
        v: int = self.vertex_to_index[destination_vertex]
        self.adj_matrix[u][v] = 1
        if not self.directed:
            self.adj_matrix[v][u] = 1

    def remove_edge(self, source_vertex: T, destination_vertex: T) -> None:
        """
        İki köşe arasındaki kenarı kaldırır. Verilen herhangi bir köşe yoksa veya kenar mevcut değilse, bir ValueError fırlatılır.
        """
        if not (
            self.contains_vertex(source_vertex)
            and self.contains_vertex(destination_vertex)
        ):
            msg = (
                f"Yanlış giriş: {source_vertex} veya "
                f"{destination_vertex} mevcut değil"
            )
            raise ValueError(msg)
        if not self.contains_edge(source_vertex, destination_vertex):
            msg = (
                "Yanlış giriş: Kenar mevcut değil "
                f"{source_vertex} ve {destination_vertex} arasında"
            )
            raise ValueError(msg)

        # İlgili köşelerin indekslerini alın ve kenar değerlerini 0 olarak ayarlayın.
        u: int = self.vertex_to_index[source_vertex]
        v: int = self.vertex_to_index[destination_vertex]
        self.adj_matrix[u][v] = 0
        if not self.directed:
            self.adj_matrix[v][u] = 0

    def add_vertex(self, vertex: T) -> None:
        """
        Grafa bir köşe ekler. Verilen köşe zaten mevcutsa, bir ValueError fırlatılır.
        """
        if self.contains_vertex(vertex):
            msg = f"Yanlış giriş: {vertex} bu grafikte zaten mevcut."
            raise ValueError(msg)

        # köşe için sütun oluştur
        for row in self.adj_matrix:
            row.append(0)

        # köşe için satır oluştur ve diğer veri yapılarını güncelle
        self.adj_matrix.append([0] * (len(self.adj_matrix) + 1))
        self.vertex_to_index[vertex] = len(self.adj_matrix) - 1

    def remove_vertex(self, vertex: T) -> None:
        """
        Verilen köşeyi grafikten kaldırır ve verilen köşeden gelen ve giden tüm kenarları siler. Verilen köşe mevcut değilse, bir ValueError fırlatılır.
        """
        if not self.contains_vertex(vertex):
            msg = f"Yanlış giriş: {vertex} bu grafikte mevcut değil."
            raise ValueError(msg)

        # önce, silinen köşeye karşılık gelen satırı silerek satırları yukarı kaydırın.
        start_index = self.vertex_to_index[vertex]
        self.adj_matrix.pop(start_index)

        # daha sonra, silinen köşeye karşılık gelen sütundaki değerleri silerek sütunları sola kaydırın
        for lst in self.adj_matrix:
            lst.pop(start_index)

        # son temizlik
        self.vertex_to_index.pop(vertex)

        # adj matrisinde silinen köşe tarafından kaydırılan köşeler için indeksleri azaltın
        for inner_vertex in self.vertex_to_index:
            if self.vertex_to_index[inner_vertex] >= start_index:
                self.vertex_to_index[inner_vertex] = (
                    self.vertex_to_index[inner_vertex] - 1
                )

    def contains_vertex(self, vertex: T) -> bool:
        """
        Grafikte köşe varsa True, yoksa False döner.
        """
        return vertex in self.vertex_to_index

    def contains_edge(self, source_vertex: T, destination_vertex: T) -> bool:
        """
        Grafikte source_vertex'ten destination_vertex'e kenar varsa True, yoksa False döner. Verilen herhangi bir köşe mevcut değilse, bir ValueError fırlatılır.
        """
        if not (
            self.contains_vertex(source_vertex)
            and self.contains_vertex(destination_vertex)
        ):
            msg = (
                f"Yanlış giriş: {source_vertex} "
                f"veya {destination_vertex} mevcut değil."
            )
            raise ValueError(msg)

        u = self.vertex_to_index[source_vertex]
        v = self.vertex_to_index[destination_vertex]
        return self.adj_matrix[u][v] == 1

    def clear_graph(self) -> None:
        """
        Tüm köşeleri ve kenarları temizler.
        """
        self.vertex_to_index = {}
        self.adj_matrix = []

    def __repr__(self) -> str:
        first = "Komşuluk Matrisi:\n" + pformat(self.adj_matrix)
        second = "\nKöşe indeks eşlemesi:\n" + pformat(self.vertex_to_index)
        return first + second


class TestGraphMatrix(unittest.TestCase):
    def __assert_graph_edge_exists_check(
        self,
        undirected_graph: GraphAdjacencyMatrix,
        directed_graph: GraphAdjacencyMatrix,
        edge: list[int],
    ) -> None:
        assert undirected_graph.contains_edge(edge[0], edge[1])
        assert undirected_graph.contains_edge(edge[1], edge[0])
        assert directed_graph.contains_edge(edge[0], edge[1])

    def __assert_graph_edge_does_not_exist_check(
        self,
        undirected_graph: GraphAdjacencyMatrix,
        directed_graph: GraphAdjacencyMatrix,
        edge: list[int],
    ) -> None:
        assert not undirected_graph.contains_edge(edge[0], edge[1])
        assert not undirected_graph.contains_edge(edge[1], edge[0])
        assert not directed_graph.contains_edge(edge[0], edge[1])

    def __assert_graph_vertex_exists_check(
        self,
        undirected_graph: GraphAdjacencyMatrix,
        directed_graph: GraphAdjacencyMatrix,
        vertex: int,
    ) -> None:
        assert undirected_graph.contains_vertex(vertex)
        assert directed_graph.contains_vertex(vertex)

    def __assert_graph_vertex_does_not_exist_check(
        self,
        undirected_graph: GraphAdjacencyMatrix,
        directed_graph: GraphAdjacencyMatrix,
        vertex: int,
    ) -> None:
        assert not undirected_graph.contains_vertex(vertex)
        assert not directed_graph.contains_vertex(vertex)

    def __generate_random_edges(
        self, vertices: list[int], edge_pick_count: int
    ) -> list[list[int]]:
        assert edge_pick_count <= len(vertices)

        random_source_vertices: list[int] = random.sample(
            vertices[0 : int(len(vertices) / 2)], edge_pick_count
        )
        random_destination_vertices: list[int] = random.sample(
            vertices[int(len(vertices) / 2) :], edge_pick_count
        )
        random_edges: list[list[int]] = []

        for source in random_source_vertices:
            for dest in random_destination_vertices:
                random_edges.append([source, dest])

        return random_edges

    def __generate_graphs(
        self, vertex_count: int, min_val: int, max_val: int, edge_pick_count: int
    ) -> tuple[GraphAdjacencyMatrix, GraphAdjacencyMatrix, list[int], list[list[int]]]:
        if max_val - min_val + 1 < vertex_count:
            raise ValueError(
                "Yinelenen köşelerle sonuçlanacak. Ya min_val ve max_val arasındaki aralığı artırın ya da köşe sayısını azaltın"
            )

        # grafik girişi oluştur
        random_vertices: list[int] = random.sample(
            range(min_val, max_val + 1), vertex_count
        )
        random_edges: list[list[int]] = self.__generate_random_edges(
            random_vertices, edge_pick_count
        )

        # grafikler oluştur
        undirected_graph = GraphAdjacencyMatrix(
            vertices=random_vertices, edges=random_edges, directed=False
        )
        directed_graph = GraphAdjacencyMatrix(
            vertices=random_vertices, edges=random_edges, directed=True
        )

        return undirected_graph, directed_graph, random_vertices, random_edges

    def test_init_check(self) -> None:
        (
            undirected_graph,
            directed_graph,
            random_vertices,
            random_edges,
        ) = self.__generate_graphs(20, 0, 100, 4)

        # köşeler ve kenarlarla grafik başlatma test
        for num in random_vertices:
            self.__assert_graph_vertex_exists_check(
                undirected_graph, directed_graph, num
            )

        for edge in random_edges:
            self.__assert_graph_edge_exists_check(
                undirected_graph, directed_graph, edge
            )

        assert not undirected_graph.directed
        assert directed_graph.directed

    def test_contains_vertex(self) -> None:
        random_vertices: list[int] = random.sample(range(101), 20)

        # Kenarlar OLMADAN grafikler oluştur
        undirected_graph = GraphAdjacencyMatrix(
            vertices=random_vertices, edges=[], directed=False
        )
        directed_graph = GraphAdjacencyMatrix(
            vertices=random_vertices, edges=[], directed=True
        )

        # contains_vertex test
        for num in range(101):
            assert (num in random_vertices) == undirected_graph.contains_vertex(num)
            assert (num in random_vertices) == directed_graph.contains_vertex(num)

    def test_add_vertices(self) -> None:
        random_vertices: list[int] = random.sample(range(101), 20)

        # boş grafikler oluştur
        undirected_graph: GraphAdjacencyMatrix = GraphAdjacencyMatrix(
            vertices=[], edges=[], directed=False
        )
        directed_graph: GraphAdjacencyMatrix = GraphAdjacencyMatrix(
            vertices=[], edges=[], directed=True
        )

        # add_vertex çalıştır
        for num in random_vertices:
            undirected_graph.add_vertex(num)

        for num in random_vertices:
            directed_graph.add_vertex(num)

        # add_vertex çalıştığını test et
        for num in random_vertices:
            self.__assert_graph_vertex_exists_check(
                undirected_graph, directed_graph, num
            )

    def test_remove_vertices(self) -> None:
        random_vertices: list[int] = random.sample(range(101), 20)

        # Kenarlar OLMADAN grafikler oluştur
        undirected_graph = GraphAdjacencyMatrix(
            vertices=random_vertices, edges=[], directed=False
        )
        directed_graph = GraphAdjacencyMatrix(
            vertices=random_vertices, edges=[], directed=True
        )

        # remove_vertex çalıştığını test et
        for num in random_vertices:
            self.__assert_graph_vertex_exists_check(
                undirected_graph, directed_graph, num
            )

            undirected_graph.remove_vertex(num)
            directed_graph.remove_vertex(num)

            self.__assert_graph_vertex_does_not_exist_check(
                undirected_graph, directed_graph, num
            )

    def test_add_and_remove_vertices_repeatedly(self) -> None:
        random_vertices1: list[int] = random.sample(range(51), 20)
        random_vertices2: list[int] = random.sample(range(51, 101), 20)

        # Kenarlar OLMADAN grafikler oluştur
        undirected_graph = GraphAdjacencyMatrix(
            vertices=random_vertices1, edges=[], directed=False
        )
        directed_graph = GraphAdjacencyMatrix(
            vertices=random_vertices1, edges=[], directed=True
        )

        # köşeleri ekleme ve kaldırma test
        for i, _ in enumerate(random_vertices1):
            undirected_graph.add_vertex(random_vertices2[i])
            directed_graph.add_vertex(random_vertices2[i])

            self.__assert_graph_vertex_exists_check(
                undirected_graph, directed_graph, random_vertices2[i]
            )

            undirected_graph.remove_vertex(random_vertices1[i])
            directed_graph.remove_vertex(random_vertices1[i])

            self.__assert_graph_vertex_does_not_exist_check(
                undirected_graph, directed_graph, random_vertices1[i]
            )

        # tüm köşeleri kaldır
        for i, _ in enumerate(random_vertices1):
            undirected_graph.remove_vertex(random_vertices2[i])
            directed_graph.remove_vertex(random_vertices2[i])

            self.__assert_graph_vertex_does_not_exist_check(
                undirected_graph, directed_graph, random_vertices2[i]
            )

    def test_contains_edge(self) -> None:
        # grafikler ve grafik girişi oluştur
        vertex_count = 20
        (
            undirected_graph,
            directed_graph,
            random_vertices,
            random_edges,
        ) = self.__generate_graphs(vertex_count, 0, 100, 4)

        # test için tüm olası kenarları oluştur
        all_possible_edges: list[list[int]] = []
        for i in range(vertex_count - 1):
            for j in range(i + 1, vertex_count):
                all_possible_edges.append([random_vertices[i], random_vertices[j]])
                all_possible_edges.append([random_vertices[j], random_vertices[i]])

        # contains_edge fonksiyonunu test et
        for edge in all_possible_edges:
            if edge in random_edges:
                self.__assert_graph_edge_exists_check(
                    undirected_graph, directed_graph, edge
                )
            elif [edge[1], edge[0]] in random_edges:
                # bu kenar yönlendirilmemiş için mevcut olduğundan ancak ters yönlendirilmiş için mevcut olmayabilir
                self.__assert_graph_edge_exists_check(
                    undirected_graph, directed_graph, [edge[1], edge[0]]
                )
            else:
                self.__assert_graph_edge_does_not_exist_check(
                    undirected_graph, directed_graph, edge
                )

    def test_add_edge(self) -> None:
        # grafik girişi oluştur
        random_vertices: list[int] = random.sample(range(101), 15)
        random_edges: list[list[int]] = self.__generate_random_edges(random_vertices, 4)

        # Kenarlar OLMADAN grafikler oluştur
        undirected_graph = GraphAdjacencyMatrix(
            vertices=random_vertices, edges=[], directed=False
        )
        directed_graph = GraphAdjacencyMatrix(
            vertices=random_vertices, edges=[], directed=True
        )

        # add_edge çalıştır ve test et
        for edge in random_edges:
            undirected_graph.add_edge(edge[0], edge[1])
            directed_graph.add_edge(edge[0], edge[1])
            self.__assert_graph_edge_exists_check(
                undirected_graph, directed_graph, edge
            )

    def test_remove_edge(self) -> None:
        # grafik girişi ve grafikler oluştur
        (
            undirected_graph,
            directed_graph,
            random_vertices,
            random_edges,
        ) = self.__generate_graphs(20, 0, 100, 4)

        # remove_edge çalıştır ve test et
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

        # daha fazla kenar seçeneği oluştur!
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
