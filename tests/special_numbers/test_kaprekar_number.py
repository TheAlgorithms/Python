from maths.special_numbers.kaprekar_number import is_kaprekar_number


def test_kaprekar_numbers():
    assert is_kaprekar_number(1) is True
    assert is_kaprekar_number(9) is True
    assert is_kaprekar_number(45) is True
    assert is_kaprekar_number(55) is True
    assert is_kaprekar_number(99) is True
    assert is_kaprekar_number(297) is True


def test_non_kaprekar_numbers():
    assert is_kaprekar_number(10) is False  # Power of 10
    assert is_kaprekar_number(100) is False  # Power of 10
    assert is_kaprekar_number(3) is False
    assert is_kaprekar_number(50) is False
    assert is_kaprekar_number(0) is False
    assert is_kaprekar_number(-45) is False
