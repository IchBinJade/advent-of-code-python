"""
Author: IchBinJade
Date  : 2025-01-09
AoC 2016 Day 8 - https://adventofcode.com/2016/day/8

Grid manipulation and printing a 10-char 'display' of ascii capital letters

Future nice-to-have: A function to decipher ascii letters in grid display
"""

import sys
import os
import time
import re

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file

REC_STR = r"rect (\d+)x(\d+)"
ROT_STR = r"rotate \w+ \w=(\d+) by (\d+)"


def do_rectangle(grid, instruction):
    # "rect AxB" = rectangle starting from 0,0 switching on B rows and A cols
    match = re.search(REC_STR, instruction)
    int_a, int_b = int(match.group(1)), int(match.group(2))

    for row in range(int_b):
        for col in range(int_a):
            grid[row][col] = "#"
    
    return grid


def do_rotate_row(grid, instruction):
    # "rotate row y=A by B" = shift pixels in row A right by B pixels; any that drop off appear back at the start of same row
    match = re.search(ROT_STR, instruction)
    row, rotate_int = int(match.group(1)), int(match.group(2))

    length = len(grid[row])
    r = [grid[row][(i - rotate_int) % length] for i in range(length)]
    grid[row] = r
    
    return grid


def do_rotate_col(grid, instruction):
    # "rotate col x=A by B" = shift pixels in col A down by B pixels; any that drop off appear at start of same col
    match = re.search(ROT_STR, instruction)
    col, rotate_int = int(match.group(1)), int(match.group(2))
        
    length = len(grid)
    c = [grid[(i - rotate_int) % length][col] for i in range(length)]
    for idx, b in enumerate(c):
        grid[idx][col] = b
    
    return grid


def part_one(data_input):
    grid = [list("." for _ in range(50)) for _ in range(6)]
    
    for instruction in data_input:
        if instruction.startswith("rect"):
            grid = do_rectangle(grid, instruction)
        elif instruction.startswith("rotate row"):
            grid = do_rotate_row(grid, instruction)
        elif instruction.startswith("rotate column"):
            grid = do_rotate_col(grid, instruction)
    
    lit_pixels = 0
    for r in grid:
        lit_pixels += r.count("#")
    
    return lit_pixels


def part_two(data_input):
    grid = [list("." for _ in range(50)) for _ in range(6)]
    
    for instruction in data_input:
        if instruction.startswith("rect"):
            grid = do_rectangle(grid, instruction)
        elif instruction.startswith("rotate row"):
            grid = do_rotate_row(grid, instruction)
        elif instruction.startswith("rotate column"):
            grid = do_rotate_col(grid, instruction)
    
    return "\n".join("".join(row) for row in grid)


if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(8, 2016)

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = (see ascii letters below)\n{part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
