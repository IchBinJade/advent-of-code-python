"""
Author: IchBinJade
Date  : 2024-12-31
AoC 2015 Day 4 - https://adventofcode.com/2015/day/4

MD5 Hashing
"""

import sys
import os
import time
import hashlib

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file


def part_one(data_input):
    key = data_input[0]
    
    num = 1
    while True:
        key_str = key + str(num)
        result = hashlib.md5(key_str.encode())
        if result.hexdigest()[:5] == "00000":
            return num
        num += 1


def part_two(data_input):
    key = data_input[0]
    
    num = 1
    while True:
        key_str = key + str(num)
        result = hashlib.md5(key_str.encode())
        if result.hexdigest()[:6] == "000000":
            return num
        num += 1    


if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(4, 2015)

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
