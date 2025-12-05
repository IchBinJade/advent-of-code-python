"""
Author: IchBinJade
Date  : 2025-12-05
AoC 2025 Day 5 - https://adventofcode.com/2025/day/5

TODO: Solve part 2
"""

import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file


def get_array_from_ranges(fresh_ranges):
    new_set = set()
    for range_str in fresh_ranges:
        start_str, end_str = range_str.split("-")
        start, end = int(start_str), int(end_str)
        for num in range(start, end + 1):
            new_set.add(num)
        
    return list(new_set)


def part_one(data_input):
    fresh_count = 0
    split_idx = data_input.index("")
    fresh_ranges, ingredients = data_input[:split_idx], [int(a) for a in data_input[split_idx + 1:]]
    
    for ingredient in ingredients:
        for fresh_range in fresh_ranges:
            start_str, end_str = fresh_range.split("-")
            start, end = int(start_str), int(end_str)
            if ingredient >= start and ingredient <= end:
                fresh_count += 1
                break
    
    return fresh_count


def part_two(data_input):
    pass



if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(5, 2025)
    # input_data = ['3-5', '10-14', '16-20', '12-18', '', '1', '5', '8', '11', '17', '32']

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
