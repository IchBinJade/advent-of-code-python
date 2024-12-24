"""
Author: IchBinJade
Date  : 2024-12-23
AoC 2023 Day 12 - https://adventofcode.com/2023/day/12
"""

import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file
from functools import cache


@cache
def count_arrangements(pattern, block, cache={}):
        
    if pattern == "":
        if block == ():
            return 1
        else:
            return 0
        
    if block == ():
        if "#" in pattern:
            return 0
        return 1
    
    key = (pattern, block)
    if key in cache:
        return cache[key]
    
    count = 0
    if pattern[0] in ".?":
        count += count_arrangements(pattern[1:], block)
        
    if pattern[0] in "#?":
        block_size = block[0]
        if block_size <= len(pattern) and "." not in pattern[:block_size] and (block_size == len(pattern) or pattern[block_size] != "#"):
            count += count_arrangements(pattern[block_size + 1:], block[1:])
    
    cache[key] = count
            
    return count


def part_one(data_input):
    total = 0
    
    for line in data_input:
        pattern, block = line.split(" ")
        block = tuple(map(int, block.split(",")))
        total += count_arrangements(pattern, block)
    
    return total


def part_two(data_input):
    total = 0
    
    for line in data_input:
        pattern, block = line.split(" ")
        # "Unfold" the pattern
        pattern = "?".join(([pattern] * 5))
        
        block = tuple(map(int, block.split(",")))
        block *= 5
        total += count_arrangements(pattern, block)
    
    return total


if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(12, 2023)

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}") # P1 test = 21
    print(f"Part 2 = {part_two(input_data)}") # P2 test = 525152

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
