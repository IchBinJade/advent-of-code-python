"""
Author: IchBinJade
Date  : 2024-12-11
AoC 2024 Day 11 - https://adventofcode.com/2024/day/11
"""

import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file
from collections import Counter


def do_blink_splits(initial_stones, loop_me):
    for _ in range(loop_me):
        split_stones = []
        for idx, stone_int in enumerate(initial_stones):
            stone_str = str(stone_int)
            if stone_int == 0:
                split_stones.append(1)
            elif len(stone_str) % 2 == 0:
                first_int, second_int = stone_str[:len(stone_str) // 2], stone_str[len(stone_str) // 2:]
                split_stones.append(int(first_int))
                split_stones.append(int(second_int))
            else:
                split_stones.append(stone_int * 2024)
        initial_stones = split_stones
            
    return initial_stones


def part_two_blink(stones):
    new_stones = Counter()
    for stone, val in stones.items():
        stone_str = str(stone)
        if stone == 0:
            new_stones[1] += val
        elif len(stone_str) % 2 == 0:
            first_int, second_int = stone_str[:len(stone_str) // 2], stone_str[len(stone_str) // 2:]
            new_stones[int(first_int)] += val
            new_stones[int(second_int)] += val
        else:
            new_stones[stone * 2024] += val
            
    return new_stones


def part_one(data_input):
    initial_stones = [int(stone) for stone in data_input[0].split()]
    
    split_stones = do_blink_splits(initial_stones, 25)
    
    return len(split_stones)


def part_two(data_input):
    initial_stones = [int(stone) for stone in data_input[0].split()]
    stones = Counter(initial_stones)
    
    for _ in range(75):
        stones = part_two_blink(stones)
    
    return sum(stones.values())



if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(11, 2024)
    
    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
