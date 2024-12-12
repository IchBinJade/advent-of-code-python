"""
Author: IchBinJade
Date  : 2024-12-11
AoC 2024 Day 10 - https://adventofcode.com/2024/day/10
"""

import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file
from collections import deque

def find_trails_with_summits(grid, row, col):
    row_count = len(grid)
    col_count = len(grid[0])
    
    queue = deque([(row, col)])
    visited = {(row, col)}
    trail_score = 0
    
    while queue:
        curr_row, curr_col = queue.popleft()
        # Check neighbours
        for next_row, next_col in [(curr_row - 1, curr_col), (curr_row + 1, curr_col), (curr_row, curr_col - 1), (curr_row, curr_col + 1)]:
            # Bounds check
            if 0 <= next_row < row_count and 0 <= next_col < col_count:
                if grid[next_row][next_col] == grid[curr_row][curr_col] + 1 and (next_row, next_col) not in visited:
                    if grid[next_row][next_col] == 9:
                        trail_score += 1
                        visited.add((next_row, next_col))
                    else:
                        queue.append((next_row, next_col))
    
    return trail_score


def rate_trails(grid, row, col):
    row_count = len(grid)
    col_count = len(grid[0])
    
    queue = deque([(row, col)])
    visited = {(row, col): 1}
    trail_rating = 0
    
    while queue:
        curr_row, curr_col = queue.popleft()
        if grid[curr_row][curr_col] == 9:
            trail_rating += visited[(curr_row, curr_col)]
        # Check neighbours
        for next_row, next_col in [(curr_row - 1, curr_col), (curr_row + 1, curr_col), (curr_row, curr_col - 1), (curr_row, curr_col + 1)]:
            # Bounds check
            if 0 <= next_row < row_count and 0 <= next_col < col_count:
                if grid[next_row][next_col] == grid[curr_row][curr_col] + 1:
                    if (next_row, next_col) in visited:
                        visited[(next_row, next_col)] += visited[(curr_row, curr_col)]
                        continue
                    visited[(next_row, next_col)] = visited[(curr_row, curr_col)]
                    queue.append((next_row, next_col))
    
    return trail_rating


def part_one(data_input):
    grid = [list(int(character) for character in row) for row in data_input]
    
    row_count = len(grid)
    col_count = len(grid[0])
    
    trail_heads = [(row, col) for row in range(row_count) for col in range(col_count) if grid[row][col] == 0]
    
    scores = [find_trails_with_summits(grid, row, col) for row, col in trail_heads]

    return sum(scores)


def part_two(data_input):
    grid = [list(int(character) for character in row) for row in data_input]
    
    row_count = len(grid)
    col_count = len(grid[0])
    
    trail_heads = [(row, col) for row in range(row_count) for col in range(col_count) if grid[row][col] == 0]
    
    ratings = [rate_trails(grid, row, col) for row, col in trail_heads]
    
    return sum(ratings)



if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(10, 2024)

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
