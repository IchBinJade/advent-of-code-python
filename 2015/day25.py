"""
Author: IchBinJade
Date  : 2025-01-07
AoC 2015 Day 25 - https://adventofcode.com/2015/day/25
"""

import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file


def find_next_code(n):
    return (n * 252533) % 33554393

def part_one(data_input):
    row, col = int(data_input[0].split()[15].strip(",")), int(data_input[0].split()[17].strip("."))
    n = 20151125
    n_count = sum(range(row + col - 1)) + col
    for _ in range(n_count - 1):
        n = find_next_code(n)
    
    return n


if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(25, 2015)

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
