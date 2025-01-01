"""
Author: IchBinJade
Date  : 2025-01-01
AoC 2015 Day 8 - https://adventofcode.com/2015/day/8

Evaluate code and in-memory string representations using eval()
"""

import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file

def part_one(data_input):
    total = 0
    
    for line in data_input:
        memory_count = len(eval(line))
        code_count = len(line)
        total += code_count - memory_count
               
    return total


def part_two(data_input):
    total = 0
    
    for line in data_input:
        orig_count = len(line)
        new_count = len(line.replace("\\", "\\\\").replace('"', '\\"'))
        total += new_count - orig_count + 2
               
    return total


if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(8, 2015)

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
