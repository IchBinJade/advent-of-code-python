"""
Author: IchBinJade
Date  : 2025-01-13
AoC 2016 Day 16 - https://adventofcode.com/2016/day/16

Performing a checksum with a modified dragon curve
"""

import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file


def generate_modified_dragon_curve(initial_str, disk_length):
    a = initial_str
    while len(a) < disk_length:
        b = []
        new_str = a[::-1]
        for char in new_str:
            if char == "0":
                b.append("1")
            elif char == "1":
                b.append("0")
                
        a = a + "0" + "".join(b)
    
    return a[:disk_length]


def perform_checksum(raw_str):
    checksum = list(raw_str)
    while len(checksum) % 2 == 0:
        checksum = [
            "1" if checksum[i] == checksum[i + 1] else "0" 
            for i in range(0, len(checksum) - 1, 2)
        ]
    
    return "".join(checksum)


def part_one(data_input):
    initial_str = "".join([str(x) for x in data_input[0]])
    raw_str = generate_modified_dragon_curve(initial_str, 272)
    checksum = perform_checksum(raw_str)
    
    return checksum


def part_two(data_input):
    initial_str = "".join([str(x) for x in data_input[0]])
    raw_str = generate_modified_dragon_curve(initial_str, 35651584)
    checksum = perform_checksum(raw_str)
    
    return checksum


if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(16, 2016)

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
