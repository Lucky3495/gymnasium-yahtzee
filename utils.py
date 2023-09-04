from enum import Enum, IntEnum
from scoring import function_list

class Rule(Enum):
    FORCED_JOKER = 0
    FREE_JOKER = 1

class Category(IntEnum):
    ONES = 0
    TWOS = 1
    THREES = 2
    FOURS = 3
    FIVES = 4
    SIXES = 5
    THREE_OF_A_KIND = 6
    FOUR_OF_A_KIND = 7
    FULL_HOUSE = 8
    SMALL_STRAIGHT = 9
    LARGE_STRAIGHT = 10
    YAHTZEE = 11
    CHOICE = 12

class Sheet:
    """
    A class that represents a Yahtzee sheet.
    """
    def __init__(self) -> None:
        """
        Initilizes a Sheet, will start empty.
        """
        self._round: int = 0
        self._sheet: list[int] = [-1]*13 # -1 means the category is empty, 0 means it is filled with 0
    
    
    def get_empty_categories(self) -> list[Category]:
        """
        Returns a list with all empty categories.
        """
        empty = []
        for value in Category:
            if self._sheet[value] == -1:
                empty.append(value)
        
        return empty

    def get_score(self, dice: list[int], category: Category) -> int:
        """
        Returns the score for a set of dice in category.
        """
        return function_list[category](dice)

    # I don't know if this should return a bool that reflects if the cell was not already filled,
    # or if it should raise an exception like it is now TODO
    def fill_category(self, dice: list[int], category: Category) -> None:
        if self._sheet[category] != -1:
            raise ValueError(f"Category: {category.name} already filled.")
        
        self._sheet[category] = self.get_score(dice, category)
