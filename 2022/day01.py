"""
Author: IchBinJade
Date  : 2022-12-15
AoC Day 1 - https://adventofcode.com/2022/day/1
"""

import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file

def part_one(input):
    # Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?"""
    max_cal = 0
    tot_cal = 0
    for cals in input:
        if cals != "":
            tot_cal += int(cals)
        elif cals == "":
            if tot_cal > max_cal:
                max_cal = tot_cal
            tot_cal = 0
    
    return max_cal


def part_two(input):
    # Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?
    meal_list = []

    # Break down into meals and append to new list
    meal = 0
    for cals in input:
        if cals == "":
            meal_list.append(meal)
            meal = 0
        else:
            meal += int(cals)
        
    # Find top 3 and return sum
    meal_list.sort(reverse=True)
    meal_sum = sum(meal_list[0:3])

    return meal_sum



if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(1, 2022)

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
