"""
Author: IchBinJade
Date  : 2024-11-27
AoC 2023 Day 5 - https://adventofcode.com/2023/day/5
"""

import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file

def part_one(data_input):
    # Create an object class for the input?
    maps = [line for line in data_input if line]
    seeds = [seed for seed in maps[0].split() if seed.isdigit()]
    print(f"seeds >>> {seeds}")
    return maps


def part_two(data_input):
    pass



if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(5, 2023)

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
