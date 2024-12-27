"""
Author: IchBinJade
Date  : 2024-12-27
AoC 2018 Day 1 - https://adventofcode.com/2018/day/1

Utilises: Itertools "cycle" to create a looping/repeating iterable
"""

import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file
from itertools import cycle

def part_one(data_input):
    total = 0
    for num_str in data_input:
        total += int(num_str)
    
    return total


def part_two(data_input):
    seen_num = set()
    input_cycle = cycle(data_input)
    result = 0
    for num_str in input_cycle:
        result += int(num_str)
        if result in seen_num:
            return result
        else:
            seen_num.add(int(result))


if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(1, 2018)

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
