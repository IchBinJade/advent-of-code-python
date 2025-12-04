"""
Author: IchBinJade
Date  : 2025-12-04
AoC 2025 Day 4 - https://adventofcode.com/2025/day/4
"""

import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file


def check_neighbours(grid, row, col):
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1),  (1, 0),  (1, 1)]
    count = 0
    
    for dr, dc in directions:
        nr, nc = row + dr, col + dc
        if (0 <= nr < len(grid)) and (0 <= nc < len(grid[0])):
            if grid[nr][nc] == "@":
                count += 1
                if count > 3:
                    return count
                
    return count


def part_one(data_input):
    total = 0
    grid = [list(row) for row in data_input]
    
    for cr in range(len(grid)):
        for cc in range(len(grid[0])):
            if grid[cr][cc] == "@":
                neighbour_count = check_neighbours(grid, cr, cc)
                if neighbour_count < 4:
                    total += 1
    
    return total


def part_two(data_input):
    pass



if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(4, 2025)

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
