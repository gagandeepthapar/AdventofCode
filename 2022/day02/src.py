"""
Day 2, 2022 of Advent of Code: Python
"""
from typing import List, Dict, Union
from enum import IntEnum

import read_file as rf

DEMO_FLAG = 0

class Play(IntEnum):
    """
    custom class to compare throws together
    """
    A = 1
    B = 2
    C = 3

    X = 1
    Y = 2
    Z = 3


# Map of which keys beat which values
k_beats_v: Dict[Play, Play] = {Play.X: Play.C,
                               Play.Y: Play.A,
                               Play.Z: Play.B}

# Map of which keys LOSE to which values
k_loses_v: Dict[Play, Play] = {v:k for k, v in k_beats_v.items()}


def read_file(filename:str) -> List[str]:
    """ 
    overloaded read_file function to return with better format/object
    """
    values = rf.read_file(filename)

    # convert into Play class for easy comparison
    values = [[Play[turn[0]], Play[turn[-1]]]for turn in values]
    return values


def check_round(throws: List[Play]) -> int:
    """ 
    return score of round based on throw of player and opponent
    throws: ['Opponent', 'Player']
    Lose => +0
    Tie => +3
    Win => +6
    """

    min_score:int = int(throws[-1])

    # Tie case
    if len(set(throws)) == 1:
        return 3 + min_score

    # Win case
    if k_beats_v[throws[-1]] == throws[0]:
        return 6 + min_score

    # Lose case
    return min_score


def think_of_move(throws:List[Play]) -> int:
    """ 
    return score but X/Y/Z pertain to Lose/Tie/Win respectively w.r.t. Opponent
    """
    # Lose Condition
    if throws[-1] == Play.X:
        my_throw = k_beats_v[throws[0]]

    # Tie Condition
    if throws[-1] == Play.Y:
        my_throw = throws[0]

    # Win Condition
    if throws[-1] == Play.Z:
        my_throw = k_loses_v[throws[0]]

    return check_round([throws[0], my_throw])


def part_one(filename:str) -> int:
    """ 
    exposed function for finding solution
    """
    max_val: int = 0
    all_throws = read_file(filename)
    max_val = sum([check_round(throw) for throw in all_throws])

    return max_val


def part_two(filename:str) -> int:
    """ 
    Solution for Part 2
    """
    max_val:int = 0
    all_throws = read_file(filename)
    max_val = sum([think_of_move(throw) for throw in all_throws])

    return max_val

if __name__ == '__main__':
    if DEMO_FLAG:
        FILE_NAME = 'demo.txt'
    else:
        FILE_NAME = 'input.txt'
    print(f'FILE: {FILE_NAME}')

    output_one = part_one(FILE_NAME)
    print(f'Part One: {output_one}')

    output_two = part_two(FILE_NAME)
    print(f'Part Two: {output_two}')
