from collections import deque

def predict_party_victory(senate: str) -> str:
    """
    Predict the winning party in the Senate based on the order of actions.

    Args:
        senate (str): A string representing the order of senators in the Senate.
            'R' represents a Republican senator, and 'D' represents a Democratic senator.

    Returns:
        str: The name of the winning party, either "Radiant" or "Dire."

    Examples:
        >>> predict_party_victory("RD")
        'Radiant'

        >>> predict_party_victory("RDD")
        'Dire'

        >>> predict_party_victory("RRDDDD")
        'Dire'

        >>> predict_party_victory("RDDRDD")
        'Dire'
    """
    democratic_senators, republican_senators = deque(), deque()

    for index, senator in enumerate(senate):
        if senator == "R":
            republican_senators.append(index)
        else:
            democratic_senators.append(index)

    while democratic_senators and republican_senators:
        democratic_turn = democratic_senators.popleft()
        republican_turn = republican_senators.popleft()

        if republican_turn < democratic_turn:
            republican_senators.append(democratic_turn + len(senate))
        else:
            democratic_senators.append(republican_turn + len(senate))

    return "Radiant" if republican_senators else "Dire"


if __name__ == "__main__":
        import doctest
    doctest.testmod()
