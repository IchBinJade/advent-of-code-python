"""
Author: IchBinJade
Date  : 2025-12-08
AoC 2025 Day 6 - https://adventofcode.com/2025/day/6

TODO: Solve Part 2
"""

import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file

import re

SPLIT_MASK = r"\s+"


def clean_line(line):
    stripped_line = line.strip()
    return re.split(SPLIT_MASK, stripped_line)


def create_grid(data_input):
    grid = []
    for line in data_input:
        row_values = clean_line(line)
        grid.append(row_values)
        
    return grid


def do_calc(num, operator, result):
    match operator:
        case "+":
            result += num
        case "-":
            result -= num
        case "*":
            result *= num
        case "/":
            result /= num
        case _:
            pass
        
    return result


def part_one(data_input):
    grid = create_grid(data_input)
    
    rows = len(grid)
    cols = len(grid[0])
    
    total = 0
    for col_idx in range(cols):
        result = None
        operator = grid[rows - 1][col_idx]
        for row_idx in range(rows - 1):
            num = int(grid[row_idx][col_idx])
            if result == None:
                result = num
            else:
                result = do_calc(num, operator, result)
        total += result
        
    return total
    

def part_two(data_input):
    pass



if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(6, 2025)
    # input_data = ['123 328  51 64 ', ' 45 64  387 23 ', '  6 98  215 314', '*   +   *   +  ']

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
