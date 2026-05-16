import os
from itertools import chain
from random import randrange, shuffle

import pytest

from .sol1 import PokerHand

SORTED_HANDS = (
    "4S 3H 2C 7S 5H",
    "9D 8H 2C 6S 7H",
    "2D 6D 9D TH 7D",
    "TC 8C 2S JH 6C",
    "JH 8S TH AH QH",
    "TS KS 5S 9S AC",
    "KD 6S 9D TH AD",
    "KS 8D 4D 9S 4S",  # pair
    "8C 4S KH JS 4D",  # pair
    "QH 8H KD JH 8S",  # pair
    "KC 4H KS 2H 8D",  # pair
    "KD 4S KC 3H 8S",  # pair
    "AH 8S AS KC JH",  # pair
    "3H 4C 4H 3S 2H",  # 2 pairs
    "5S 5D 2C KH KH",  # 2 pairs
    "3C KH 5D 5S KH",  # 2 pairs
    "AS 3C KH AD KH",  # 2 pairs
    "7C 7S 3S 7H 5S",  # 3 of a kind
    "7C 7S KH 2H 7H",  # 3 of a kind
    "AC KH QH AH AS",  # 3 of a kind
    "2H 4D 3C AS 5S",  # straight (low ace)
    "3C 5C 4C 2C 6H",  # straight
    "6S 8S 7S 5H 9H",  # straight
    "JS QS 9H TS KH",  # straight
    "QC KH TS JS AH",  # straight (high ace)
    "8C 9C 5C 3C TC",  # flush
    "3S 8S 9S 5S KS",  # flush
    "4C 5C 9C 8C KC",  # flush
    "JH 8H AH KH QH",  # flush
    "3D 2H 3H 2C 2D",  # full house
    "2H 2C 3S 3H 3D",  # full house
    "KH KC 3S 3H 3D",  # full house
    "JC 6H JS JD JH",  # 4 of a kind
    "JC 7H JS JD JH",  # 4 of a kind
    "JC KH JS JD JH",  # 4 of a kind
    "2S AS 4S 5S 3S",  # straight flush (low ace)
    "2D 6D 3D 4D 5D",  # straight flush
    "5C 6C 3C 7C 4C",  # straight flush
    "JH 9H TH KH QH",  # straight flush
    "JH AH TH KH QH",  # royal flush (high ace straight flush)
)

TEST_COMPARE = (
    ("2H 3H 4H 5H 6H", "KS AS TS QS JS", "Loss"),
    ("2H 3H 4H 5H 6H", "AS AD AC AH JD", "Win"),
    ("AS AH 2H AD AC", "JS JD JC JH 3D", "Win"),
    ("2S AH 2H AS AC", "JS JD JC JH AD", "Loss"),
    ("2S AH 2H AS AC", "2H 3H 5H 6H 7H", "Win"),
    ("AS 3S 4S 8S 2S", "2H 3H 5H 6H 7H", "Win"),
    ("2H 3H 5H 6H 7H", "2S 3H 4H 5S 6C", "Win"),
    ("2S 3H 4H 5S 6C", "3D 4C 5H 6H 2S", "Tie"),
    ("2S 3H 4H 5S 6C", "AH AC 5H 6H AS", "Win"),
    ("2S 2H 4H 5S 4C", "AH AC 5H 6H AS", "Loss"),
    ("2S 2H 4H 5S 4C", "AH AC 5H 6H 7S", "Win"),
    ("6S AD 7H 4S AS", "AH AC 5H 6H 7S", "Loss"),
    ("2S AH 4H 5S KC", "AH AC 5H 6H 7S", "Loss"),
    ("2S 3H 6H 7S 9C", "7H 3C TH 6H 9S", "Loss"),
    ("4S 5H 6H TS AC", "3S 5H 6H TS AC", "Win"),
    ("2S AH 4H 5S 6C", "AD 4C 5H 6H 2C", "Tie"),
    ("AS AH 3H AD AC", "AS AH 2H AD AC", "Win"),
    ("AH AC 5H 5C QS", "AH AC 5H 5C KS", "Loss"),
    ("AH AC 5H 5C QS", "KH KC 5H 5C QS", "Win"),
    ("7C 7S KH 2H 7H", "3C 3S AH 2H 3H", "Win"),
    ("3C 3S AH 2H 3H", "7C 7S KH 2H 7H", "Loss"),
    ("6H 5H 4H 3H 2H", "5H 4H 3H 2H AH", "Win"),
    ("5H 4H 3H 2H AH", "5H 4H 3H 2H AH", "Tie"),
    ("5H 4H 3H 2H AH", "6H 5H 4H 3H 2H", "Loss"),
    ("AH AD KS KC AC", "AH KD KH AC KC", "Win"),
    ("2H 4D 3C AS 5S", "2H 4D 3C 6S 5S", "Loss"),
    ("2H 3S 3C 3H 2S", "3S 3C 2S 2H 2D", "Win"),
    ("4D 6D 5D 2D JH", "3S 8S 3H TC KH", "Loss"),
    ("4S 6C 8S 3S 7S", "AD KS 2D 7D 7C", "Loss"),
    ("6S 4C 7H 8C 3H", "5H JC AH 9D 9C", "Loss"),
    ("9D 9H JH TC QH", "3C 2S JS 5C 7H", "Win"),
    ("2H TC 8S AD 9S", "4H TS 7H 2C 5C", "Win"),
    ("9D 3S 2C 7S 7C", "JC TD 3C TC 9H", "Loss"),
)

TEST_FLUSH = (
    ("2H 3H 4H 5H 6H", True),
    ("AS AH 2H AD AC", False),
    ("2H 3H 5H 6H 7H", True),
    ("KS AS TS QS JS", True),
    ("8H 9H QS JS TH", False),
    ("AS 3S 4S 8S 2S", True),
)

TEST_STRAIGHT = (
    ("2H 3H 4H 5H 6H", True),
    ("AS AH 2H AD AC", False),
    ("2H 3H 5H 6H 7H", False),
    ("KS AS TS QS JS", True),
    ("8H 9H QS JS TH", True),
)

TEST_FIVE_HIGH_STRAIGHT = (
    ("2H 4D 3C AS 5S", True, [5, 4, 3, 2, 14]),
    ("2H 5D 3C AS 5S", False, [14, 5, 5, 3, 2]),
    ("JH QD KC AS TS", False, [14, 13, 12, 11, 10]),
    ("9D 3S 2C 7S 7C", False, [9, 7, 7, 3, 2]),
)

TEST_KIND = (
    ("JH AH TH KH QH", 0),
    ("JH 9H TH KH QH", 0),
    ("JC KH JS JD JH", 7),
    ("KH KC 3S 3H 3D", 6),
    ("8C 9C 5C 3C TC", 0),
    ("JS QS 9H TS KH", 0),
    ("7C 7S KH 2H 7H", 3),
    ("3C KH 5D 5S KH", 2),
    ("QH 8H KD JH 8S", 1),
    ("2D 6D 9D TH 7D", 0),
)

TEST_TYPES = (
    ("JH AH TH KH QH", 23),
    ("JH 9H TH KH QH", 22),
    ("JC KH JS JD JH", 21),
    ("KH KC 3S 3H 3D", 20),
    ("8C 9C 5C 3C TC", 19),
    ("JS QS 9H TS KH", 18),
    ("7C 7S KH 2H 7H", 17),
    ("3C KH 5D 5S KH", 16),
    ("QH 8H KD JH 8S", 15),
    ("2D 6D 9D TH 7D", 14),
)


def generate_random_hand():
    play, oppo = randrange(len(SORTED_HANDS)), randrange(len(SORTED_HANDS))
    expected = ["Loss", "Tie", "Win"][(play >= oppo) + (play > oppo)]
    hand, other = SORTED_HANDS[play], SORTED_HANDS[oppo]
    return hand, other, expected


def generate_random_hands(number_of_hands: int = 100):
    return (generate_random_hand() for _ in range(number_of_hands))


@pytest.mark.parametrize(("hand", "expected"), TEST_FLUSH)
def test_hand_is_flush(hand, expected):
    assert PokerHand(hand)._is_flush() == expected


@pytest.mark.parametrize(("hand", "expected"), TEST_STRAIGHT)
def test_hand_is_straight(hand, expected):
    assert PokerHand(hand)._is_straight() == expected


@pytest.mark.parametrize(("hand", "expected", "card_values"), TEST_FIVE_HIGH_STRAIGHT)
def test_hand_is_five_high_straight(hand, expected, card_values):
    player = PokerHand(hand)
    assert player._is_five_high_straight() == expected
    assert player._card_values == card_values


@pytest.mark.parametrize(("hand", "expected"), TEST_KIND)
def test_hand_is_same_kind(hand, expected):
    assert PokerHand(hand)._is_same_kind() == expected


@pytest.mark.parametrize(("hand", "expected"), TEST_TYPES)
def test_hand_values(hand, expected):
    assert PokerHand(hand)._hand_type == expected


@pytest.mark.parametrize(("hand", "other", "expected"), TEST_COMPARE)
def test_compare_simple(hand, other, expected):
    assert PokerHand(hand).compare_with(PokerHand(other)) == expected


@pytest.mark.parametrize(("hand", "other", "expected"), generate_random_hands())
def test_compare_random(hand, other, expected):
    assert PokerHand(hand).compare_with(PokerHand(other)) == expected


def test_hand_sorted():
    poker_hands = [PokerHand(hand) for hand in SORTED_HANDS]
    list_copy = poker_hands.copy()
    shuffle(list_copy)
    user_sorted = chain(sorted(list_copy))
    for index, hand in enumerate(user_sorted):
        assert hand == poker_hands[index]


def test_custom_sort_five_high_straight():
    # Test that five high straights are compared correctly.
    pokerhands = [PokerHand("2D AC 3H 4H 5S"), PokerHand("2S 3H 4H 5S 6C")]
    pokerhands.sort(reverse=True)
    assert pokerhands[0].__str__() == "2S 3H 4H 5S 6C"


def test_multiple_calls_five_high_straight():
    # Multiple calls to five_high_straight function should still return True
    # and shouldn't mutate the list in every call other than the first.
    pokerhand = PokerHand("2C 4S AS 3D 5C")
    expected = True
    expected_card_values = [5, 4, 3, 2, 14]
    for _ in range(10):
        assert pokerhand._is_five_high_straight() == expected
        assert pokerhand._card_values == expected_card_values


def test_euler_project():
    # Problem number 54 from Project Euler
    # Testing from poker_hands.txt file
    answer = 0
    script_dir = os.path.abspath(os.path.dirname(__file__))
    poker_hands = os.path.join(script_dir, "poker_hands.txt")
    with open(poker_hands) as file_hand:
        for line in file_hand:
            player_hand = line[:14].strip()
            opponent_hand = line[15:].strip()
            player, opponent = PokerHand(player_hand), PokerHand(opponent_hand)
            output = player.compare_with(opponent)
            if output == "Win":
                answer += 1
    assert answer == 376
