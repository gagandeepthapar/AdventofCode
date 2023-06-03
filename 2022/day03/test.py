""" 
Test cases for Day 3, 2022 Advent of Code
"""

import src as s

class TestReadFile:
    """ 
    Test class for read file
    """
    def test_sanity(self):
        """ 
        Sanity check for pytest
        """
        test = 1+2
        expect = 3
        assert test == expect


    def test_demo(self):
        """ 
        Copy of Demo values 
        """
        file = "demo.txt"
        rucksack = s.read_file(file)
        assert rucksack == ['vJrwpWtwJgWrhcsFMMfFFhFp',
                             'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
                             'PmmdzqPrVvPwwTWBwg',
                             'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
                             'ttgJtRGJQctTZtZT',
                             'CrZsJsPPZsGzwwsLwLmpwMDw']


class TestDemoOne:
    """ 
    Test class for pytest
    """
    def test_sanity(self):
        """ 
        Sanity check for pytest
        """
        test = 1+2
        expect = 3
        assert test == expect


    def test_find_letter(self):
        """ 
        test set intersection for letters
        """
        rucksack = 'vJrwpWtwJgWrhcsFMMfFFhFp'
        part_a = rucksack[:len(rucksack)//2]
        part_b = rucksack[len(rucksack)//2:]
        test = s.find_letter([part_a, part_b])
        expect = 'p'
        assert test == expect


    def test_char_to_prio_lower(self):
        """ 
        test set intersection for lowecase letters
        """
        char = ['a']
        test = [1]
        expect = s.chars_to_prio(char)
        assert test == expect


    def test_char_to_prio_upper(self):
        """ 
        test set intersection for uppercase letters
        """
        char = ['A']
        test = [27]
        expect = s.chars_to_prio(char)
        assert test == expect


    def test_demo(self):
        """ 
        Solution provided by Advent of Code
        """
        file = "demo.txt"
        rucksack = s.part_one(file)
        assert rucksack == 157


    def test_input_one(self):
        """
        Solution tested against AoC
        """
        file = 'input.txt'
        rucksack = s.part_one(file)
        assert rucksack == 8123

class TestDemoTwo:
    """ 
    Test class for pytest, part 2
    """
    def test_sanity(self):
        """ 
        Sanity check for pytest
        """
        test = 1+2
        expect = 3
        assert test == expect


    def test_demo(self):
        """ 
        Solution provided by Advent of Code
        """
        file = "demo.txt"
        rucksack = s.part_two(file, 3)
        assert rucksack == 70


    def test_input_one(self):
        """
        Solution tested against AoC
        """
        file = 'input.txt'
        rucksack = s.part_two(file, 3)
        assert rucksack == 2620
