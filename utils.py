from enum import Enum, IntEnum
from scoring import function_list

class JokerRule(Enum):
    # The rules correspond to when a second Yahtzee is gotten, the second Yahtzee is a "Joker"
    # Upper section is: Ones, Twos, ..., Sixes
    # Lower section is the rest

    # Forced Joker:
    # 1. Upper section box corresponding to Yahtzee must be used if unused
    # 2. If the corresponding upper section box was used, 
    #    a lower section box can be used, score is calculated normally
    # 3. If all lower sections are already used,
    #    then an upper box section must be used, it will score 0
    FORCED_JOKER = 0

    # Free Choice Joker:
    # Player can choose any box, only if the upper corresponding box has already been used,
    # otherwise it would score 0 if it's used in the lower section's full house, small and large straigt.
    # (i am not sure about the three of a kind, four of a kind, and chance, wikipedia doesn't mention them)
    FREE_JOKER = 1

    # Original Joker:
    # Jokers can only be used in the lower section, this was changed later to idk what
    # (this rule sucks the most, probably won't ever use it, maybe not implement it either)
    ORIGINAL_JOKER = 2

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
    
    def __getitem__(self, i):
        assert i >= 0 and i <= 12
        return self._sheet[i]

    # I don't know if this should return a bool that reflects if the cell was not already filled,
    # or if it should raise an exception like it is now TODO
    def fill_category(self, dice: list[int], category: Category, joker: bool=False) -> None:
        if self._sheet[category] != -1:
            raise ValueError(f"Category: {category.name} already filled.")
        if len(dice) != 5:
            raise ValueError(f"List of dice {dice} is not of length 5. It is of length {len(dice)}.")

        if category in [Category.FULL_HOUSE, Category.SMALL_STRAIGHT, Category.LARGE_STRAIGHT]:
            self._sheet[category] = self.get_score(dice, category)
        else:
            self._sheet[category] = self.get_score(dice, category)
    
    def __setitem__(self, i, value: int):
        assert i >= 0 and i <= 12
        self._sheet[i] = value
