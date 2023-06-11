"""
Day 1, 2022 of Advent of Code: Python
"""
from typing import List

DEMO_FLAG = 0


def read_file(filename: str) -> List[List[int]]:
    """
    Read in file of list of values separated by newlines
    """
    value_list: List[List[int]] = []
    current_list: List[int] = []

    with open(filename, encoding="utf-8") as file_p:
        file_line = file_p.readline()
        while file_line:
            if file_line == "\n":
                value_list.append(current_list)
                current_list = []
            else:
                current_list.append(int(file_line))
            file_line = file_p.readline()
        value_list.append(current_list)

    return value_list


def part_one(filename: str) -> int:
    """
    exposed function for finding solution
    """
    max_val: int = 0
    elf_colony = read_file(filename=filename)
    for elf in elf_colony:
        elf_sum = sum(elf)
        max_val = max(max_val, elf_sum)

    return max_val


def part_two(filename: str, top_n: int) -> int:
    """
    Solution for Part 2
    """
    elf_sums: List[int] = []
    elf_colony = read_file(filename=filename)
    for elf in elf_colony:
        elf_sums.append(sum(elf))

    sorted_elves = sorted(elf_sums, reverse=True)
    return sum(sorted_elves[:top_n])


if __name__ == "__main__":
    if DEMO_FLAG:
        FILE_NAME = "../demo.txt"
    else:
        FILE_NAME = "../input.txt"
    print(f"FILE: {FILE_NAME}")

    output_one = part_one(FILE_NAME)
    print(f"Part One: {output_one}")

    output_two = part_two(FILE_NAME, 3)
    print(f"Part Two: {output_two}")
