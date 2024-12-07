"""
Author: IchBinJade
Date  : 2024-12-07
AoC 2024 Day 7 - https://adventofcode.com/2024/day/7
"""

import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file

def find_all_expressions(num_list, target, current_result, index, expression, use_concat):
    # Base case: if we've used all numbers
    if index == len(num_list):
        if current_result == target:
            return target
        else:
            return False
    
    next_num = num_list[index]
    
    # Try adding "+""
    if find_all_expressions(num_list, target, current_result + next_num, index + 1, expression + f" + {next_num}", use_concat):
        return target
    
    # Try adding "*""
    if find_all_expressions(num_list, target, current_result * next_num, index + 1, expression + f" * {next_num}", use_concat):
        return target
    
    if use_concat:
        # Try adding concatenation
        if find_all_expressions(num_list, target, int(str(current_result) + str(next_num)), index + 1, expression + f" * {next_num}", use_concat):
            return target
    
    return False

def solve_expression(num_list, target, use_concat):
    initial_expr = str(num_list[0])
    return find_all_expressions(num_list, target, num_list[0], 1, initial_expr, use_concat)


def part_one(data_input):
    count = 0
    for line in data_input:
        #print(f"line >>> {line}")
        desired_result, *nums_to_use = line.split(": ")
        desired_result = int(desired_result)
        nums_list = list(map(int, nums_to_use[0].split()))
        #print(f"desired = {desired_result}; nums_to_use = {nums_list}")
        if solve_expression(nums_list, desired_result, use_concat=False):
            count += solve_expression(nums_list, desired_result, use_concat=False)
    
    return count


def part_two(data_input):
    count = 0
    for line in data_input:
        #print(f"line >>> {line}")
        desired_result, *nums_to_use = line.split(": ")
        desired_result = int(desired_result)
        nums_list = list(map(int, nums_to_use[0].split()))
        #print(f"desired = {desired_result}; nums_to_use = {nums_list}")
        if solve_expression(nums_list, desired_result, use_concat=True):
            count += solve_expression(nums_list, desired_result, use_concat=True)
    
    return count



if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(7, 2024)

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
