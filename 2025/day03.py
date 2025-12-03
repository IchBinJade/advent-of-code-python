"""
Author: IchBinJade
Date  : 2025-12-03
AoC 2025 Day 3 - https://adventofcode.com/2025/day/3
"""

import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file


def find_largest_two_digit_num(bank):
    """
    Use 2-pointer algorithm to find the largest
    two digit number
    """
    largest_num = 0
    for i in range(len(bank)):
        for j in range(i + 1, len(bank)):
            check_num = int(str(bank[i]) + str(bank[j]))
            if check_num > largest_num:
                largest_num = check_num
    
    return largest_num


def find_largest_twelve_digit_num(bank):
    """
    Stack-based greedy logic to remove unnecessary
    digits to find the largest 12-digit
    """
    target_length = 12
    to_remove = len(bank) - target_length
    result = []
    
    for current_digit in bank:
        while (result and to_remove > 0 and result[-1] < current_digit):
            result.pop()
            to_remove -= 1
        result.append(current_digit)
        
    largest_num_str = result[:target_length]
    largest_num = int("".join(str(n) for n in largest_num_str))
    
    return largest_num


def part_one(data_input):
    total_joltage = 0
    for bank_str in data_input:
        bank_arr = [int(n) for n in bank_str]
        bank_joltage = find_largest_two_digit_num(bank_arr)
        total_joltage += bank_joltage
    
    return total_joltage


def part_two(data_input):
    total_joltage = 0
    for bank_str in data_input:
        bank_arr = [int(n) for n in bank_str]
        bank_joltage = find_largest_twelve_digit_num(bank_arr)
        total_joltage += bank_joltage
        
    return total_joltage



if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(3, 2025)

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
