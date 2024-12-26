"""
Author: IchBinJade
Date  : YYYY-MM-DD
AoC YYYY Day X - https://adventofcode.com/20YY/day/X
"""

import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file

def part_one(data_input):
    # print(data_input)
    # input_int = int("".join(data_input))
    input_str = "".join(data_input)
    # print(input_int)
    total = 0
    for idx in range(len(input_str)):
        # print(f"idx = {idx} ; len_input = {len(input_str)}")
        if idx == len(input_str) - 1:
            if input_str[idx] == input_str[0]:
                total += int(input_str[idx])    
        elif input_str[idx] == input_str[idx + 1]:
            total += int(input_str[idx])
        
    return total


def part_two(data_input):
    input_str = "".join(data_input)
    # print(input_int)
    total = 0
    length = len(input_str)
    for idx in range(length):
        # print(f"idx = {idx} ; len_input = {len(input_str)}")
        half_idx = (idx + length // 2) % length
        if input_str[idx] == input_str[half_idx]:
            total += int(input_str[idx])
        
    return total

TEST_INPUT_1 = ['1212']
TEST_INPUT_2 = ['123123']

TEST_INPUT_3 = ['1234']
TEST_INPUT_4 = ['91212129']

if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(1, 2017)
    
    # input_data = TEST_INPUT_4

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    # input_data = TEST_INPUT_2
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
