"""
Author: IchBinJade
Date  : 2024-12-31
AoC 2015 Day 6 - https://adventofcode.com/2015/day/6

Manipulating grid values from regex matched instruction
"""

import sys
import os
import time
import re

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file

RANGE_PATTERN = r"(\d+,\d+)"


def part_one(data_input):
    grid = [[False] * 1000 for _ in range(1000)]

    for instruction in data_input:
        ranges = [tuple(map(int, match.split(','))) for match in re.findall(RANGE_PATTERN, instruction)]
        (x1, y1), (x2, y2) = ranges[0], ranges[1]
        for y in range(y1, y2 + 1):
            for x in range(x1, x2 + 1):
                if instruction.startswith("turn on"):
                    grid[y][x] = True
                elif instruction.startswith("toggle"):
                    grid[y][x] = not grid[y][x]
                elif instruction.startswith("turn off"):
                    grid[y][x] = False
    
    total = 0
    for row in grid:
        for lit in row:
            if lit:
                total += 1
                
    return total


def part_two(data_input):
    grid = [[0] * 1000 for _ in range(1000)]

    for instruction in data_input:
        ranges = [tuple(map(int, match.split(','))) for match in re.findall(RANGE_PATTERN, instruction)]
        (x1, y1), (x2, y2) = ranges[0], ranges[1]
        for y in range(y1, y2 + 1):
            for x in range(x1, x2 + 1):
                if instruction.startswith("turn on"):
                    grid[y][x] = grid[y][x] + 1
                elif instruction.startswith("toggle"):
                    grid[y][x] = grid[y][x] + 2
                elif instruction.startswith("turn off"):
                    if grid[y][x] > 0:
                        grid[y][x] = grid[y][x] - 1
    
    total = 0
    for row in grid:
        for brightness in row:
            total += brightness
                
    return total  


if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(6, 2015)

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
