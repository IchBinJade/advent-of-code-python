"""
Author: IchBinJade
Date  : 2020-12-XX
AoC Day 1 - https://adventofcode.com/2020/day/1
"""

import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file

def part_one(input):
    int_input = [int(num) for num in input]
    for first_num in int_input:
        for second_num in int_input:
            if first_num + second_num == 2020:
                result = first_num * second_num
                return result

    return None


def part_two(input):
    int_input = [int(num) for num in input]
    for first_num in int_input:
        for second_num in int_input:
            for third_num in int_input:
                if first_num + second_num + third_num == 2020:
                    result = first_num * second_num * third_num
                    return result

    return None



if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(1, 2020)

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
