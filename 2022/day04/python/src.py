"""
Day 3, 2022 of Advent of Code: Python
"""
from typing import List, Union
import read_file as rf

DEMO_FLAG = 0


def read_file(filename: str) -> List[List[str]]:
    """
    overloaded read_file function to return with better format/object
    """
    task_splits = rf.read_file(filename)
    pair_splits = [task.split(",") for task in task_splits]
    return pair_splits


def sign(val: Union[int, float]) -> int:
    """
    return sign of value:
        1 if positive
        -1 if negative
        0 if 0
    """
    return 0 if val == 0 else int(val / abs(val))


def check_encapsulation(task_split: List[str]) -> int:
    """
    method to check for total task encapsulation

    if any of task num is equal then guaranteed for encapsulation
    else must ensure that either e2 max > e1 max AND e2 min < e1 min
        OR e2 max < e1 max AND e2 min > e1 min; can check via sign of diff

    """
    # split and conv into ints
    e1_min, e1_max = map(int, task_split[0].split("-"))
    e2_min, e2_max = map(int, task_split[1].split("-"))

    min_diff = sign(e2_min - e1_min)
    max_diff = sign(e2_max - e1_max)

    if min_diff == 0 or max_diff == 0:
        return 1

    return min_diff != max_diff


def check_overlap(task_split: List[str]) -> int:
    """
    method to check for any overlap

    if any task num is equal then guaranteed for overlap
    else check inner differences
        if inner diff have same sign then one is completely outside the other
        if inner diff have diff sign then ranges overlap by definition
    """
    # split and conv into ints
    e1_min, e1_max = map(int, task_split[0].split("-"))
    e2_min, e2_max = map(int, task_split[1].split("-"))

    # take sign; magnitude is irrelevant
    min_sub_max = sign(e1_min - e2_max)
    max_sub_min = sign(e1_max - e2_min)

    if min_sub_max == 0 or max_sub_min == 0:
        return 1

    return min_sub_max != max_sub_min


def part_one(filename: str) -> int:
    """
    exposed function for finding solution
    """
    pair_splits: List[List[str]] = read_file(filename)

    return sum(check_encapsulation(task) for task in pair_splits)


def part_two(filename: str) -> int:
    """
    Solution for Part 2
    """
    pair_splits: List[List[str]] = read_file(filename)
    return sum(check_overlap(task) for task in pair_splits)


if __name__ == "__main__":
    if DEMO_FLAG:
        FILE_NAME = "../demo.txt"
    else:
        FILE_NAME = "../input.txt"
    print(f"FILE: {FILE_NAME}")

    output_one = part_one(FILE_NAME)
    print(f"Part One: {output_one}")

    output_two = part_two(FILE_NAME)
    print(f"Part Two: {output_two}")
