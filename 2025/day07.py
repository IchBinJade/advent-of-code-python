"""
Author: IchBinJade
Date  : 2025-12-15
AoC 2025 Day 7 - https://adventofcode.com/2025/day/7
"""

import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file
from collections import deque
from functools import cache


def trace_beam(grid):
    splits = 0
    grid_height = len(grid)
    grid_width = len(grid[0])
    start_col = grid[0].index("S")
    queue = deque([(0, start_col)]) 
    visited = set([(0, start_col)]) 

    # Helper function to manage adding new positions to the queue/set
    def add_beam(r, c):
        if 0 <= r < grid_height and 0 <= c < grid_width:
            if (r, c) not in visited:
                visited.add((r, c))
                queue.append((r, c))

    while queue:
        r, c = queue.popleft()
        cell = grid[r][c]
        if cell == "." or cell == "S":
            # If we're not out of bounds, continue down to next row.
            if r < grid_height - 1:
                add_beam(r + 1, c)
        elif cell == "^":
            splits += 1
            nr = r + 1 
            lc, rc = c - 1, c + 1
            # Add Left Beam
            add_beam(nr, lc) 
            # Add Right Beam
            add_beam(nr, rc)
            
    return splits


def find_timelines(grid):
    grid_height = len(grid)
    grid_width = len(grid[0])
    start_col = grid[0].index("S")
    start = (1, start_col)
    
    @cache
    def count_paths(r, c):
        # Out of bounds
        if not (0 <= c < grid_width):
            return 0
        # Reach the bottom
        if r >= grid_height:
            return 1
        cell = grid[r][c]
        # Empty space
        if cell == ".":
            return count_paths(r + 1, c)
        # Splitter
        if cell == "^":
            left = count_paths(r + 1, c - 1)
            right = count_paths(r + 1, c + 1)
            return left + right
        return 0
    
    return count_paths(*start)

def part_one(data_input):
    grid = [list(row) for row in data_input]
    
    total = trace_beam(grid)
        
    return total


def part_two(data_input):
    grid = [list(row) for row in data_input]
    
    total = find_timelines(grid)
    
    return total



if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(7, 2025)

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
