"""Tests for rolling hash Rabin-Karp implementation."""
import pytest
from rolling_hash.rabin_karp import rabin_karp


def test_basic_matches():
    assert rabin_karp("abracadabra", "abra") == [0, 7]
    assert rabin_karp("aaaaa", "aa") == [0, 1, 2, 3]
    assert rabin_karp("hello world", "world") == [6]


def test_no_match():
    assert rabin_karp("abcdef", "gh") == []
    assert rabin_karp("abc", "abcd") == []


def test_empty_pattern():
    # Empty pattern matches at every position (including end)
    assert rabin_karp("abc", "") == [0, 1, 2, 3]
    assert rabin_karp("", "") == [0]


def test_single_character():
    assert rabin_karp("a", "a") == [0]
    assert rabin_karp("ab", "a") == [0]
    assert rabin_karp("ab", "b") == [1]


def test_overlapping():
    text = "aaa"
    pattern = "aa"
    assert rabin_karp(text, pattern) == [0, 1]


def test_case_sensitive():
    assert rabin_karp("ABCabc", "abc") == [3]
    assert rabin_karp("ABCabc", "ABC") == [0]


def test_unicode():
    # Unicode characters
    assert rabin_karp("你好世界你好", "你好") == [0, 4]


def test_long_pattern():
    text = "a" * 1000
    pattern = "a" * 100
    expected = list(range(0, 901))
    assert rabin_karp(text, pattern) == expected
