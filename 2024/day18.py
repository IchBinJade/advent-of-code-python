"""
Author: IchBinJade
Date  : 2024-12-20
AoC 2024 Day 18 - https://adventofcode.com/2024/day/18

Utilises: BFS
Execution time:  ~8s
"""

import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file
from collections import deque

def find_path(grid):
    end_pos = (70, 70)
    rows, cols = len(grid), len(grid[0])
    visited = set((0,0))
    queue = deque([(0, 0, 0)])
    step = 0
    
    while queue:
        curr_row, curr_col, step = queue.popleft()
        if (curr_row, curr_col) == end_pos:
            return step
        for next_row, next_col in [(curr_row + 1, curr_col), (curr_row, curr_col + 1), (curr_row - 1, curr_col), (curr_row, curr_col - 1)]:
            # Bounds check
            if 0 <= next_row < rows and 0 <= next_col < cols:
                if grid[next_row][next_col] != "#" and (next_row, next_col) not in visited:
                    visited.add((next_row, next_col))
                    queue.append((next_row, next_col, step + 1))
    
    return None


def find_trouble_coord(grid):
    end_pos = (70, 70)
    rows, cols = len(grid), len(grid[0])
    
    visited = set((0,0))
    queue = deque([(0, 0)])
    while queue:
        curr_row, curr_col = queue.popleft()
        if (curr_row, curr_col) == end_pos:
            # Exit has been found, move to the next coord
            return True
        for next_row, next_col in [(curr_row + 1, curr_col), (curr_row, curr_col + 1), (curr_row - 1, curr_col), (curr_row, curr_col - 1)]:
            # Bounds check
            if 0 <= next_row < rows and 0 <= next_col < cols:
                if grid[next_row][next_col] != "#" and (next_row, next_col) not in visited:
                    visited.add((next_row, next_col))
                    queue.append((next_row, next_col))
                        
    return False


def part_one(data_input):
    # Create grid and plot coords of first
    grid = [list("." for _ in range(71)) for _ in range(71)]
    coord_list = [tuple(map(int, coord.split(","))) for coord in data_input]
    for x, y in coord_list[:1024]:
        grid[y][x] = "#"

    return find_path(grid)


def part_two(data_input):
    # Create grid and plot coords of first
    grid = [list("." for _ in range(71)) for _ in range(71)]
    coord_list = [tuple(map(int, coord.split(","))) for coord in data_input]
    for x, y in coord_list[:12]:
        grid[y][x] = "#"
    
    # Then go through the remaining coords until the path is blocked
    for next_x, next_y in coord_list[12:]:
        grid[next_y][next_x] = "#"
        if find_trouble_coord(grid) == False:
            return ",".join((str(next_x), str(next_y)))


if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(18, 2024)

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")