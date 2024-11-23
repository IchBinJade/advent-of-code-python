"""
Author: IchBinJade
Date  : 2023-01-31
AoC Day 3 - https://adventofcode.com/2022/day/3
"""

import sys
import os
import time
import string

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file

def part_one(input):
    # What is the sum of the priorities of those item types?
    lowers = string.ascii_lowercase
    uppers = string.ascii_uppercase
    priority = 0
    total_priority = 0

    for rucksack in input:
        half = len(rucksack)//2
        comp_one = set(rucksack[:half])
        comp_two = set(rucksack[half:])
        common = next(iter(comp_one.intersection(comp_two)))
        if common in lowers:
            priority = 1 + lowers.index(common)
        elif common in uppers:
            priority = 27 + uppers.index(common)
        
        total_priority += priority

    return total_priority


def part_two(input):
    lowers = string.ascii_lowercase
    uppers = string.ascii_uppercase
    priority = 0
    total_priority = 0

    while len(input) > 0:
        first = set(input.pop())
        second = set(input.pop())
        third = set(input.pop())
        common = next(iter(first.intersection(second, third)))
        if common in lowers:
            priority = 1 + lowers.index(common)
        elif common in uppers:
            priority = 27 + uppers.index(common)
        
        total_priority += priority

    return total_priority



if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(3, 2022)

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")