"""
Author: IchBinJade
Date  : 2024-12-26
AoC 2017 Day 1 - https://adventofcode.com/2017/day/1
"""

import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file

def part_one(data_input):
    input_str = "".join(data_input)
    total = 0
    for idx in range(len(input_str)):
        if idx == len(input_str) - 1:
            if input_str[idx] == input_str[0]:
                total += int(input_str[idx])    
        elif input_str[idx] == input_str[idx + 1]:
            total += int(input_str[idx])
        
    return total


def part_two(data_input):
    input_str = "".join(data_input)
    total = 0
    length = len(input_str)
    for idx in range(length):
        half_idx = (idx + length // 2) % length
        if input_str[idx] == input_str[half_idx]:
            total += int(input_str[idx])
        
    return total


if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(1, 2017)

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
