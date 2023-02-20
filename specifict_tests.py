import doctest
import coverage
import pytest
import numpy as np
# methods to test: _remove_repair, remove
from data_structures.binary_tree.red_black_tree import RedBlackTree
from linear_algebra.src.polynom_for_points import points_to_polynomial
from graphs.a_star import search
from matrix.inverse_of_matrix import inverse_of_matrix
from project_euler.problem_049.sol1 import solution
from project_euler.problem_551.sol1 import next_term
from cellular_automata.conways_game_of_life import *  # needs globals in file to run tests
from graphs.bi_directional_dijkstra import *  # needs globals in file to run tests
from strings.detecting_english_programmatically import *

cov = coverage.Coverage(branch=True, )

cov.start()
doctest.run_docstring_examples(RedBlackTree._remove_repair,
                               globals(), name="_remove_repair")
doctest.run_docstring_examples(bidirectional_dij, globals(), name="bidirectional_dij")
# separate testfile
pytest.main(["digital_image_processing/test_digital_image_processing.py::test_canny"])
doctest.run_docstring_examples(
    points_to_polynomial, globals(), name="points_to_polynomial")
doctest.run_docstring_examples(search, globals(), name="search")
doctest.run_docstring_examples(inverse_of_matrix, globals(), name="inverse_of_matrix")
doctest.run_docstring_examples(solution, globals(), name="solution")
doctest.run_docstring_examples(next_term, globals(), name="next_term")
doctest.run_docstring_examples(new_generation, globals(), name="new_generation")
doctest.run_docstring_examples(RedBlackTree.remove, globals(), name="remove")
doctest.run_docstring_examples(get_english_count, globals(), name="get_english_count")
doctest.run_docstring_examples(remove_non_letters, globals(), name="remove_non_letters")

cov.stop()
cov.save()

# the pytest runs alot of test we are not interested in, omit these
to_omit = ["/usr/lib/python3/dist-packages/PIL/Image.py",
           "/usr/lib/python3/dist-packages/attr/_compat.py",
           "digital_image_processing/sepia.py",
           "digital_image_processing/dithering/burkes.py",
           "digital_image_processing/filters/local_binary_pattern.py",
           "digital_image_processing/filters/median_filter.py",
           "digital_image_processing/filters/gaussian_filter.py",
           "digital_image_processing/convert_to_negative.py",
           "digital_image_processing/resize/resize.py",
           "digital_image_processing/change_contrast.py",
           "/usr/lib/python3/dist-packages/attr/_make.py",
           "digital_image_processing/test_digital_image_processing.py",
           "digital_image_processing/filters/sobel_filter.py",
           "digital_image_processing/filters/convolve.py",
           "config-3.py",
           "config.py",
           "digital_image_processing/__init__.py",
           "digital_image_processing/dithering/__init__.py",
           "digital_image_processing/edge_detection/__init__.py",
           "digital_image_processing/filters/__init__.py",
           "digital_image_processing/resize/__init__.py"]

cov.report(omit=to_omit, skip_empty=False, show_missing=True)

#doctest.run_docstring_examples(solution, globals())
