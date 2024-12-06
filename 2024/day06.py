"""
Author: IchBinJade
Date  : 2024-12-06
AoC 2024 Day 6 - https://adventofcode.com/2024/day/6
"""

import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file

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


def find_looped_route(start_pos, next_row, next_col, grid):
    row_count = len(grid)
    col_count = len(grid[0])
    curr_row, curr_col = start_pos
    visited = set()

    while True:
        # Add coords to visited
        visited.add((curr_row, curr_col, next_row, next_col))
        # Bounds check (is guard gonna leave)
        if curr_row + next_row < 0 or curr_row + next_row >= row_count or curr_col + next_col < 0 or curr_col + next_col >= col_count:
            break
        # Check for obstacle else move
        if grid[curr_row + next_row][curr_col + next_col] == "#":
            next_col, next_row = -next_row, next_col
        else:
            curr_row += next_row
            curr_col += next_col
        # Check if looped
        if (curr_row, curr_col, next_row, next_col) in visited:
            return True


def get_empty_steps(grid):
    empty_steps = []
    for row_idx, row in enumerate(grid):
        for col_idx, step in enumerate(row):
            if step == ".":
                empty_steps.append((row_idx, col_idx))

    return empty_steps


def part_one(data_input):
    total = 0
    visited = set()
    grid = [list(row) for row in data_input]
    
    # Get start position of guard
    start_pos = None
    for row_idx, row in enumerate(grid):
        if "^" in row:
            col_idx = row.index("^")
            start_pos = (row_idx, col_idx)

    next_row, next_col = -1, 0
    find_route(visited, start_pos, next_row, next_col, grid)

    total = len(visited)

    return total


def part_two(data_input):
    total = 0
    visited = set()
    loopers = set()
    grid = [list(row) for row in data_input]
    
    # Get start position of guard
    start_pos = None
    for row_idx, row in enumerate(grid):
        if "^" in row:
            col_idx = row.index("^")
            start_pos = (row_idx, col_idx)
        
    next_row, next_col = -1, 0

    # Loop the rows and columns, adding an obstacle and check for looped route
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] != ".":
                continue
            grid[row][col] = "#"
            if find_looped_route(start_pos, next_row, next_col, grid):
                total += 1
            grid[row][col] = "."

    return total



if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(6, 2024)

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
