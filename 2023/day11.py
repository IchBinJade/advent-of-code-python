"""
Author: IchBinJade
Date  : 2024-12-23
AoC 2023 Day 11 - https://adventofcode.com/2023/day/11
"""

import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file
from collections import deque


def get_empty(grid):
    rows = len(grid)
    cols = len(grid[0])
    
    empty_rows = []
    for row in range(rows):
        all_empty = True
        for col in range(cols):
            if grid[row][col] != ".":
                all_empty = False
        empty_rows.append(all_empty)
    
    empty_cols = []
    for col in range(cols):
        all_empty = True
        for row in range(rows):
            if grid[row][col] != ".":
                all_empty = False
        empty_cols.append(all_empty)
    
    return empty_rows, empty_cols


def calculate_distances(coord1, coord2, empty_rows, empty_cols, scale):
    row1, col1 = coord1
    row2, col2 = coord2
    
    # Change the coord values so we're always working with min then max value
    row1, row2 = min(row1, row2), max(row1, row2)
    col1, col2 = min(col1, col2), max(col1, col2)
    
    distance = 0
    for row in range(row1, row2):
        distance += 1
        if empty_rows[row]:
            distance += scale - 1
    for col in range(col1, col2):
        distance += 1
        if empty_cols[col]:
            distance += scale - 1
    
    return distance


def part_one(data_input):
    total = 0

    grid = [list(row) for row in data_input]

    empty_rows, empty_cols = get_empty(grid)
        
    galaxies = [(r, c) for r, row in enumerate(grid) for c, char in enumerate(row) if char == "#"]
        
    # Traverse the galaxy coords and calculate distances
    for row in range(len(galaxies)):
        for col in range(row + 1, len(galaxies)):
            distance = calculate_distances(galaxies[row], galaxies[col], empty_rows, empty_cols, scale=2)
            total += distance
    
    return total


def part_two(data_input):
    total = 0
    
    grid = [list(row) for row in data_input]
   
    empty_rows, empty_cols = get_empty(grid)
   
    galaxies = [(r, c) for r, row in enumerate(grid) for c, char in enumerate(row) if char == "#"]
    
    # Traverse the galaxy coords and calculate distances
    for row in range(len(galaxies)):
        for col in range(row + 1, len(galaxies)):
            distance = calculate_distances(galaxies[row], galaxies[col], empty_rows, empty_cols, scale=1000000)
            total += distance

    return total


if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(11, 2023)

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
