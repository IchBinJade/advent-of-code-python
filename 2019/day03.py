"""
Author: IchBinJade
Date  : 2024-12-30
AoC 2019 Day 3 - https://adventofcode.com/2019/day/3

Intersections of wires on a dynamic grid
"""

import sys
import os
import time
import re

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file

MASK = r"([A-Za-z])(\d+)"

def find_intersection(wire_1, wire_2, P2=False):
    if not P2:
        visited_1 = set([])
        visited_2 = set([])
    else:
        visited_1 = {}
        visited_2 = {}
    cr, cc = 0, 0
    
    # Move Wire 1
    step_count = 0
    for idx in range(len(wire_1)):
        direction, steps = wire_1[idx]
        dx = 1 if direction == "R" else -1 if direction == "L" else 0
        dy = 1 if direction == "U" else -1 if direction == "D" else 0
        for _ in range(steps):
            cr, cc = cr + dx, cc + dy
            step_count += 1
            if not P2:
                visited_1.add((cr, cc))
            else:
                if (cr, cc) not in visited_1:
                    visited_1[(cr, cc)] = step_count
    
    # Move wire 2
    cr, cc = 0, 0
    step_count = 0
    for idx in range(len(wire_2)):   
        direction, steps = wire_2[idx]
        dx = 1 if direction == "R" else -1 if direction == "L" else 0
        dy = 1 if direction == "U" else -1 if direction == "D" else 0
        for _ in range(steps):
            cr, cc = cr + dx, cc + dy
            step_count += 1
            if not P2:
                visited_2.add((cr, cc))
            else:
                if (cr, cc) not in visited_2:
                    visited_2[(cr, cc)] = step_count
    
    if not P2:
        intersect_coords = visited_1.intersection(visited_2)
        min_distance = float("inf")
        for coord in intersect_coords:
            distance = abs(coord[0]) + abs(coord[1])
            if distance < min_distance and coord != (0, 0):
                min_distance = distance
    
        return min_distance
    else:
        intersect_coords = visited_1.keys() & visited_2.keys()
        min_steps = float("inf")
        for coord in intersect_coords:
            total_steps = visited_1[coord] + visited_2[coord]
            if total_steps < min_steps:
                min_steps = total_steps
                
        return min_steps


def part_one(data_input):
    wire_1 = [(match[0], int(match[1])) for match in re.findall(MASK, data_input[0])]
    wire_2 = [(match[0], int(match[1])) for match in re.findall(MASK, data_input[1])]

    min_distance = find_intersection(wire_1, wire_2)

    return min_distance


def part_two(data_input):
    wire_1 = [(match[0], int(match[1])) for match in re.findall(MASK, data_input[0])]
    wire_2 = [(match[0], int(match[1])) for match in re.findall(MASK, data_input[1])]

    min_steps = find_intersection(wire_1, wire_2, True)

    return min_steps


if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(3, 2019)

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
