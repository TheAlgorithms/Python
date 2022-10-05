from other.best_match_finder import best_match_found, perform_matching, get_best_match


def test_best_match_found():
    assert best_match_found({0: ['A'], 1: ['B'], 2: ['C']}) == True


def test_perform_matching():
    boys = {
        1: ["C", "B", "E", "A", "D"],
        2: ["A", "B", "E", "C", "D"],
        3: ["D", "C", "B", "A", "E"],
        4: ["A", "C", "D", "B", "E"],
        5: ["A", "B", "D", "E", "C"],
    }

    girls = {
        "A": [3, 5, 2, 1, 4],
        "B": [5, 2, 1, 4, 3],
        "C": [4, 3, 5, 1, 2],
        "D": [1, 2, 3, 4, 5],
        "E": [2, 3, 4, 1, 5],
    }
    boys_checklist: Dict[object, List[object]] = boys.copy()
    girls_possible_matches: Dict[object, List[object]] = dict(
        zip(girls.keys(), [[]] * len(boys.keys()))
    )

    assert perform_matching(
        group1=boys,
        group2=girls,
        group1_checklist=boys_checklist,
        group2_possible_matches=girls_possible_matches
    ) == [
        ('A', 5), ('B', 2), ('C', 4), ('D', 3), ('E', 1)]


def test_get_best_match():
    boys = {
        1: ["C", "B", "E", "A", "D"],
        2: ["A", "B", "E", "C", "D"],
        3: ["D", "C", "B", "A", "E"],
        4: ["A", "C", "D", "B", "E"],
        5: ["A", "B", "D", "E", "C"],
    }

    girls = {
        "A": [3, 5, 2, 1, 4],
        "B": [5, 2, 1, 4, 3],
        "C": [4, 3, 5, 1, 2],
        "D": [1, 2, 3, 4, 5],
        "E": [2, 3, 4, 1, 5],
    }

    assert get_best_match(boys, girls) == [
        ('A', 5), ('B', 2), ('C', 4), ('D', 3), ('E', 1)]
