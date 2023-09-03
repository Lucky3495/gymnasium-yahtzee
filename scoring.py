"""
This file contains all the functions for counting 
the score of a set of dice in a category.

The functions return the default scores, special joker
rules are implemented by the Sheet class."""

def get_score_ones(dice: list[int]) -> int:
    return dice.count(1)

def get_score_twos(dice: list[int]) -> int:
    return dice.count(2)

def get_score_threes(dice: list[int]) -> int:
    return dice.count(3)

def get_score_fours(dice: list[int]) -> int:
    return dice.count(4)

def get_score_fives(dice: list[int]) -> int:
    return dice.count(5)

def get_score_sixes(dice: list[int]) -> int:
    return dice.count(6)

def get_score_three_of_a_kind(dice: list[int]) -> int:
    for die in dice:
        if dice.count(die) >= 3:
            return sum(dice)
        
    return 0

def get_score_four_of_a_kind(dice: list[int]) -> int:
    for die in dice:
        if dice.count(die) >= 4:
            return sum(dice)
        
    return 0

def get_score_full_house(dice: list[int]) -> int:
    triple = False
    pair = False
    for die in dice:
        if dice.count(die) == 3:
            triple = True
        if dice.count(die) == 2:
            pair = True
    
    if triple and pair:
        return 25
    
    return 0

# TODO: This and large_straight are not ideal (probably). Do something about it later.
def get_score_small_straight(dice: list[int]) -> int:
    sets: list[set[int]] = [
        {1, 2, 3, 4},
        {2, 3, 4, 5},
        {3, 4, 5, 6}
    ]

    dice_set = set(dice)
    for s in sets:
        if s.issubset(dice):
            return 30
    
    return 0


def get_score_large_straight(dice: list[int]) -> int:
    sets: list[set[int]] = [
        {1, 2, 3, 4, 5},
        {2, 3, 4, 5, 6},
    ]

    dice_set = set(dice)
    for s in sets:
        if s.issubset(dice):
            return 40
    
    return 0

def get_score_yahtzee(dice: list[int]) -> int:
    if len(set(dice)) == 1:
        return 50
    return 0

def get_score_choice(dice: list[int]) -> int:
    return sum(dice)

function_list = [
    get_score_ones,
    get_score_twos,
    get_score_threes,
    get_score_fours,
    get_score_fives,
    get_score_sixes,
    get_score_three_of_a_kind,
    get_score_four_of_a_kind,
    get_score_full_house,
    get_score_small_straight,
    get_score_large_straight,
    get_score_yahtzee,
    get_score_choice,
]