"""
Author: IchBinJade
Date  : 2024-12-26
AoC 2020 Day 2: Password Philosophy - https://adventofcode.com/2020/day/2
"""

import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file

def part_one(data_input):
    total = 0
    for line in data_input:
        policy, password = line.split(": ")
        p_range, letter = policy.split()
        p_lo, p_high = p_range.split("-")
        letter_count = password.count(letter)
        if int(p_lo) <= letter_count <= int(p_high):
            total += 1
    
    return total


def part_two(data_input):
    total = 0
    for line in data_input:
        policy, password = line.split(": ")
        p_range, letter = policy.split()
        p_1, p_2 = p_range.split("-")
        pos_1, pos_2 = int(p_1) - 1, int(p_2) - 1
        if (password[pos_1] == letter) != (password[pos_2] == letter):
            total += 1
    
    return total


if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(2, 2020)

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
