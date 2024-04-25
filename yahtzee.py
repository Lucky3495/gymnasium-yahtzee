from utils import *
from sheet import Sheet
from scoring import function_list
from numpy.random import randint as np_randint
from random import randint

class Yahtzee:

    def __init__(self, rule: JokerRule=JokerRule.FORCED_JOKER) -> None:
        self.sheet: Sheet = Sheet()
        self.rule: JokerRule = rule
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

    def get_score(self, category: Category) -> int:
        """
        Returns the score for a set of dice in category.
        """
        return function_list[category](self.dice)
    
    def is_joker(self) -> bool:
        """
        Returns `True` if the current set of dice is a joker, otherwise returns False.
        """
        # the dice are a joker iff the yahtzee is socred with 50 and the current set of dice are a yahtzee
        return self.sheet[Category.YAHTZEE] == 50 and len(set(self.dice)) == 1

