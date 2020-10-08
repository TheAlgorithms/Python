from dataclasses import dataclass
from typing import Any

import pytest

from data_structures.linked_list.is_palindrome import (
    is_palindrome,
    is_palindrome_dict,
    is_palindrome_stack,
)


@dataclass
class Node:
    val: Any
    next: "Node" = None


@pytest.fixture
def single_char() -> Node:
    return Node("a")


@pytest.fixture
def kayake() -> Node:
    e = Node("e")
    k = Node("k", e)
    a = Node("a", k)
    y = Node("y", a)
    a = Node("a", y)
    k = Node("k", a)
    return k


@pytest.fixture
def racecar() -> Node:
    r = Node("r")
    a = Node("a", r)
    c = Node("c", a)
    e = Node("e", c)
    c = Node("c", e)
    a = Node("a", c)
    r = Node("r", a)
    return r


@pytest.fixture
def stats() -> Node:
    s = Node("s")
    t = Node("t", s)
    a = Node("a", t)
    t = Node("t", a)
    s = Node("s", t)
    return s


@pytest.fixture
def computer() -> Node:
    r = Node("r")
    e = Node("e", r)
    t = Node("t", e)
    u = Node("u", t)
    p = Node("p", u)
    m = Node("m", p)
    o = Node("o", m)
    c = Node("c", o)
    return c


def test_is_palindrome_correct_result(racecar, stats, computer, kayake, single_char):
    assert is_palindrome(None)
    assert is_palindrome(single_char)
    assert is_palindrome(racecar)
    assert is_palindrome(stats)
    assert not is_palindrome(kayake)
    assert not is_palindrome(computer)


def test_is_palindrome_dict_correct_result(
    racecar, stats, computer, kayake, single_char
):
    assert is_palindrome_dict(None)
    assert is_palindrome_dict(single_char)
    assert is_palindrome_dict(racecar)
    assert is_palindrome_dict(stats)
    assert not is_palindrome_dict(kayake)
    assert not is_palindrome_dict(computer)


def test_is_palindrome_stack_correct_result(
    racecar, stats, computer, kayake, single_char
):
    assert is_palindrome_stack(None)
    assert is_palindrome_stack(single_char)
    assert is_palindrome_stack(racecar)
    assert is_palindrome_stack(stats)
    assert not is_palindrome_stack(kayake)
    assert not is_palindrome_stack(computer)
