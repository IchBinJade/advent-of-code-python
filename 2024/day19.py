"""
Author: IchBinJade
Date  : 2024-12-21
AoC 2024 Day 19 - https://adventofcode.com/2024Y/day/19
"""

import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file

def can_make_design(patterns, design):
    if not design:
        return True
    
    for pattern in "".join(patterns).split(", "):
        #print(f"pattern = {pattern} ; design = {design}")
        if design.startswith(pattern):
            if can_make_design(patterns, design[len(pattern):]):
                return True
        
    return False


def part_one(data_input):
    count = 0
    empty_idx = data_input.index("")
    patterns, designs = data_input[:empty_idx], data_input[empty_idx + 1:]
    
    for design in designs:
        if can_make_design(patterns, design):
            count += 1
    
    return count


def part_two(data_input):
    pass


TEST_INPUT = ['r, wr, b, g, bwu, rb, gb, br', '', 'brwrr', 'bggr', 'gbbr', 'rrbgbr', 'ubwu', 'bwurrg', 'brgr', 'bbrgwb']


if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(19, 2024)
    
    # input_data = TEST_INPUT

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
