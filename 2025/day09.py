"""
Author: IchBinJade
Date  : 2025-12-22
AoC 2025 Day 9 - https://adventofcode.com/2025/day/9
"""

import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file
from itertools import combinations

def part_one(data_input):
    red_coords = [tuple(int(coord) for coord in item.split(",")) for item in data_input]
    max_area = 0
    for point1, point2 in combinations(red_coords, 2):
        width = abs(point1[0] - point2[0]) + 1
        height = abs(point1[1] - point2[1]) + 1
        current_area = width * height
        if current_area > max_area:
            max_area = current_area
    
    return max_area


def part_two(data_input):
    pass



if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(9, 2025)
    

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
