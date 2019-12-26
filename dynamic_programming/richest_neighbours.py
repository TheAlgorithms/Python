# Author: Biney Kingsley
# email: bineykingsley36@gmail.com
import logging
logging.basicConfig(level=logging.INFO)
def richest_neighbours(community: list) -> int:
    '''
    Scenario
    --------
    In a given community, we want to determine the perfect resident with the richest neighbours 
    given the networth of all households in community.
    A perfect neighbour is one with all neighbours on all sides of his/her residence.
    Given a model of the residence to be an nxn, nxm, or mxn array matrix of size at least 3x3,
    Compute the resident with the richest neighbour.

    Example
    -------
    Givena model of community z to be [[3,4,5], with the networth of residents as 3,4,5,6,5,4,3,4,5
                                       [6,5,4],
                                       [3,4,5]]
    The resident with the richest neighbours will be 5 at index z[1][1]. This is because only 5 
    satisfies the contraint of a perfect neighbour. The combined networth of 5's neighbours is 18.
    >>> community = [[3,4,5], [6,5,4],[3,4,5]]
    >>> richest_neighbours(community)
    5
    '''
    neigh_sum = 0
    big_neighbours = []
    nw_map = dict()
    if len(community) < 3:
        logging.warn('Constraint not satisfied by any neighbour. Community should be at least 3x3')
        return 'No resident'
    try:
            for ind_i, it_1 in enumerate(community):
                for ind_j, val in enumerate(it_1):
                    if ind_i > 0 and ind_j > 0 and ind_i < len(community)-1 and ind_j < len(it_1)-1:
                        right_neighbour = community[ind_i][ind_j+1]
                        left_neighbour = community[ind_i][ind_j-1]
                        top_neighbour = community[ind_i-1][ind_j]
                        bottom_neighbour = community[ind_i+1][ind_j]
                        neighbours = [right_neighbour, left_neighbour, top_neighbour, bottom_neighbour]
                        if all(neighbours):
                            neigh_sum += right_neighbour + left_neighbour + top_neighbour + bottom_neighbour
                            stingified_neighbour_index = f'{ind_i},{ind_j}'
                            nw_map[stingified_neighbour_index] = neigh_sum
            a, b = list(map(int, max(nw_map).split(',')))
            return community[a][b]
    except Exception as e:
        logging.error('Exception occured', exc_info=True)
        return 'No resident'

if __name__== "__main__":
    import doctest
    test_community = [[3,4,5], [6,5,4],[3,4,5]]
    doctest.testmod(extraglobs={'c': richest_neighbours(test_community)})
