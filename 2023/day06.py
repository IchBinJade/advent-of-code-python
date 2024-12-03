"""
Author: IchBinJade
Date  : 2024-12-01
AoC 2023 Day 6 - https://adventofcode.com/2023/day/6
"""

import sys
import os
import time
import re
import math

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file

DIGITS = r"\d+"

def calculate_distance(race_time, record_distance):
    """
    Calculate distances using below formula (not quite a typical physics equation):

    Distance = Speed * (Race Time - Held Time)

    where Speed is the same as the Held Time.
    """
    beaten_count = 0
    for held_time in range(1, race_time + 1):
        distance = held_time * (race_time - held_time)
        if distance > record_distance:
            beaten_count += 1
    
    return beaten_count


def part_one(data_input):
    total = 0
    times_list = [int(match.group(0)) for match in re.finditer(DIGITS, data_input[0])]
    record_dist_list = [int(match.group(0)) for match in re.finditer(DIGITS, data_input[1])]
    race_details = [(time, record) for time, record in zip(times_list, record_dist_list)]
    
    beat_records = [calculate_distance(time, record) for time, record in race_details]
    total = math.prod(beat_records)

    return total


def part_two(data_input):
    # Easier to just remove non-numerics from lines to get values
    timing = int(re.sub(f"\D", "", data_input[0]))
    record_dist = int(re.sub(f"\D", "", data_input[1]))

    beat_record = calculate_distance(timing, record_dist)

    return beat_record



if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(6, 2023)

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
