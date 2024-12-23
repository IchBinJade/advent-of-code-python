"""
Author: IchBinJade
Date  : 2024-12-08
AoC 2023 Day 10 - https://adventofcode.com/2023/day/10

2024-12-23: Solved part 2 (thanks @mebeim!)
"""

import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file
from collections import deque


def find_looped_route(start_pos, grid):
    looped_list = {start_pos}
    queued_list = deque([start_pos])  
    
    while queued_list:
        row, col = queued_list.popleft()
        character = grid[row][col]
        # Moving Up
        if row > 0 and character in "S|LJ" and grid[row - 1][col] in "|7F" and (row - 1, col) not in looped_list:
            queued_list.append((row - 1, col))
            looped_list.add((row - 1, col))
        # Moving Down
        if row < len(grid) - 1 and character in "S|7F" and grid[row + 1][col] in "|JL" and (row + 1, col) not in looped_list:
            queued_list.append((row + 1, col))
            looped_list.add((row + 1, col))
        # Moving Left
        if col > 0 and character in "S-J7" and grid[row][col - 1] in "-LF" and (row, col -1) not in looped_list:
            queued_list.append((row, col - 1))
            looped_list.add((row, col - 1))
        # Moving Right
        if col < len(grid[row]) and character in "S-LF" and grid[row][col + 1] in "-J7" and (row, col + 1) not in looped_list:
            queued_list.append((row, col + 1))
            looped_list.add((row, col + 1))
    
    return looped_list


def calc_inner_area(grid, loop_list):
    area = 0
    for r_idx, row in enumerate(grid):
        inside = False
        for c_idx, cell in enumerate(row):
            if (r_idx, c_idx) not in loop_list:
                area += inside
            else:
                inside = inside ^ (cell in "|F7")
    
    return area


def part_one(data_input):
    grid = [list(row) for row in data_input]

    for row_idx, row in enumerate(grid):
        if "S" in row:
            col_idx = row.index("S")
            start_pos = (int(row_idx), int(col_idx))
            break
            
    looped_list = find_looped_route(start_pos, grid)
    
    return len(looped_list) // 2


def part_two(data_input):
    result = 0
    
    grid = [list(row) for row in data_input]

    for row_idx, row in enumerate(grid):
        if "S" in row:
            col_idx = row.index("S")
            start_pos = (int(row_idx), int(col_idx))
            break

    looped = find_looped_route(start_pos, grid)
    result = calc_inner_area(grid, looped)
  
    return result


if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(10, 2023)

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
