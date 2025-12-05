"""
Author: IchBinJade
Date  : 2025-12-05
AoC 2025 Day 5 - https://adventofcode.com/2025/day/5

Part 2: Thanks to Vallentin for their answer on StackOverflow for merging ranges
"""

import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file


def merge_overlapped_ranges(fresh_ranges):
    fresh_list = [[int(n) for n in range_str.split("-")] for range_str in fresh_ranges]
    fresh_list.sort(key=lambda interval: interval[0])
    new_list = [fresh_list[0]]
    
    for current in fresh_list:
        previous = new_list[-1]
        if current[0] <= previous[1]:
            previous[1] = max(previous[1], current[1])
        else:
            new_list.append(current)
        
    return new_list


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
    fresh_count = 0
    split_idx = data_input.index("")
    fresh_ranges = data_input[:split_idx]
    fresh_list = merge_overlapped_ranges(fresh_ranges)
    
    for fresh_range in fresh_list:
        start, end = fresh_range[0], fresh_range[1]
        fresh_count += (end - start) + 1
        
    return fresh_count



if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(5, 2025)

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
