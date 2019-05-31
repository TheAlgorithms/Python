from bogo_sort import bogo_sort
from bubble_sort import bubble_sort
from bucket_sort import bucket_sort
from cocktail_shaker_sort import cocktail_shaker_sort
from comb_sort import comb_sort
from counting_sort import counting_sort
from cycle_sort import cycle_sort
from gnome_sort import gnome_sort
from heap_sort import heap_sort
from insertion_sort import insertion_sort
from merge_sort_fastest import merge_sort as merge_sort_fastest
from merge_sort import merge_sort
from pancake_sort import pancake_sort
from quick_sort_3_partition import quick_sort_3partition
from quick_sort import quick_sort
from radix_sort import radix_sort
from random_pivot_quick_sort import quick_sort_random
from selection_sort import selection_sort
from shell_sort import shell_sort
from tim_sort import tim_sort
from topological_sort import topological_sort
from tree_sort import tree_sort
from wiggle_sort import wiggle_sort


TEST_CASES = [
    {'input': [8, 7, 6, 5, 4, 3, -2, -5], 'expected': [-5, -2, 3, 4, 5, 6, 7, 8]},
    {'input': [-5, -2, 3, 4, 5, 6, 7, 8], 'expected': [-5, -2, 3, 4, 5, 6, 7, 8]},
    {'input': [5, 6, 1, 4, 0, 1, -2, -5, 3, 7], 'expected': [-5, -2, 0, 1, 1, 3, 4, 5, 6, 7]},
    {'input': [2, -2], 'expected': [-2, 2]},
    {'input': [1], 'expected': [1]},
    {'input': [], 'expected': []},
]

'''
    TODO:
    - Fix some broken tests in particular cases (as [] for example),
    - Unify the input format: should always be function(input_collection) (no additional args)
    - Unify the output format: should always be a collection instead of updating input elements
      and returning None
    - Rewrite some algorithms in function format (in case there is no function definition)
'''

TEST_FUNCTIONS = [
    bogo_sort,
    bubble_sort,
    bucket_sort,
    cocktail_shaker_sort,
    comb_sort,
    counting_sort,
    cycle_sort,
    gnome_sort,
    heap_sort,
    insertion_sort,
    merge_sort_fastest,
    merge_sort,
    pancake_sort,
    quick_sort_3partition,
    quick_sort,
    radix_sort,
    quick_sort_random,
    selection_sort,
    shell_sort,
    tim_sort,
    topological_sort,
    tree_sort,
    wiggle_sort,
]


for function in TEST_FUNCTIONS:
    for case in TEST_CASES:
        result = function(case['input'])
        assert result  == case['expected'], 'Executed function: {}, {} != {}'.format(function.__name__, result, case['expected'])
