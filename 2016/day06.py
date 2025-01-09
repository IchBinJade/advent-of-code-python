"""
Author: IchBinJade
Date  : 2025-01-09
AoC 2016 Day 6 - https://adventofcode.com/2016/day/6

Transpose input into columns and return string of most/least common characters
"""

import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file
from collections import Counter

def part_one(data_input):
    # Find the most common character in each column
    grid = [list(row) for row in data_input]
    transposed_grid = list(zip(*grid))
    
    message = ""
    for idx in range(len(transposed_grid)):
        col = transposed_grid[idx]
        freq_char = Counter(col).most_common(1)[0][0]
        message += freq_char
    
    return message


def part_two(data_input):
    # Find the least common character in each column
    grid = [list(row) for row in data_input]
    transposed_grid = list(zip(*grid))
    
    message = ""
    for idx in range(len(transposed_grid)):
        col = transposed_grid[idx]
        freq_char = Counter(col).most_common()[-1][0]
        message += freq_char
    
    return message


if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(6, 2016)

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
