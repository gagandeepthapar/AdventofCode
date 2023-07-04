""" 
Test cases for Day 4, 2022 Advent of Code
"""

import src as s

DEMO_FILE = "../demo.txt"
INPUT_FILE = "../input.txt"


class TestReadFile:
    """
    Test class for read file
    """

    def test_sanity(self):
        """
        Sanity check for pytest
        """
        test = 1 + 2
        expect = 3
        assert test == expect

    def test_demo(self):
        """
        Copy of Demo values
        """
        file = DEMO_FILE
        rucksack = s.read_file(file)
        assert rucksack == [
            ["2-4", "6-8"],
            ["2-3", "4-5"],
            ["5-7", "7-9"],
            ["2-8", "3-7"],
            ["6-6", "4-6"],
            ["2-6", "4-8"],
        ]


class TestDemoOne:
    """
    Test class for pytest
    """

    def test_sanity(self):
        """
        Sanity check for pytest
        """
        test = 1 + 2
        expect = 3
        assert test == expect

    def test_demo(self):
        """
        Solution provided by Advent of Code
        """
        file = DEMO_FILE
        rucksack = s.part_one(file)
        assert rucksack == 2

    def test_input_one(self):
        """
        Solution tested against AoC
        """
        file = INPUT_FILE
        rucksack = s.part_one(file)
        assert rucksack == 584


class TestDemoTwo:
    """
    Test class for pytest, part 2
    """

    def test_sanity(self):
        """
        Sanity check for pytest
        """
        test = 1 + 2
        expect = 3
        assert test == expect

    def test_demo(self):
        """
        Solution provided by Advent of Code
        """
        file = DEMO_FILE
        rucksack = s.part_two(file)
        assert rucksack == 4

    def test_input_one(self):
        """
        Solution tested against AoC
        """
        file = INPUT_FILE
        rucksack = s.part_two(file)
        assert rucksack == 933
