import random
from typing import List


class Validator:
    """
    Represents a validator in a Proof of Stake system.

    Attributes:
        name (str): The name of the validator.
        stake (int): The amount of stake (coins) the validator holds.
    """

    def __init__(self, name: str, stake: int):
        """
        Initializes a new validator with a given name and stake.

        Args:
            name (str): The name of the validator.
            stake (int): The amount of stake the validator has.
        """
        self.name = name
        self.stake = stake


def choose_validator(validators: List[Validator]) -> Validator:
    """
    Selects a validator to create the next block based on the weight of their stake.

    The higher the stake, the greater the chance to be selected.

    Args:
        validators (List[Validator]): A list of Validator objects.

    Returns:
        Validator: The selected validator based on weighted random selection.

    Example:
        >>> validators = [Validator("Alice", 50), Validator("Bob", 30), Validator("Charlie", 20)]
        >>> chosen = choose_validator(validators)
        >>> isinstance(chosen, Validator)
        True
    """
    total_stake = sum(v.stake for v in validators)
    weighted_validators = [(v, v.stake / total_stake) for v in validators]
    selected = random.choices(
        [v[0] for v in weighted_validators], weights=[v[1] for v in weighted_validators]
    )
    return selected[0]
