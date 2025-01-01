"""
Author: IchBinJade
Date  : 2025-01-01
AoC 2015 Day 12 - https://adventofcode.com/2015/day/12

Recursive processing of an object/dict
"""

import sys
import os
import time
import re
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file


def recursive_sum(obj):
    # Process a dict
    if isinstance(obj, dict):
        if "red" in obj.values():
            return 0
        return sum(recursive_sum(value) for value in obj.values())
    # Process arrays
    elif isinstance(obj, list):
        return sum(recursive_sum(item) for item in obj)
    # Process ints
    elif isinstance(obj, int):
        return obj
        
    return 0


def part_one(data_input):
    result = [int(x) for x in re.findall(r"(-?\d+)", data_input[0])]
    
    return sum(result)


def part_two(data_input):
    """ 
    Convert the string to an object (dict) and recursively sum
    """
    data = json.loads(data_input[0])
    
    return recursive_sum(data)


if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(12, 2015)

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
