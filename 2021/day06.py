"""
Author: IchBinJade
Date  : 2024-12-27
AoC 2021 Day 6: Lanternfish - https://adventofcode.com/2021/day/6

Utilises: Dynamic programming
"""

import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file

def simulate_lanterfish(fish_times, sim_days):
    # Init fish_count arr where idx 0-8 is timer values
    fish_counts = [0] * 9
    
    # Populate the initial counts from fish_times
    for timer in fish_times:
        fish_counts[timer] += 1
        
    for _ in range(sim_days):
        new_fish = fish_counts[0]
        # Shift all fish_counts down by 1
        for idx in range(8):
            fish_counts[idx] = fish_counts[idx + 1]
        # Fish at 0 reset to 6, new fish get added to 8
        fish_counts[6] += new_fish
        fish_counts[8] = new_fish
    
    return fish_counts


def part_one(data_input):
    input_arr = [int(num) for line in data_input for num in line.split(",")]
    sim_days = 80
    result_arr = simulate_lanterfish(input_arr, sim_days)
   
    return sum(result_arr)


def part_two(data_input):
    input_arr = [int(num) for line in data_input for num in line.split(",")]
    sim_days = 256
    result_arr = simulate_lanterfish(input_arr, sim_days)
   
    return sum(result_arr)


if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(6, 2021)

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
