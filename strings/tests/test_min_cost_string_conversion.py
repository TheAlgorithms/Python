from strings.min_cost_string_conversion import min_cost_string_conversion


def test_calculate_min_cost_conversion_correct_answer_empty_string():
    s1, s2 = "", "short string"
    copy, replace, delete, insert = 1, 2, 3, 4
    min_cost = min_cost_string_conversion(s1, s2, copy, replace, delete, insert)
    assert min_cost == len(s2) * insert


def test_calculate_min_cost_conversion_correct_answer_first_correct_case():
    s1, s2 = "geek", "gesek"
    copy, replace, delete, insert = 2, 4, 3, 8
    min_cost = min_cost_string_conversion(s1, s2, copy, replace, delete, insert)
    assert min_cost == copy * 4 + insert


def test_calculate_min_cost_conversion_correct_answer_second_correct_case():
    s1, s2 = "cat", "cut"
    copy, replace, delete, insert = 2, 6, 3, 8
    min_cost = min_cost_string_conversion(s1, s2, copy, replace, delete, insert)
    assert min_cost == copy * 2 + replace


def test_calculate_min_cost_conversion_correct_answer_third_correct_case():
    s1, s2 = "sunday", "saturday"
    copy, replace, delete, insert = 10, 20, 30, 40
    min_cost = min_cost_string_conversion(s1, s2, copy, replace, delete, insert)
    assert min_cost == copy * 5 + insert * 2 + replace


def test_calculate_min_cost_conversion_correct_answer_fourth_correct_case():
    s1, s2 = "pythonista", ""
    copy, replace, delete, insert = 4, 1, 3, 4
    min_cost = min_cost_string_conversion(s1, s2, copy, replace, delete, insert)
    assert min_cost == delete * len(s1)
