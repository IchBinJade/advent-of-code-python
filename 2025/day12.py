"""
Author: IchBinJade
Date  : 2026-01-09
AoC 2025 Day 12 - https://adventofcode.com/2025/day/12

Thanks again HyperNeutrino!
"""

import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file


def parse_input(data_input):
    regions = []
    
    for line in input_data:
        if not line: # Skip the empty strings
            continue
            
        if 'x' in line:
            w_h, counts_str = line.split(':')
            w, h = map(int, w_h.split('x'))
            counts = [int(x) for x in counts_str.strip().split()]
            regions.append({'w': w, 'h': h, 'counts': counts})
    
    return regions


def part_one(data_input):
    regions = parse_input(data_input)
    total = 0
    for region in regions:
        slots_w = region["w"] // 3
        slots_h = region["h"] // 3
        total_slots = slots_w * slots_h
        total_presents = sum(region["counts"])
        if total_slots >= total_presents:
            total += 1
            
    return total


def part_two(data_input):
    return "Congrats! You've completed 2025!"



if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(12, 2025)

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
