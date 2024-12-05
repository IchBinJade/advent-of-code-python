"""
Author: IchBinJade
Date  : 2024-12-04
AoC 2024 Day 4 - https://adventofcode.com/2024/day/4

Logic inspired by my 2023 Day 3 solution! My thanks also to the following coder whose YouTube
vids and explanations have helped and taught me much so far!:

@hyper-neutrino

"""

import sys
import os
import time
import re

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file

NEIGHBOURS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

def get_char_list(data, finder):
    # Get the coords of the X's
    char_list = []
    for row in range(len(data)):
        for match in re.finditer(finder, data[row]):
            start_pos = match.start(0)
            char_list.append((row, start_pos))
    
    return char_list


def check_for_mas(data, x_coord):
    tally = 0
    # Check neighbours of coord, then check for 'MAS' and return tally
    row, col = x_coord
    for nx, ny in NEIGHBOURS:
        if nx == 0 and ny == 0:
            continue # There's no movement
        if 0 <= row + 3 * nx < len(data) and 0 <= col + 3 * ny < len(data[row]):
            # Check for "MAS" pattern
            if data[row + nx][col + ny] == "M":
                if data[row + nx * 2][col + ny * 2] == "A":
                    if data[row + nx * 3][col + ny * 3] == "S":
                        tally += 1

    return tally


def check_for_cross_mas(data, a_coord):
    row, col = a_coord
    tally = 0

    # Bounds check
    if 0 < row < len(data) - 1 and 0 < col < len(data[row]) - 1:
        # Get the values from the four corners
        top_left = data[row - 1][col - 1]
        top_right = data[row - 1][col + 1]
        bottom_left = data[row + 1][col - 1]
        bottom_right = data[row + 1][col + 1]
            
        # Check the pattern in both diagonals:
        # Combo: M > A > S (top-left M, bottom-right S, top-right S, bottom-left M)
        if top_left == 'M' and bottom_right == 'S' and top_right == 'S' and bottom_left == 'M':
            tally += 1
        # Combo: S > A > M (top-left S, bottom-right M, top-right M, bottom-left S)
        elif top_left == 'S' and bottom_right == 'M' and top_right == 'M' and bottom_left == 'S':
            tally += 1
        # Combo: M > S, M > S (top-left M, bottom-left S, top-right M, bottom-right S)
        elif top_left == 'M' and bottom_left == 'S' and top_right == 'M' and bottom_right == 'S':
            tally += 1
        # Combo: S > M, S > M (top-left S, bottom-left M, top-right S, bottom-right M)
        elif top_left == 'S' and bottom_left == 'M' and top_right == 'S' and bottom_right == 'M':
            tally += 1

    return tally


def part_one(data_input):
    total = 0
    x_list = get_char_list(data_input, "X")
    for row, pos in x_list:
        total += check_for_mas(data_input, (row, pos))

    return total


def part_two(data_input):
    total = 0
    a_list = get_char_list(data_input, "A")
    for row, pos in a_list:
        total += check_for_cross_mas(data_input, (row, pos))
        
    return total


if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(4, 2024)

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
