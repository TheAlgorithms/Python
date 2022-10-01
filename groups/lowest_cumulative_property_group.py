"""
Organize objects with attribute values into N groups such that the cumulative property of the largest group is the lowest among all other N groups.
"""

"""
Strategy: Here, the first strategy can be used with O(n^2(lnn)^2). Here, a heap data structure is used to insert elements into groups. 
Each time, the groups with the minimum cumulatvie attirbute value is picked and the element inserted into that group. 
Repeat the step until no more elements remain 
"""

#Maintain the heap data structure but as a priority queue. This can be a directly addressed system, such as 2*n and 2*n+1, same as a heap structure.
array_group_heap = []

#A list of ungrouped elements, again maintained as a heap.

def heapify_data(heap_structure_or_list, number_of_elements: int):

    """
    This function will create a max-element heap of all the ungrouped data as well as the maximum attributes linked to each group data.
    """

    pass

def prioritize_element(heap_structure_or_list):

    """
    Same as above. Is a priority queue that returns the min element in the bunch.
    """

    pass

def pick_and_place(max_element, min_group):

    """
    Pick the element with the maximum value from the ungrouped data heap. Place it into the element with min cumulative attribute value.


    """

    pass


def test_heap_value():

    """
    Unit test to validate against.


    ungrouped_data = [2,5,8,30,55]

    number of groups = 3

    groups = [
        [55],
        [30],
        [8,5,2]

    ]

    """

    pass




