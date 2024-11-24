"""
Author: IchBinJade
Date  : 2022-11-XX
AoC 2021 Day 2 - https://adventofcode.com/2021/day/2
"""

import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file

def part_one(input):
    position = 0
    depth = 0
    for i in range(len(input)):
        direction, value = input[i].split(" ")

        match direction:
            case "forward":
                position += int(value)
            case "up":
                depth -= int(value)
            case "down":
                depth += int(value)
            case _:
                continue

    return position * depth


def part_two(input):
    position = 0
    depth = 0
    aim = 0
    for i in range(len(input)):
        direction, value = input[i].split(" ")

        match direction:
            case "forward":
                position += int(value)
                depth += aim * int(value)
            case "up":
                aim -= int(value)
            case "down":
                aim += int(value)
            case _:
                continue

    return position * depth


if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(2, 2021)

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
