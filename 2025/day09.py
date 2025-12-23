"""
Author: IchBinJade
Date  : 2025-12-22
AoC 2025 Day 9 - https://adventofcode.com/2025/day/9

Mega thanks to @HyperNeutrino on YT for explaining
part 2 and breaking down each component!

TODO: Optimise part 2 solution with coord compression
"""

import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file
from itertools import combinations
from collections import defaultdict


def trace_outline(reds):
    valid_tiles = set()
    for i in range(len(reds)):
        point1, point2 = reds[i], reds[(i + 1) % len(reds)]
        if point1[0] == point2[0]:
            y_start, y_end = min(point1[1], point2[1]), max(point1[1], point2[1])
            for y in range(y_start, y_end + 1):
                valid_tiles.add((point1[0], y))
        elif point1[1] == point2[1]:
            x_start, x_end = min(point1[0], point2[0]), max(point1[0], point2[0])
            for x in range(x_start, x_end + 1):
                valid_tiles.add((x, point1[1]))
    
    return valid_tiles


def find_max_area(reds, outline_tiles):
    # 1. Group outline by row to find min/max X per row
    row_bounds = {}
    rows = defaultdict(list)
    for x, y in outline_tiles:
        rows[y].append(x)
    
    for y, x_list in rows.items():
        row_bounds[y] = (min(x_list), max(x_list))

    max_area = 0
    # 2. Check pairs
    for p1, p2 in combinations(reds, 2):
        x1, x2 = sorted([p1[0], p2[0]])
        y1, y2 = sorted([p1[1], p2[1]])
        
        is_valid = True
        # Check every row in the rectangle
        for y in range(y1, y2 + 1):
            if y not in row_bounds:
                is_valid = False
                break
            
            row_min, row_max = row_bounds[y]
            # Does our rectangle fit inside the row's boundaries?
            if x1 < row_min or x2 > row_max:
                is_valid = False
                break
        
        if is_valid:
            area = (x2 - x1 + 1) * (y2 - y1 + 1)
            if area > max_area:
                max_area = area
                
    return max_area


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
    red_coords = [tuple(int(coord) for coord in item.split(",")) for item in data_input]
    valid_tiles = trace_outline(red_coords)
    max_area = find_max_area(red_coords, valid_tiles)
    
    return max_area



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
