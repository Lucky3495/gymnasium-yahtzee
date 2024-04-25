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
