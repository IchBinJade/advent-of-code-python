"""
Author: IchBinJade
Date  : 2025-01-13
AoC 2016 Day 15 - https://adventofcode.com/2016/day/15

Simulating a sorta 2p machine with horizontally-sliding discs
"""

import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file


def create_disc_dict(data_input):
    discs = []
    for line in data_input:
        disc_id = line.split()[1].strip("#")
        no_of_pos = int(line.split()[3])
        start_pos = line.split()[-1].strip(".")
        new_disc = {
            "disc_id": int(disc_id),
            "no_of_pos": int(no_of_pos),
            "start_pos": int(start_pos),
            "curr_time": 0,
            "curr_pos": int(start_pos)
        }
        discs.append(new_disc)
    
    return discs


def bad_timing(first_time, discs):
    """FORMULA: Current position = (start_pos + t + disc_id) % no_of_pos"""
    for _, disc in enumerate(discs):
        if (disc["start_pos"] + first_time + disc["disc_id"]) % disc["no_of_pos"] != 0:
            return True
    
    return False


def part_one(data_input):
    discs = create_disc_dict(data_input)
    first_time = 0
    
    while bad_timing(first_time, discs):
        first_time += 1
    
    return first_time


def part_two(data_input):
    discs = create_disc_dict(data_input)
    first_time = 0
    
    p2_disc = {
            "disc_id": len(discs) + 1,
            "no_of_pos": 11,
            "start_pos": 0,
            "curr_time": 0,
            "curr_pos": 0
        }
    
    discs.append(p2_disc)
    
    while bad_timing(first_time, discs):
        first_time += 1
    
    return first_time


if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(15, 2016)

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
