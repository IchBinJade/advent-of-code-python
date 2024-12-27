"""
Author: IchBinJade
Date  : 2024-12-27
AoC 2017 Day 2 - https://adventofcode.com/2017/day/2

Number manipulation and comparing pairs of numbers in an array
"""

import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file


def part_one(data_input):
    total = 0
    for line in data_input:
        num_arr = [int(char) for char in line.split()]
        hi, lo = max(num_arr), min(num_arr)
        total += hi - lo

    return total


def part_two(data_input):
    total = 0
    for line in data_input:
        num_arr = list(map(int, line.split()))
        for i in range(len(num_arr)):
            for j in range(i + 1, len(num_arr)):
                if num_arr[i] % num_arr[j] == 0:
                    total += num_arr[i] // num_arr[j]
                elif num_arr[j] % num_arr[i] == 0:
                    total += num_arr[j] // num_arr[i]
    
    return total


if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(2, 2017)

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
