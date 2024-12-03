"""
Author: IchBinJade
Date  : 2024-12-03
AoC 2024 Day 3 - https://adventofcode.com/2024/day/3
"""

import sys
import os
import time
import re

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file

MUL_MASK = r"mul\((\d+),(\d+)\)"
DO_MASK = r"mul\(\d+,\d+\)|don't\(\)|do\(\)"

def part_one(data_input):
    # Use regex to match "mul(#,#)" as a list of tuples then return the sum of their products
    match_list = []
    for line in data_input:
        matches = re.findall(MUL_MASK, line)
        matches_list = [(int(x), int(y)) for x, y in matches]
        match_list.extend(matches_list) # Extend flattens and will add the tuples, not list of tuples like append
    
    total = sum(x * y for x, y in match_list)
    
    return total


def part_two(data_input):
    # Get matches, including the do and don't combos to use as a flag
    match_list = []
    add_me = True # Line starts enabled

    for line in data_input:
        matches = re.findall(DO_MASK, line)
        for match in matches:
            # Set or check the flag
            if match == "do()":
                add_me = True
            elif match == "don't()":
                add_me = False
            elif add_me and match.startswith("mul"): # Ignore other tuples of numbers for they are false gods
                # Extract the tuples and add to list
                match_tuple = tuple([int(x) for x in match.strip("mul()").split(",")])
                match_list.append(match_tuple)

    total = sum(x * y for x, y in match_list)
    
    return total


if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(3, 2024)

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
