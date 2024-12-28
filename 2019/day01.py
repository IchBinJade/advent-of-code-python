"""
Author: IchBinJade
Date  : 2024-12-28
AoC 2019 Day 1 - https://adventofcode.com/2019/day/1

Recursion of number calculations
"""

import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file


def calc_fuel(module):
    return int(module) // 3 - 2


def part_one(data_input):
    total = 0
    for entry in data_input:
        mass = calc_fuel(entry)
        total += mass
        
    return total


def part_two(data_input):
    total = 0
    for entry in data_input:
        while True:
            fuel_needed = calc_fuel(entry)
            if fuel_needed <= 0:
                break
            total += fuel_needed
            entry = fuel_needed
    
    return total


if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(1, 2019)

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
