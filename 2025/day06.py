"""
Author: IchBinJade
Date  : 2025-12-08
AoC 2025 Day 6 - https://adventofcode.com/2025/day/6

With thanks to JR and HyperNeutrino for helping me understand
the problem for part 2 better!
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


def separate_math_problems(cols):
    groups = []
    curr_group = []
    
    for col in cols:
        if set(col) == {" "}:
            if curr_group:
                groups.append(curr_group)
            curr_group = []
        else:
            curr_group.append(col)
            
    if curr_group:
        groups.append(curr_group)
        
    return groups


def rebuild_num(num_col):
    num_str = ""
    for digit in num_col[:-1]:
        if digit.isdigit():
            num_str += digit
            
    return int(num_str) if num_str else None


def process_problems(groups):
    total = 0
    for group in groups:
        nums = []
        operator = group[0][-1]
        for num_col in group:
            num = rebuild_num(num_col)
            if num is not None:
                nums.append(num)
        
        # Do Calcs
        if not nums:
            continue
        calc_list = nums[::-1]
        running_tot = calc_list[0]
        for i in range(1, len(calc_list)):
            next_num = calc_list[i]
            running_tot = do_calc(next_num, operator, running_tot)
            
        total += running_tot
        
    return total    


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
    grid = [list(row.strip("\n")) for row in data_input]

    column_list = list(zip(*grid))
    
    groups = separate_math_problems(column_list)
    
    total = process_problems(groups)
    
    return total



if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(6, 2025)

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
