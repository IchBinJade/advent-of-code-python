"""
Author: IchBinJade
Date  : 2023-02-04
AoC Day 4 - https://adventofcode.com/2022/day/4
"""

import sys
import os
import time
import string

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file

def is_range_a_in_range_b(first, second):
    first_a, first_b = map(int, first.split("-"))
    second_a, second_b = map(int, second.split("-"))
    if second_a <= first_a and first_b <= second_b:
        return True
    

def part_one(input):
    # In how many assignment pairs does one range fully contain the other?
    contained_count = 0
    for pairs in input:
        first_elf, second_elf = pairs.split(",")
        if is_range_a_in_range_b(first_elf, second_elf) or is_range_a_in_range_b(second_elf, first_elf):
            contained_count += 1

    return contained_count


def part_two(input):
    pass



if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(4, 2022)

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")