import math

def calculate_elo_expected_score(rating_a: int, rating_b: int) -> float:
    """
    Calculate the expected score (probability of winning) for Player A
    against Player B using Elo ratings.
    
    The formula is: E_A = 1 / (1 + 10^((R_B - R_A) / 400)).

    Args:
        rating_a (int): Elo rating of Player A.
        rating_b (int): Elo rating of Player B.

    Returns:
        float: Expected score for Player A (between 0.0 and 1.0).
    """
    exponent = (rating_b - rating_a) / 400
    return 1.0 / (1.0 + math.pow(10, exponent))

def test_calculate_elo_expected_score():
    # Player A higher rating
    assert 0.5 < calculate_elo_expected_score(1600, 1400) < 1.0
    # Player B higher rating
    assert 0.0 < calculate_elo_expected_score(1400, 1600) < 0.5
    # Equal ratings
    assert calculate_elo_expected_score(1500, 1500) == 0.5

if __name__ == "__main__":
    ra, rb = 1600, 1400
    expected_a = calculate_elo_expected_score(ra, rb)
    print(f"Player A Rating: {ra}")
    print(f"Player B Rating: {rb}")
    print(f"Expected Score for Player A: {expected_a:.4f}")
    print(f"Expected Score for Player B: {1.0 - expected_a:.4f}")