"""
Author: IchBinJade
Date  : 2025-01-02
AoC 2015 Day 20 - https://adventofcode.com/2015/day/20

Calculating elf/house present deliveries with upper limit
"""

import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file


def find_min_house(target):
    upper = target // 10
    presents = [0] * (upper + 1)

    for elf in range(1, upper + 1):
        for house in range(elf, upper + 1, elf):
            presents[house] += elf * 10

    house = 0
    while presents[house] < target:
        house += 1
    
    return house


def part_one(data_input):
    target = int(data_input[0])

    min_house = find_min_house(target)
    
    return min_house


def part_two(data_input):
    target = int(data_input[0])
    
    upper = target // 10
    presents = [0] * (upper + 1)

    for elf in range(1, upper + 1):
        for house in range(elf, min(51 * elf, upper), elf):  # Elf stops after house 50
            presents[house] += elf * 11

    house = 0
    while presents[house] < target:
        house += 1
    
    return house


if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(20, 2015)

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
