# Let's create a roll and dice program using the random module and a class called Dice

import random


class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        
        return first, second # Is not neccesary the parenthesis to return a tuple


dice = Dice()
print(dice.roll())