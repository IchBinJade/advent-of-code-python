"""
Author: IchBinJade
Date  : 2024-12-08
AoC 2023 Day 9 - https://adventofcode.com/2023/day/9

Learned about the pairwise function in 3.10+ which really
made life easier for part 1!
"""

import sys
import os
import time
import re

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file
from itertools import pairwise

def get_historic_value(num_list, calc_prev):
    """
    Recursive helper function to calculate the difference between the numbers
    until all 0's are reached. Then use the diff to return the next historic value
    
    Args:
        num_list (list[int]): List of integers from each input line
        calc_prev (boolean): Flag to determine if the previous value should be calculated

    Returns:
        int: Calculated next historic value after differences have been calculated
             recursively
    """
   
    # Base case
    if all(num == 0 for num in num_list):
        return 0
    
    # Generate difference through helper
    difference_list = [next_val - prev_val for prev_val, next_val in pairwise(num_list)]
    difference = get_historic_value(difference_list, calc_prev)
    
    if not calc_prev:
        historic_value = num_list[-1] + difference
    else:
        historic_value = num_list[0] - difference
    
    return historic_value


def part_one(data_input):
    total = 0
    for line in data_input:
        num_list = list(map(int,line.split()))
        historic_val = get_historic_value(num_list, calc_prev=False)
        total += historic_val
    
    return total


def part_two(data_input):
    total = 0
    for line in data_input:
        num_list = list(map(int, line.split()))
        historic_val = get_historic_value(num_list, calc_prev=True)
        total += historic_val
    
    return total



if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(9, 2023)

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
