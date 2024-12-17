"""
Author: IchBinJade
Date  : 2024-12-13
AoC 2024 Day 12 - https://adventofcode.com/2024/day/12

Utilises: BFS / Flood Fill

2024-12-17: Solved part 2 (thanks @hyper-neutrino on YT
            for the explanation about offsets)
"""

import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file
from collections import deque

def group_plants(grid):
    row_count = len(grid)
    col_count = len(grid[0])
    
    plant_plots = []
    visited = set()
    
    for row in range(row_count):
        for col in range(col_count):
            if (row, col) not in visited:
                visited.add((row, col))
                plots = {(row, col)}
                queue = deque([(row, col)])
                while queue:
                    curr_row, curr_col = queue.popleft()
                    # Check neighbours
                    for next_row, next_col in [(curr_row - 1, curr_col), (curr_row + 1, curr_col), (curr_row, curr_col - 1), (curr_row, curr_col + 1)]:
                        # Bounds check
                        if 0 <= next_row < row_count and 0 <= next_col < col_count:
                            if grid[next_row][next_col] == grid[curr_row][curr_col] and (next_row, next_col) not in visited:
                                plots.add((next_row, next_col))
                                visited.add((next_row, next_col))
                                queue.append((next_row, next_col))

                plant_plots.append(plots)         
    
    return plant_plots


def get_price(plot):
    # Calculate the perimeter first and return price (area * perimeter)
    perimeter = 0
    for (row, col) in plot:
        perimeter += 4
        for next_row, next_col in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
            if (next_row, next_col) in plot:
                perimeter -= 1
    
    result = len(plot) * perimeter
                
    return result


def count_corners(plot):
    corner_count = 0
    plot = sorted(plot)
    corners_to_check = set()
    
    # For each cell in the plot, check the 4 "corner" positions slightly offset
    for (row, col) in plot:
        for curr_row, curr_col in [(row - 0.5, col - 0.5), (row + 0.5, col - 0.5), (row + 0.5, col + 0.5), (row - 0.5, col + 0.5)]:
            corners_to_check.add((curr_row, curr_col))
    
    for curr_row, curr_col in corners_to_check:
        # Check the surrounding cells in the grid (offsets by 0.5 in both directions)
        neighbours = [(r, c) in plot for r, c in [(curr_row - 0.5, curr_col - 0.5), (curr_row + 0.5, curr_col - 0.5), (curr_row + 0.5, curr_col + 0.5), (curr_row - 0.5, curr_col + 0.5)]]
        number = sum(neighbours)
        
        # Case 1: If exactly one neighbor exists, it's a corner
        if number == 1:
            corner_count += 1
        
        # Case 2: If exactly two neighbors exist and they form a valid corner (L-shape)
        elif number == 2:
            if neighbours == [True, False, True, False] or neighbours == [False, True, False, True]:
                corner_count += 2
        
        # Case 3: If three neighbors exist, count one corner
        elif number == 3:
            corner_count += 1
    
    # Additional check for single-row/column regions (always has 4 corners)
    rows = {row for row, _ in plot}
    cols = {col for _, col in plot}
    if len(rows) == 1 or len(cols) == 1:
        corner_count = 4
    
    return corner_count


def part_one(data_input):
    grid = [list(character for character in row) for row in data_input]

    grouped_plants = group_plants(grid)

    price_list = []
    for plot in grouped_plants:
        price_list.append(get_price(plot))

    return sum(price_list)


def part_two(data_input):
    grid = [list(character for character in row) for row in data_input]

    grouped_plants = group_plants(grid)
    
    result = 0
    for plot in grouped_plants:
        price = len(plot) * count_corners(plot)
        result += price
    
    return result


if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(12, 2024)
    
    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
    