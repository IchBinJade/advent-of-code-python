"""
Author: IchBinJade
Date  : 2025-01-02
AoC 2015 Day 17 - https://adventofcode.com/2015/day/17

"How many containers to fill X litres" using itertools.combinations()
"""

import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file
from itertools import combinations


def find_combinations(containers, storage):
    num_containers = len(containers)
    total = 0
    
    for idx in range(1, num_containers + 1):
        total += len([combo for combo in combinations(containers, idx) if sum(combo) == storage])
                
    return total


def part_one(data_input):
    # How many combos of containers can fit 150 liters
    containers = []
    for line in data_input:
        val = int(line)
        containers.append(val)
    
    total_combos = find_combinations(containers, 150)
    
    return total_combos


def part_two(data_input):
    # What's the number of ways to fill min number of containers
    containers = []
    for line in data_input:
        val = int(line)
        containers.append(val)
    
    total = 0
    num_containers = len(containers)
    for idx in range(1, num_containers + 1):
        total += len([combo for combo in combinations(containers, idx) if sum(combo) == 150])
        if total:
            break
    
    return total


if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(17, 2015)

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
