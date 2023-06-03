"""
Day 3, 2022 of Advent of Code: Python
"""
from typing import List
import read_file as rf

DEMO_FLAG = 1


def read_file(filename:str) -> List[str]:
    """ 
    overloaded read_file function to return with better format/object
    """
    return rf.read_file(filename)


def find_letter(rucksack:str) -> str:
    """ 
    returns common letter in list of rucksacks
    """
    # find set of letters in each input
    list_of_sets = [set([letter for letter in pack]) for pack in rucksack]

    # intersection of sets returns the common letter(s); guaranteed only 1
    common_letter = set.intersection(*list_of_sets)
    return list(common_letter)[0]


def chars_to_prio(charlist:List[str]) -> int:
    """ 
    convert list of letters to priority
    """
    upper_prio_start = 27
    lower_prio_start = 1
    prio_list:List[int] = []

    upper_ord_diff = ord('A') - upper_prio_start
    lower_ord_diff = ord('a') - lower_prio_start

    for char in charlist:
        char_ord = ord(char)
        if char_ord < 97:
            prio_list.append(char_ord - upper_ord_diff)
        else:
            prio_list.append(char_ord - lower_ord_diff)

    return prio_list


def part_one(filename:str) -> int:
    """ 
    exposed function for finding solution
    """
    rucksack = read_file(filename)
    common_letters:List[str] = []
    for comp in rucksack:
        # split each rucksack into 2 equal parts
        comp_a = comp[:len(comp)//2]
        comp_b = comp[len(comp)//2:]

        # find common letter between two halves
        common_letters.append(find_letter([comp_a, comp_b]))

    rucksack_value = sum(chars_to_prio(common_letters))

    return rucksack_value


def part_two(filename:str, group_size:int) -> int:
    """ 
    Solution for Part 2
    """
    rucksack = read_file(filename)

    # separate rucksacks into groups of `group_size`
    elf_groups = [rucksack[i:i+group_size] for i in range(0, len(rucksack), group_size)]

    # find group badge by common letter
    common_letter:List[str] = []
    for triple in elf_groups:
        common_letter.append(find_letter(triple))

    # convert letter to priority
    rucksack_value = sum(chars_to_prio(common_letter))
    return rucksack_value


if __name__ == '__main__':
    if DEMO_FLAG:
        FILE_NAME = 'demo.txt'
    else:
        FILE_NAME = 'input.txt'
    print(f'FILE: {FILE_NAME}')

    output_one = part_one(FILE_NAME)
    print(f'Part One: {output_one}')

    output_two = part_two(FILE_NAME, 3)
    print(f'Part Two: {output_two}')
