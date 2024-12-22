"""
Author: IchBinJade
Date  : 2024-12-22
AoC 2024 Day 22 - https://adventofcode.com/2024/day/22
"""

import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file

def calc_new_secret(num):
    # Multiply by 64 then get bitwise xor of result and prune
    num = (num ^ (num * 64)) % 16777216
    # divide by 32, round down, then get bitwise xor and prune
    num = (num ^ (num // 32)) % 16777216
    # multuple by 2048, get bitwise xor and prune
    num = (num ^ (num * 2048)) % 16777216
    
    return num


def part_one(data_input):
    new_nums = []
    for secret in data_input:
        new_num = int(secret)
        # print(f"new_num = {new_num}")
        for _ in range(2000):
            new_num =  calc_new_secret(new_num)
        new_nums.append(new_num)
    
    # print(f"new_nums = {new_nums}")        
    return sum(new_nums)


def part_two(data_input):
    pass

TEST_INPUT = ['1', '10', '100', '2024']

if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(22, 2024)
    
    # input_data = TEST_INPUT

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
