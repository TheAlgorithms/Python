from strings.palindrome import is_palindrome


def test_palindrome_true():
    assert is_palindrome("level") == True


def test_palindrome_false():
    assert is_palindrome("hello") == False