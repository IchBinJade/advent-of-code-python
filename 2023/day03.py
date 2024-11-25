"""
Author: IchBinJade
Date  : 2024-11-24
AoC 2023 Day 3 - https://adventofcode.com/2023/day/3
"""

import sys
import os
import time
import re

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file

DIGITS = r"\d+"
SYMBOLS = r"[^.\d]"
NEIGHBOURS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

def extract_whole_num(row, char_pos, input):
    # Save start pos to get end pos later
    start_pos = char_pos
    number_str = ""
    # Keep shifting along until we stop getting a digit
    while char_pos < len(input[row]) and input[row][char_pos].isdigit():
        number_str += input[row][char_pos]
        char_pos += 1

    if number_str:
        end_pos = char_pos - 1
        return int(number_str), start_pos, end_pos
    
    return None


def get_number_list(input):
    numbers_pos = []
    for row in range(len(input)):
        for match in re.finditer(DIGITS, input[row]):
            start_pos = match.start(0)
            end_pos = match.end(0) - 1
            number = int(match.group(0))
            numbers_pos.append((number, row, start_pos, end_pos))

    return numbers_pos


def is_adjacent_to_symbol(input, num_coord):
    # Check neighbours of current num coord and return boolean
    row, col = num_coord
    for nx, ny in NEIGHBOURS:
        nrow = row + nx
        ncol = col + ny
        if 0 <= nrow < len(input) and 0 <= ncol < len(input[nrow]):
            if re.match(SYMBOLS, input[nrow][ncol]):
                return True
    
    return False


def part_one(input):
    total = 0
    numbers_pos = get_number_list(input)
    for number, row, start_pos, end_pos in numbers_pos:
        for col in range(start_pos, end_pos + 1):
            if is_adjacent_to_symbol(input, (row, col)):
                total += number
                print(f"Added number {number}")
                break # don't need to check further once added

    return total


def part_two(input):
    pass



if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(3, 2023)

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
