"""
Author: IchBinJade
Date  : 2024-12-31
AoC 2015 Day 5 - https://adventofcode.com/2015/day/5

Identifying string patterns with regex
"""

import sys
import os
import time
import re

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file

# Contains: At least 3 vowels, at least 1 doubled letter, does not contain
#           substrings ab, cd, pq or xy
P1_PATTERN = r"^(?=(.*[aeiou]){3,})(?=.*([a-z])\2)(?!.*(?:ab|cd|pq|xy)).*$"

# Contains: A pair of two letters that appears at least twice in the string without overlapping,
#           A letter that repeats with exactly one letter between them
P2_PATTERN = r"^(?=(.*([a-z]{2}).*\2))(?=.*([a-z]).\3).*"


def part_one(data_input):
    total = 0
    for strings in data_input:
        if re.match(P1_PATTERN, strings):
            total += 1
    
    return total


def part_two(data_input):
    total = 0
    for strings in data_input:
        if re.match(P2_PATTERN, strings):
            total += 1
    
    return total  


if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(5, 2015)

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
