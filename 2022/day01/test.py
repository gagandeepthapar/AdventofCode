""" 
Test cases for Day 1, 2022 Advent of Code
"""

from main import read_file, part_one, part_two

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
        max_elf = read_file(file)
        assert max_elf == [[1_000, 2_000, 3_000],
                           [4_000],
                           [5_000, 6_000],
                           [7_000,8_000,9_000],
                           [10_000]]

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


    def test_demo(self):
        """ 
        Solution provided by Advent of Code
        """
        file = "demo.txt"
        max_elf = part_one(file)
        assert max_elf == 24000


    def test_input_one(self):
        """
        Solution tested against AoC
        """
        file = 'input.txt'
        max_elf = part_one(file)
        assert max_elf == 66719

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
        max_elf = part_two(file, 3)
        assert max_elf == 45000


    def test_input_one(self):
        """
        Solution tested against AoC
        """
        file = 'input.txt'
        max_elf = part_two(file, 3)
        assert max_elf == 198551
