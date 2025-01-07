"""
Author: IchBinJade
Date  : 2025-01-07
AoC 2015 Day 24 - https://adventofcode.com/2015/day/24

Partition problem; brute force searching combinations of packages that meet target weight
"""

import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file
from itertools import combinations
from functools import reduce
from operator import mul


def find_ideal_qe(packages, total_weight, groups=3):
    target_weight = total_weight // groups
    
    combo_list = []
    for length in range(0, len(packages) + 1):
        for combo in combinations(packages, length):
            if sum(combo) == target_weight:
                combo_list.append(combo)
        if combo_list:
            break
        
    ideal_qe = float("inf")
    for combo in combo_list:
        qe = reduce(mul, combo)
        if qe < ideal_qe:
            ideal_qe = qe
    
    return ideal_qe


def part_one(data_input):
    packages = [int(x) for x in data_input]

    total_weight = sum(packages)

    ideal_qe = find_ideal_qe(packages, total_weight)

    return ideal_qe


def part_two(data_input):
    packages = [int(x) for x in data_input]

    total_weight = sum(packages)

    ideal_qe = find_ideal_qe(packages, total_weight, groups=4)

    return ideal_qe


if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(24, 2015)

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
