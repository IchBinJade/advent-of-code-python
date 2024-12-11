"""
Author: IchBinJade
Date  : 2024-12-08
AoC 2023 Day 10 - https://adventofcode.com/2023/day/10
"""

import sys
import os
import time
import re

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
            queued_list.appendleft((row - 1, col))
            looped_list.add((row - 1, col))
        # Moving Down
        if row < len(grid) - 1 and character in "S|7F" and grid[row + 1][col] in "|JL" and (row + 1, col) not in looped_list:
            queued_list.appendleft((row + 1, col))
            looped_list.add((row + 1, col))
        # Moving Left
        if col > 0 and character in "S-J7" and grid[row][col - 1] in "-LF" and (row, col -1) not in looped_list:
            queued_list.appendleft((row, col - 1))
            looped_list.add((row, col - 1))
        # Moving Right
        if col < len(grid[row]) and character in "S-LF" and grid[row][col + 1] in "-J7" and (row, col + 1) not in looped_list:
            queued_list.appendleft((row, col + 1))
            looped_list.add((row, col + 1))
            
    return looped_list


def part_one(data_input):
    total = 0
    #print(f"data_input >>> {data_input}")

    # Create a grid from the input
    grid = [list(row) for row in data_input]

    # Identify the start pos
    for row_idx, row in enumerate(grid):
        if "S" in row:
            col_idx = row.index("S")
            start_pos = (int(row_idx), int(col_idx))
            break
            
    #print(f"start_pos >>> {start_pos}")
    # Identify the looping path, utilising visited[]
    looped_list = find_looped_route(start_pos, grid)
    #print(f"looped_list >>> {looped_list}")
    
    #return longest_step
    return len(looped_list) // 2


def part_two(data_input):
    total = 0

    
    return total

TEST_INPUT_1 = ['-L|F7', '7S-7|', 'L|7||', '-L-J|', 'L|-JF'] # First example w/ added pipes (loop is same as #3)

TEST_INPUT_2 = ['7-F7-', '.FJ|7', 'SJLL7', '|F--J', 'LJ.LJ'] # More complex loop

TEST_INPUT_3 = ['.....', '.S-7.', '.|.|.', '.L-J.', '.....'] # First example w/ just the looping pipe

if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(10, 2023)
    
    #input_data = TEST_INPUT_2

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
