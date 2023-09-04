from utils import *
import numpy as np

class Yahtzee:

    def __init__(self, rule: Rule=Rule.FORCED_JOKER) -> None:
        self._sheet = Sheet()
        self.rule = rule
        self.round = 0 # rounds will have the range [0, 12], when round == 13 the game is over
        self.dice = np.random.randint(low=1, high=7, size=5)
        self.rolls = 2 # number of rolls remaining, 0 means no rolls, must choose a category. (Rounds start with dice already rolled for first time)

    
