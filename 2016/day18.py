"""
Author: IchBinJade
Date  : 2025-01-19
AoC 2016 Day 18 - https://adventofcode.com/2016/day/18

Helping Admiral Ackbar logically identify traps in a grid
"""

import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file


def build_grid(first_row, total_rows):
    no_of_cols = len(first_row)
    
    grid = []
    
    for idx in range(total_rows):
        if idx == 0:
            new_row = [char for char in first_row]
        else:
            new_row = ["."] * no_of_cols
        
        grid.append(new_row)
        
    return grid


def its_a_trap(left, centre, right):
    if (left == "^" and centre == "^") and (right != "^"):
        return True
    elif (right == "^" and centre == "^") and (left != "^"):
        return True
    elif (left == "^") and (centre != "^" and right != "^"):
        return True
    elif (right == "^") and (centre != "^" and left != "^"):
        return True
    
    return False


def help_admiral_ackbar(grid):
    # Find the traps and update the grid
    rows = len(grid)
    cols = len(grid[0])
    
    for r, row in enumerate(grid):
        for c, _ in enumerate(row):
            if r == 0:
                continue
            else:
                left = grid[r-1][c-1] if c > 0 else "."
                centre = grid[r-1][c] if 0 <= c < cols else "."
                right = grid[r-1][c+1] if c < cols-1 else "."
                
                if its_a_trap(left, centre, right):
                    grid[r][c] = "^"
                else:
                    grid[r][c] = "."

    
    return grid


def part_one(data_input):
    first_row = data_input[0]
    total_rows = 40
    
    grid = build_grid(first_row, total_rows)
    
    mapped_grid = help_admiral_ackbar(grid)
    
    safe_count = 0
    for _, row in enumerate(mapped_grid):
        for c in row:
            if c == ".": safe_count += 1
    
    return safe_count


def part_two(data_input):
    first_row = data_input[0]
    total_rows = 400000
    
    grid = build_grid(first_row, total_rows)
    
    mapped_grid = help_admiral_ackbar(grid)
    
    safe_count = 0
    for _, row in enumerate(mapped_grid):
        for c in row:
            if c == ".": safe_count += 1
    
    return safe_count


if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(18, 2016)

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
