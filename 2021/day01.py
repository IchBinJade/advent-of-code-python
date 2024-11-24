"""
Author: IchBinJade
Date  : 2022-11-XX
AoC 2021 Day 1 - https://adventofcode.com/2021/day/1
"""

import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file

def part_one(input):
    readings = [int(x) for x in input]
    previous = readings[0]
    count = 0
    for reading in readings:
        if reading > previous:
            count += 1
        previous = reading
    return count


def part_two(input):
    readings = [int(x) for x in input]
    previous = sum(readings[0:2])
    count = 0
    for reading in range(1, len(readings) - 2):
        new_reading = sum(readings[reading : reading+3])
        if new_reading > previous:
            count += 1
        previous = new_reading
    return count


if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(1, 2021)

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
