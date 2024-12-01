"""
Author: IchBinJade
Date  : 2024-12-01
AoC 2024 Day 1 - https://adventofcode.com/2024/day/1
"""

import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file

def part_one(data_input):
    left_list = [int(line.split("  ")[0]) for line in data_input]
    right_list = [int(line.split("  ")[-1]) for line in data_input]
    left_list.sort()
    right_list.sort()
    pairs = [(left_location, right_location) for left_location, right_location in zip(left_list, right_list)]
    distances = [abs(left_location - right_location) for left_location, right_location in pairs]
    return sum(distances)


def part_two(data_input):
    left_list = [int(line.split("  ")[0]) for line in data_input]
    right_list = [int(line.split("  ")[-1]) for line in data_input]
    counts = [left_location * (right_list.count(left_location)) for left_location in left_list]
    return sum(counts)



if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(1, 2024)

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
