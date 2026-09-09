import pytest

from strings.split import split


def test_split_rejects_multi_character_separator():
    with pytest.raises(ValueError, match="separator must be a single character"):
        split("a--b--c", separator="--")


def test_split_supports_single_character_separator():
    assert split("a--b--c", separator="-") == ["a", "", "b", "", "c"]
