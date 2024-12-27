"""
Author: IchBinJade
Date  : 2024-12-27
AoC 2016 Day 2 - https://adventofcode.com/2016/day/2

Utilises: "Keypad" grid traversal with invalid neighbours
"""

import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file

KEYPAD = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

NEW_PAD = [
    [None, None, 1, None, None],
    [None, 2, 3, 4, None],
    [5, 6, 7, 8, 9],
    [None, "A", "B", "C", None],
    [None, None, "D", None, None]
]


def process_line(line, start_pos):
    # Start from previous position
    row, col = start_pos            
    for char in line:
        if char == "U" and row > 0:
            row -= 1
        if char == "D" and row < 2:
            row += 1
        if char == "L" and col > 0:
            col -= 1
        if char == "R" and col < 2:
            col += 1
    
    code = KEYPAD[row][col]    
    
    return code, (row, col)


def process_line_with_new_keypad(line, start_pos):
    row, col = start_pos
    directions = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
    for char in line:
        dr, dc = directions[char]
        nr, nc = row + dr, col + dc
        if 0 <= nr < len(NEW_PAD) and 0 <= nc < (len(NEW_PAD[0])) and NEW_PAD[nr][nc] is not None:
            row, col = nr, nc
            
    code = NEW_PAD[row][col]
    
    return code, (row, col)


def part_one(data_input):
    code_arr = []
    start_pos = 1, 1 # Key 5 in KEYPAD
    for line in data_input:
        code, start_pos = process_line(line, start_pos)
        code_arr.append(str(code))
   
    return "".join(code_arr)


def part_two(data_input):
    code_arr = []
    start_pos = 2, 0 # Key 5 in NEW_PAD
    for line in data_input:
        code, start_pos = process_line_with_new_keypad(line, start_pos)
        code_arr.append(str(code))
    
    return "".join(code_arr)


if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(2, 2016)

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
