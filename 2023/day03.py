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
GEAR = r"\*"
NEIGHBOURS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

def extract_whole_num(row, char_pos, input):
    orig_pos = char_pos
    number_str = ""
    # Check backwards in case this isn't the start of the number
    while char_pos >= 0 and input[row][char_pos].isdigit():
        number_str = input[row][char_pos] + number_str
        char_pos -= 1

    # Check forwards now backwards is done
    char_pos = orig_pos
    while char_pos + 1 < len(input[row]) and input[row][char_pos + 1].isdigit():
        number_str += input[row][char_pos + 1]
        char_pos += 1

    if number_str:
        return int(number_str)
    
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


def get_gear_list(input):
    gears_pos = []
    for row in range(len(input)):
        for match in re.finditer(GEAR, input[row]):
            col = match.start(0)
            gears_pos.append((row, col))

    return gears_pos


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
                break # don't need to check further once added

    return total


def part_two(input):
    total = 0
    gears_list = get_gear_list(input)
    visited_coords = set()
    
    for gear_row, gear_col in gears_list:
        part_nums = []
        for nx, ny in NEIGHBOURS:
            nrow = gear_row + nx
            ncol = gear_col + ny
            if 0 <= nrow < len(input) and 0 <= ncol < len(input[nrow]):
                if input[nrow][ncol].isdigit() and (nrow, ncol) not in visited_coords:
                    part = extract_whole_num(nrow, ncol, input)
                    if part and part not in part_nums:
                        part_nums.append(part)
                        visited_coords.add((nrow, ncol))
        
        if len(part_nums) == 2:
            gear_ratio = part_nums[0] * part_nums[1]
            total += gear_ratio              
    
    return total



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
