import random

"""

"""

class Dice():
    NUM_SIDES = 6
    def __init__(self):
        self.sides = []
        for i in range(1, 7):
            self.sides.append(i)
        self.odds = len(self.sides)
    
    def roll(self):
        return random.choice(self.sides)
    
    def _str_(self):
        return 'Fair Dice'

def play_dice(num_dice, num_rolls):
    dices = [Dice() for i in range(num_dice)]
    occurrence = [0 for i in range(0, len(dices)*Dice.NUM_SIDES+1)]

    for i in range(num_rolls):
        occurrence[sum([dice.roll() for dice in dices])] += 1

    probability = [count/num_rolls for count in occurrence]
    print(f"Number of rolls = {num_rolls}") 
    for idx, val in enumerate(probability):
        print(f"{idx} {round(val*100, 2)}%")

play_dice(1, 100000)
play_dice(2, 100000)
play_dice(3, 100000)