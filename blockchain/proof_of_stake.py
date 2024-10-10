import random

class Validator:
    """
    Represents a validator in a Proof of Stake system.

    Attributes:
        name (str): The name of the validator.
        stake (int): The amount of stake (coins) the validator holds.
    """
    def __init__(self, name, stake):
        """
        Initializes a new validator with a given name and stake.
        
        Args:
            name (str): The name of the validator.
            stake (int): The amount of stake the validator has.
        """
        self.name = name
        self.stake = stake  # Stake defines how much weight the validator has.

def choose_validator(validators):
    """
    Selects a validator to create the next block based on the weight of their stake.
    
    The higher the stake, the greater the chance to be selected.
    
    Args:
        validators (list): A list of Validator objects.
    
    Returns:
        Validator: The selected validator based on weighted random selection.
    """
    # Total stake of all validators
    total_stake = sum(v.stake for v in validators)
    
    # Create a list of validators with weights (probability of being chosen)
    weighted_validators = [(v, v.stake / total_stake) for v in validators]
    
    # Randomly select a validator based on their stake weight
    selected = random.choices([v[0] for v in weighted_validators],
                              weights=[v[1] for v in weighted_validators])
    return selected[0]

# Example of validators with different stakes
validators = [Validator("Alice", 50), Validator("Bob", 30), Validator("Charlie", 20)]

# Select a validator based on their stake
chosen_validator = choose_validator(validators)
print(f"Chosen validator: {chosen_validator.name}")
