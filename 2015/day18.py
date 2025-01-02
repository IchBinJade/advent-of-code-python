"""
Author: IchBinJade
Date  : 2025-1-02
AoC 2015 Day 18 - https://adventofcode.com/2015/day/18

Manipulating "lights" in a grid (similar to day 6)
"""

import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file

NEIGHBOURS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def perform_light_show(grid, row, col, P2=False):
    """ Rules as per instructions:
    
    Light on? If 2 or 3 neighbours on stay on, else turn off
    Light off? If exactly 3 neighbours on stay off, else turn on
    """

    row_count = len(grid)
    col_count = len(grid[0])
    
    # Define the corners based on the grid size
    corners = [(0, 0), (0, col_count - 1), (row_count - 1, 0), (row_count - 1, col_count - 1)]
    
    if P2:
        # Ensure corners are switched on before processing
        for corner in corners:
            grid[corner[0]][corner[1]] = "#"
    
    neighbours_on_count = 0
    for dx, dy in NEIGHBOURS:
        nr, nc = row + dx, col + dy
        if 0 <= nr < row_count and 0 <= nc < col_count and grid[nr][nc] == "#":
            neighbours_on_count += 1
            
    if P2 and (row, col) in corners:
        return "#"
            
    # Apply the rules
    if grid[row][col] == "#":
        if neighbours_on_count == 2 or neighbours_on_count == 3:
            return "#" # Turned on - keep on
        else:
            return "." # Turned on - turn off
    else:
        if neighbours_on_count == 3:
            return "#" # Turned off - turn on
        else:
            return "." # Turned off - keep off


def part_one(data_input):
    total = 0
    
    # Initial grid configuration
    grid = [list(row) for row in data_input]
    
    # After 100 steps, how many lights are on    
    for _ in range(100):
        updated_grid = [row[:] for row in grid]
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                updated_grid[row][col] = perform_light_show(grid, row, col)
                
        grid = updated_grid
    
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "#":
                total += 1
        
    return total


def part_two(data_input):
    total = 0
    
    # Initial grid configuration
    grid = [list(row) for row in data_input]
    
    # After 100 steps, how many lights are on    
    for step in range(100):
        updated_grid = [row[:] for row in grid]
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                updated_grid[row][col] = perform_light_show(grid, row, col, P2=True)
                
        grid = updated_grid
    
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "#":
                total += 1
        
    return total


if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(18, 2015)

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
