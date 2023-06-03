"""
Utility function to read input text files
"""
from typing import List

def read_file(filename:str) -> List[List]:
    """ 
    Read in file of list of values separated by newlines
    """

    input_data: List = []

    with open(filename, encoding='utf-8') as file_p:
        file_line = file_p.readline()
        while file_line:
            input_data.append(file_line)

    return input_data
