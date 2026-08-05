"""
Unit tests for the Snake Water Gun game.

Tests cover:
    - All win/loss/tie combinations (3×3 matrix).
    - Case‑insensitivity and whitespace handling.
    - Invalid inputs.
    - The interactive ``main()`` loop (with mocked I/O).
"""

import random
import pytest
from io import StringIO

from snake_water_gun import play, main, VALID_CHOICES, WIN_CONDITIONS


# ---------------------------------------------------------------------------
# Helper: parametrised tests for play()
# ---------------------------------------------------------------------------

# Map computer choice to expected outcome for a given player choice
OUTCOMES = {
    # player chooses Snake
    ("Snake", "Snake"): "It's a tie!",
    ("Snake", "Water"): "You win!",
    ("Snake", "Gun"): "You lose!",
    # player chooses Water
    ("Water", "Snake"): "You lose!",
    ("Water", "Water"): "It's a tie!",
    ("Water", "Gun"): "You win!",
    # player chooses Gun
    ("Gun", "Snake"): "You win!",
    ("Gun", "Water"): "You lose!",
    ("Gun", "Gun"): "It's a tie!",
}


@pytest.mark.parametrize(
    "player_choice, computer_choice",
    [(p, c) for p in VALID_CHOICES for c in VALID_CHOICES],
)
def test_all_outcomes(player_choice: str, computer_choice: str, monkeypatch) -> None:
    """
    Verify that every possible combination returns the correct result string.
    """
    monkeypatch.setattr(random, "choice", lambda _: computer_choice)

    result = play(player_choice)
    expected_outcome = OUTCOMES[(player_choice, computer_choice)]
    expected = (
        f"You chose {player_choice}, Computer chose {computer_choice}. "
        f"{expected_outcome}"
    )
    assert result == expected


@pytest.mark.parametrize(
    "raw_input, normalised",
    [
        ("snake", "Snake"),
        ("SNAKE", "Snake"),
        ("  water  ", "Water"),
        ("GuN", "Gun"),
    ],
)
def test_case_insensitivity_and_whitespace(
    raw_input: str, normalised: str, monkeypatch
) -> None:
    """Input is normalised regardless of casing and surrounding spaces."""
    # Fix computer choice to something predictable
    monkeypatch.setattr(random, "choice", lambda _: "Gun")

    result = play(raw_input)
    # We expect the result string to contain the normalised player choice
    assert f"You chose {normalised}" in result


@pytest.mark.parametrize(
    "invalid_input",
    [
        "",
        "  ",
        "rock",
        "paper",
        "scissors",
        "snakes",
        "gunwater",
        "123",
    ],
)
def test_invalid_input_returns_error(invalid_input: str) -> None:
    """Invalid choices produce an error message."""
    result = play(invalid_input)
    assert result.startswith("Invalid choice:")


# ---------------------------------------------------------------------------
# Tests for main() interactive loop
# ---------------------------------------------------------------------------


def test_main_quit_immediately(monkeypatch, capsys) -> None:
    """Typing 'quit' right away exits the loop with a goodbye message."""
    monkeypatch.setattr("sys.stdin", StringIO("quit\n"))
    main()
    captured = capsys.readouterr()
    assert "Thanks for playing. Goodbye!" in captured.out


def test_main_one_round_then_quit(monkeypatch, capsys) -> None:
    """Play a single round and then quit."""
    inputs = StringIO("Snake\nquit\n")
    monkeypatch.setattr("sys.stdin", inputs)
    # Force computer choice to make assertion deterministic
    monkeypatch.setattr(random, "choice", lambda _: "Water")

    main()
    captured = capsys.readouterr()
    assert "You chose Snake, Computer chose Water. You win!" in captured.out
    assert "Thanks for playing. Goodbye!" in captured.out
