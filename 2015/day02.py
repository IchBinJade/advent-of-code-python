"""
Author: IchBinJade
Date  : 2024-12-31
AoC 2015 Day 2 - https://adventofcode.com/2015/day/2
"""

import sys
import os
import time
import re

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file

LWH_MASK = r"(\d+)x(\d+)x(\d+)"

def part_one(data_input):
    total = 0
    # Result =  2*l*w + 2*w*h + 2*h*l ; extra = l*w
    for entry in data_input:
        dimensions = re.search(LWH_MASK, entry)
        l, w, h = sorted([int(dimensions.group(1)), int(dimensions.group(2)), int(dimensions.group(3))])
        box = (2 * l * w) + (2 * w * h) + (2 * h * l)
        extra = l * w
        total += box + extra
    
    return total


def part_two(data_input):
    total = 0
    # Result =  2*l+ w*2 ; extra = l*w*h
    for entry in data_input:
        dimensions = re.search(LWH_MASK, entry)
        l, w, h = sorted([int(dimensions.group(1)), int(dimensions.group(2)), int(dimensions.group(3))])
        ribbon = 2 * l + w * 2
        extra = l * w * h
        total += ribbon + extra
    
    return total


if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(2, 2015)

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
