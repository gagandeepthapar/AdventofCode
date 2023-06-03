""" 
Test cases for Day 2, 2022 Advent of Code
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
        rps_round = s.read_file(file)
        assert rps_round == [[s.Play.A, s.Play.Y],
                             [s.Play.B, s.Play.X],
                             [s.Play.C, s.Play.Z]]

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

    def test_check_res(self):
        """ 
        Testing function to check single throw
        """
        test = s.check_round([s.Play.A, s.Play.X])
        expect = 4

        assert test == expect

    def test_demo(self):
        """ 
        Solution provided by Advent of Code
        """
        file = "demo.txt"
        max_elf = s.part_one(file)
        assert max_elf == 15


    def test_input_one(self):
        """
        Solution tested against AoC
        """
        file = 'input.txt'
        max_elf = s.part_one(file)
        assert max_elf == 15422

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
        rps_score = s.part_two(file)
        assert rps_score == 12


    def test_input_one(self):
        """
        Solution tested against AoC
        """
        file = 'input.txt'
        rps_score = s.part_two(file)
        assert rps_score == 15442
