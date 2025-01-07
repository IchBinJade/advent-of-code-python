"""
Author: IchBinJade
Date  : 2025-01-07
AoC 2016 Day 3 - https://adventofcode.com/2016/day/3

Transposing input into columns and extracting triples to find possible triangles
"""

import sys
import os
import time
import re

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file


def can_make_triangle(line):
    sides = [int(x) for x in re.findall(r"(\d+)", line)]

    side1, side2, side3 = sorted(sides)
    
    return side1 + side2 > side3


def part_one(data_input):
    possible_count = 0
    for line in data_input:
        if can_make_triangle(line):
            possible_count += 1
    
    return possible_count


def part_two(data_input):
    possible_count = 0
    
    for idx in range(len(data_input[0].split())):
        for jdx in range(0, len(data_input), 3):
            line = " ".join([data_input[jdx].strip().split()[idx], data_input[jdx+1].strip().split()[idx], data_input[jdx+2].strip().split()[idx]])
            if can_make_triangle(line):
                possible_count += 1
    
    return possible_count


if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(3, 2016)

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
