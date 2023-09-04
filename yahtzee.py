from utils import *
from numpy.random import randint as np_randint
from random import randint

class Yahtzee:

    def __init__(self, rule: Rule=Rule.FORCED_JOKER) -> None:
        self.sheet: Sheet = Sheet()
        self.rule: Rule = rule
        self.round: int = 0 # rounds will have the range [0, 12], when round == 13 the game is over
        self.dice: list[int] = list(np_randint(low=1, high=7, size=5))
        self.rolls: int = 2 # number of rolls remaining, 0 means no rolls, must choose a category. (Rounds start with dice already rolled for first time)

    def reroll(self, mask: list[bool]) -> None:    
        if self.rolls <= 0:
            raise RuntimeError("No dice rolls remaining.")
        
        self.rolls -= 1
        
        for i in range(5):
            if mask[i]:
                self.dice[i] = randint(1, 6)
