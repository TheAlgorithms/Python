import unittest
import os
from tabu_search import generate_neighbours, generate_first_solution, find_neighborhood, tabu_search

TEST_FILE = os.path.join(os.path.dirname(__file__), './tabuTestData.txt')

NEIGHBOURS_DICT = {'a': [['b', '20'], ['c', '18'], ['d', '22'], ['e', '26']],
                   'c': [['a', '18'], ['b', '10'], ['d', '23'], ['e', '24']],
                   'b': [['a', '20'], ['c', '10'], ['d', '11'], ['e', '12']],
                   'e': [['a', '26'], ['b', '12'], ['c', '24'], ['d', '40']],
                   'd': [['a', '22'], ['b', '11'], ['c', '23'], ['e', '40']]}

FIRST_SOLUTION = ['a', 'c', 'b', 'd', 'e', 'a']

DISTANCE = 105

NEIGHBOURHOOD_OF_SOLUTIONS = [['a', 'e', 'b', 'd', 'c', 'a', 90],
                              ['a', 'c', 'd', 'b', 'e', 'a', 90],
                              ['a', 'd', 'b', 'c', 'e', 'a', 93],
                              ['a', 'c', 'b', 'e', 'd', 'a', 102],
                              ['a', 'c', 'e', 'd', 'b', 'a', 113],
                              ['a', 'b', 'c', 'd', 'e', 'a', 119]]


class TestClass(unittest.TestCase):
    def test_generate_neighbours(self):
        neighbours = generate_neighbours(TEST_FILE)

        self.assertEquals(NEIGHBOURS_DICT, neighbours)

    def test_generate_first_solutions(self):
        first_solution, distance = generate_first_solution(TEST_FILE, NEIGHBOURS_DICT)

        self.assertEquals(FIRST_SOLUTION, first_solution)
        self.assertEquals(DISTANCE, distance)

    def test_find_neighbours(self):
        neighbour_of_solutions = find_neighborhood(FIRST_SOLUTION, NEIGHBOURS_DICT)

        self.assertEquals(NEIGHBOURHOOD_OF_SOLUTIONS, neighbour_of_solutions)

    def test_tabu_search(self):
        best_sol, best_cost = tabu_search(FIRST_SOLUTION, DISTANCE, NEIGHBOURS_DICT, 4, 3)

        self.assertEquals(['a', 'd', 'b', 'e', 'c', 'a'], best_sol)
        self.assertEquals(87, best_cost)