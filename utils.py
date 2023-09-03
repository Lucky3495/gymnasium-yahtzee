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
