"""
Author: IchBinJade
Date  : 2024-12-31
AoC 2015 Day 3 - https://adventofcode.com/2015/day/3
"""

import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file


def part_one(data_input):
    cr, cc = 0, 0
    visited = set([(cr, cc)])
    
    for char in data_input[0]:
        dr = 1 if char == ">" else -1 if char == "<" else 0
        dc = 1 if char == "^" else -1 if char == "v" else 0
        nr, nc = cr + dr, cc + dc
        visited.add((nr, nc))
        cr, cc = nr, nc
    
    return len(visited)


def part_two(data_input):
    santa_cr, santa_cc = 0, 0
    robo_cr, robo_cc = 0, 0
    visited = set([(0, 0)])
    
    for idx, char in enumerate(data_input[0]):
        dr = 1 if char == ">" else -1 if char == "<" else 0
        dc = 1 if char == "^" else -1 if char == "v" else 0
        if idx % 2 == 0:
            # Move santa
            nr, nc = santa_cr + dr, santa_cc + dc
            visited.add((nr, nc))
            santa_cr, santa_cc = nr, nc
        else:
            # Move robo santa
            nr, nc = robo_cr + dr, robo_cc + dc
            visited.add((nr, nc))
            robo_cr, robo_cc = nr, nc
    
    return len(visited)


if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(3, 2015)

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
