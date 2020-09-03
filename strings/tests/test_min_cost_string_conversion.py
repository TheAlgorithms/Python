from strings.min_cost_string_conversion import run_algorithm as calc_min_cost


def test_calculate_min_cost_conversion_correct_answer_empty_string():
    s2 = "short string"
    copy, replace, delete, insert = 1, 2, 3, 4
    min_cost = calc_min_cost("", s2, copy, replace, delete, insert)
    assert min_cost == len(s2) * insert


def test_calculate_min_cost_conversion_correct_answer_first_correct_case():
    s1, s2 = "geek", "gesek"
    copy, replace, delete, insert = 2, -2, 3, 8
    min_cost = calc_min_cost(s1, s2, copy, replace, delete, insert)
    assert min_cost == insert


def test_calculate_min_cost_conversion_correct_answer_second_correct_case():
    s1, s2 = "cat", "cut"
    copy, replace, delete, insert = 2, 6, 3, 8
    min_cost = calc_min_cost(s1, s2, copy, replace, delete, insert)
    assert min_cost == copy * 2 + replace


def test_calculate_min_cost_conversion_correct_answer_third_correct_case():
    s1, s2 = "sunday", "saturday"
    copy, replace, delete, insert = 4, 1, 3, 4
    min_cost = calc_min_cost(s1, s2, copy, replace, delete, insert)
    assert min_cost == replace * 6 + insert * 2


def test_calculate_min_cost_conversion_correct_answer_fourth_correct_case():
    s1, s2 = "pythonista", ""
    copy, replace, delete, insert = 4, 1, 3, 4
    min_cost = calc_min_cost(s1, s2, copy, replace, delete, insert)
    assert min_cost == delete * len(s1)
