"""
Author: IchBinJade
Date  : 2024-12-31
AoC 2015 Day 1 - https://adventofcode.com/2015/day/1
"""

import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file

def part_one(data_input):
    total = 0
    for char in data_input[0]:
        if char == "(":
            total += 1
        else:
            total -= 1
    
    return total


def part_two(data_input):
    total = 0
    for idx, char in enumerate(data_input[0]):
        if char == "(":
            total += 1
        else:
            total -= 1
        if total == -1:
            return idx + 1
    
    return total


if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(1, 2015)

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
