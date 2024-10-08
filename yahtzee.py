from utils import JokerRule, Category
from scoring import function_list
from numpy.random import randint as np_randint
from random import randint

# TODO: for now this only works with the free choice JokerRule
class Yahtzee:

    def __init__(self, rule: JokerRule=JokerRule.FREE_JOKER) -> None:
        if self.joker_rule != JokerRule.FREE_JOKER:
            raise NotImplementedError("Only `Category.FREE_JOKER` is implemented thus far.")
        
        self.sheet: dict[Category, int] = {category:-1 for category in Category}
        self.joker_rule: JokerRule = rule
        self.round: int = 0 # rounds will have the range [0, 12], when round == 13 the game is over
        self.dice: list[int] = list(np_randint(low=1, high=7, size=5))
        self.rolls: int = 2 # number of rolls remaining, 0 means no rolls, must choose a category. (Rounds start with dice already rolled for first time)

    def reroll(self, mask: list[bool]) -> None:    
        if self.rolls <= 0:
            raise RuntimeError("No dice rolls remaining.")
        if len(mask) != 5:
            raise ValueError(f"Mask expected to be of length 5 but got a mask of length {len(mask)}")
        
        self.rolls -= 1
        
        for i in range(5):
            if mask[i]:
                self.dice[i] = randint(1, 6)

        # if the player already has a yahtzee, and he got another one, add 100 points to the yahtzee box
        if self.sheet[Category.YAHTZEE] > 0 and self.get_score(Category.YAHTZEE) > 0:
            self.sheet[Category.YAHTZEE] += 100

    def get_score(self, category: Category) -> int:
        """
        Returns the score for a set of dice in category.
        """

        # if the score is affected by a joker, give it the is_joker boolean
        if category in [Category.FULL_HOUSE, Category.SMALL_STRAIGHT, Category.LARGE_STRAIGHT]:
            return function_list[category](self.dice, self.is_joker())
        else:
            return function_list[category](self.dice)
    
    def is_joker(self) -> bool:
        """
        Returns `True` if the current set of dice is a joker, otherwise returns False.
        This depends on the `JokerRule` used.
        """

        # if it's not a yahtzee, it cannot be a joker
        if self.get_score(Category.YAHTZEE) == 0:
            return False
        
        if self.joker_rule == JokerRule.FREE_JOKER:
            die = self.dice[0]
            if self.sheet[Category(die-1)] == -1:
                return False
        return True

    def fill_category(self, category: Category) -> None:
        if self.sheet[category] != -1:
            raise ValueError(f"Category: {category.name} already filled.")
        if len(self.dice) != 5: # it shouldn't come to this, unless the user modifies self.dice
            raise ValueError(f"List of dice {self.dice} is not of length 5. It is of length {len(self.dice)}.")

        self.sheet[category] = self.get_score(category)
