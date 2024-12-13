"""
Author: IchBinJade
Date  : 2024-12-13
AoC 2024 Day 12 - https://adventofcode.com/2024/day/12

Utilises: BFS / Flood Fill

TODO: Start and solve part 2
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


def part_one(data_input):
    grid = [list(character for character in row) for row in data_input]
    row_count = len(grid)
    col_count = len(grid[0])
    #print(f"grid >>> {grid}; Rows = {row_count}; Cols = {col_count}")
    grouped_plants = group_plants(grid)
    #print(f"grouped_plants >>> {grouped_plants}")
    price_list = []
    for plot in grouped_plants:
        price_list.append(get_price(plot))

    return sum(price_list)


def part_two(data_input):
    
    
    return None

TEST_INPUT_1 = ['AAAA', 'BBCD', 'BBCC', 'EEEC']
TEST_INPUT_2 = ['RRRRIICCFF', 'RRRRIICCCF', 'VVRRRCCFFF', 'VVRCCCJFFF', 'VVVVCJJCFE', 'VVIVCCJJEE', 'VVIIICJJEE', 'MIIIIIJJEE', 'MIIISIJEEE', 'MMMISSJEEE']

if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(12, 2024)

    # input_data = TEST_INPUT_2
    
    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
    