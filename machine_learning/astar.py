"""
A* algoritması, optimal çözümleri verimli bir şekilde hesaplamak için uniform-cost arama ve saf heuristic arama özelliklerini birleştirir.

A* algoritması, bir düğümle ilişkili maliyetin f(n) = g(n) + h(n) olduğu en iyi ilk arama algoritmasıdır. Burada g(n), başlangıç durumundan düğüm n'ye kadar olan yolun maliyeti ve h(n), düğüm n'den bir hedefe kadar olan yolun heuristic tahminidir.

A* algoritması, düzenli bir grafik arama algoritmasına bir heuristic ekler, esasen her adımda daha optimal bir karar verilmesi için önceden plan yapar. Bu nedenle, A* beyinli bir algoritma olarak bilinir.

https://tr.wikipedia.org/wiki/A*_arama_algoritması
"""

import numpy as np


class Cell:
    """
    Cell sınıfı, dünyadaki bir hücreyi temsil eder ve şu özelliklere sahiptir:
    position: Başlangıçta (0,0) olarak ayarlanan x ve y koordinatlarından oluşan bir demet.
    parent: Bu hücreye gelmeden önce ziyaret edilen parent hücre nesnesini içerir.
    g, h, f: Heuristic fonksiyonu çağrıldığında kullanılan parametreler.
    """

    def __init__(self):
        self.position = (0, 0)
        self.parent = None
        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, cell):
        return self.position == cell.position

    def showcell(self):
        print(self.position)


class Gridworld:
    """
    Gridworld sınıfı, burada bir M*M matrisi olan dış dünyayı temsil eder.
    world_size: Varsayılan olarak 5 olan world_size ile bir numpy array oluşturur.
    """

    def __init__(self, world_size=(5, 5)):
        self.w = np.zeros(world_size)
        self.world_x_limit = world_size[0]
        self.world_y_limit = world_size[1]

    def show(self):
        print(self.w)

    def get_neighbours(self, cell):
        """
        Hücrenin komşularını döndürür
        """
        neighbour_cord = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        ]
        current_x = cell.position[0]
        current_y = cell.position[1]
        neighbours = []
        for n in neighbour_cord:
            x = current_x + n[0]
            y = current_y + n[1]
            if 0 <= x < self.world_x_limit and 0 <= y < self.world_y_limit:
                c = Cell()
                c.position = (x, y)
                c.parent = cell
                neighbours.append(c)
        return neighbours


def astar(world, start, goal):
    """
    A* algoritmasının uygulanması.
    world : Dünya nesnesinin bir örneği.
    start : Başlangıç pozisyonu olarak hücre nesnesi.
    goal  : Hedef pozisyonu olarak hücre nesnesi.

    >>> p = Gridworld()
    >>> start = Cell()
    >>> start.position = (0,0)
    >>> goal = Cell()
    >>> goal.position = (4,4)
    >>> astar(p, start, goal)
    [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]
    """
    _open = []
    _closed = []
    _open.append(start)

    while _open:
        min_f = np.argmin([n.f for n in _open])
        current = _open[min_f]
        _closed.append(_open.pop(min_f))
        if current == goal:
            break
        for n in world.get_neighbours(current):
            if n in _closed:
                continue
            n.g = current.g + 1
            x1, y1 = n.position
            x2, y2 = goal.position
            n.h = (y2 - y1) ** 2 + (x2 - x1) ** 2
            n.f = n.h + n.g

            if any(c == n and c.f < n.f for c in _open):
                continue
            _open.append(n)
    path = []
    while current.parent is not None:
        path.append(current.position)
        current = current.parent
    path.append(current.position)
    return path[::-1]


if __name__ == "__main__":
    world = Gridworld()
    # Başlangıç pozisyonu ve hedef
    start = Cell()
    start.position = (0, 0)
    goal = Cell()
    goal.position = (4, 4)
    print(f"{start.position} konumundan {goal.position} konumuna yol")
    s = astar(world, start, goal)
    # Görsel nedenlerle.
    for i in s:
        world.w[i] = 1
    print(world.w)
