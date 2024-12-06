"""
Author: IchBinJade
Date  : 2024-12-06
AoC 2024 Day 6 - https://adventofcode.com/2024/day/6

TODO: Complete part 2
"""

import sys
import os
import time
import re

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file

TEST_INPUT = ['....#.....', '.........#', '..........', '..#.......', '.......#..', '..........', '.#..^.....', '........#.', '#.........', '......#...']


def find_route(visited, start_pos, next_row, next_col, grid):
    row_count = len(grid)
    col_count = len(grid[0])
    curr_row, curr_col = start_pos
    while True:
        # Add coords to visited
        visited.add((curr_row, curr_col))
        # Bounds check (is guard gonna leave)
        if curr_row + next_row < 0 or curr_row + next_row >= row_count or curr_col + next_col < 0 or curr_col + next_col >= col_count:
            break
        # Check for obstacle else move
        if grid[curr_row + next_row][curr_col + next_col] == "#":
            next_col, next_row = -next_row, next_col
        else:
            curr_row += next_row
            curr_col += next_col


def part_one(data_input):
    total = 0
    visited = set()
    #print(f"data_input >>> {data_input}")
    grid = [list(row) for row in data_input]
    
    #print(f"grid >>> {grid}")
    
    # Get start position of guard
    start_pos = None
    for row_idx, row in enumerate(grid):
        if "^" in row:
            col_idx = row.index("^")
            start_pos = (row_idx, col_idx)
        
    #print(f"start_pos >>> {start_pos}")

    next_row, next_col = -1, 0
    find_route(visited, start_pos, next_row, next_col, grid)

    # Final answer will be the number of coords in visited?
    total = len(visited)

    return total


def part_two(data_input):
    pass



if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(6, 2024)

    #input_data = TEST_INPUT

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
