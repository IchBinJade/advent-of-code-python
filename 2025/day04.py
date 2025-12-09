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
from collections import deque

DIRECTIONS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1),  (1, 0),  (1, 1)]


def check_neighbours(grid, row, col):
    count = 0
    
    for dr, dc in DIRECTIONS:
        nr, nc = row + dr, col + dc
        if (0 <= nr < len(grid)) and (0 <= nc < len(grid[0])):
            if grid[nr][nc] == "@":
                count += 1
                if count > 3:
                    return count
                
    return count


def do_removals(grid, queue):
    removed = 0
    
    while queue:
        cr, cc = queue.popleft()
        removed += 1
        grid[cr][cc] = "."
        
        for dr, dc in DIRECTIONS:
            nr, nc = cr + dr, cc + dc
            if (0 <= nr < len(grid)) and (0 <= nc < len(grid[0])):
                if grid[nr][nc] == "@" and (check_neighbours(grid, nr, nc) < 4):
                    if (nr, nc) not in queue:
                        queue.append((nr, nc))
                        
    return removed


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
    grid = [list(row) for row in data_input]
    queue = deque()
    
    # Initial scan of boxes
    for cr in range(len(grid)):
        for cc in range(len(grid[0])):
            if grid[cr][cc] == "@" and (check_neighbours(grid, cr, cc) < 4):
                queue.append((cr,cc))
    
    total = do_removals(grid, queue)
    
    return total



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
