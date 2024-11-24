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

SYMBOLS = r"[^.\d]"
NEIGHBOURS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

def extract_whole_num(row, char_pos, input):
    number_str = ""
    # Keep shifting along until we stop getting a digit
    while char_pos < len(input[row]) and input[row][char_pos].isdigit():
        number_str += input[row][char_pos]
        char_pos += 1

    if number_str:
        return int(number_str)
    
    return None


def get_number_list(input):
    numbers_pos = []
    for row in range(len(input)):
        for char_pos in range(len(input[row])):
            if input[row][char_pos].isdigit():
                number = extract_whole_num(row, char_pos, input)
                if number is not None:
                    numbers_pos.append((number, row, char_pos))

    return numbers_pos


def part_one(input):
    total = 0
    numbers_pos = get_number_list(input)
    print(f"numbers_pos >>> {numbers_pos}")
    # Check for symbols adjacent to each number
    for number, row, char_pos in numbers_pos:
        for x, y in NEIGHBOURS:
                    nb_row, nb_col = row + x, char_pos + y
                    # Check neighbour within bounds
                    if 0 <= nb_row < len(input) and 0 <= nb_col < len(input[row]):
                        if re.match(SYMBOLS, input[row][char_pos]):
                            total += number
                            break # No need to check other neighbours, already counted

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
