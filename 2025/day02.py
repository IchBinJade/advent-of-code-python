"""
Author: IchBinJade
Date  : 2025-12-02
AoC 2025 Day 2 - https://adventofcode.com/2025/day/2
"""

import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file


def convert_string(data_input):
    """
    Convert input string into an array of integer tuples
    """
    input_arr_str = data_input[0].split(",")
    tuple_arr = [tuple(map(int, inp_range.split("-"))) for inp_range in input_arr_str]
    return tuple_arr


def is_id_invalid(num):
    """
    Split number in half then compare if the two sides are equal
    """
    num_str = str(num)
    midpoint = len(num_str) // 2
    half_a, half_b = num_str[:midpoint], num_str[midpoint:]
    
    return half_a == half_b


def p2_is_id_valid(num):
    """
    Using modulo, identify sequence combos and then check for
    the sequence(s) repeating at least once more
    """
    num_str = str(num)
    
    if len(num_str) < 2:
        return False
    
    max_seq_len = len(num_str) // 2
    for seq_len in range(1, max_seq_len + 1):
        if len(num_str) % seq_len == 0:
           possible_seq = num_str[:seq_len]
           exp_repeat = len(num_str) // seq_len
           test_str = possible_seq * exp_repeat
           if test_str == num_str:
               return True
           
    return False 
    

def part_one(data_input):
    tuple_arr = convert_string(data_input)
    total = 0
    for range_pair in tuple_arr:
        start, end = range_pair[0], range_pair[1]
        for num in range(start, end + 1):
            if is_id_invalid(num):
                total += num
                
    return total


def part_two(data_input):
    tuple_arr = convert_string(data_input)
    total = 0
    for range_pair in tuple_arr:
        start, end = range_pair[0], range_pair[1]
        for num in range(start, end + 1):
            if p2_is_id_valid(num):
                total += num
                
    return total



if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(2, 2025)

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
