"""
Author: IchBinJade
Date  : 2024-12-29
AoC 2019 Day 2 - https://adventofcode.com/2019/day/2

Intcode program
"""

import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file


def perform_intcode(input_list):
    idx = 0
    new_num = 0
    while idx < len(input_list):
        block = input_list[idx: idx + 4]
        assert len(block) == 4
        op, a, b, new_pos = block
        if op == 99:
            break
        if op == 1:
            new_num = input_list[a] + input_list[b]
        if op == 2:
            new_num = input_list[a] * input_list[b]
            
        input_list[new_pos] = new_num
        idx += 4
        
    return input_list


def process_array(data_arr):
    arr = data_arr[:]
    for idx in range(0, len(arr), 4):
        op = arr[idx]
        a = arr[arr[idx + 1]]
        b = arr[arr[idx + 2]]
        if op == 99:
            return arr[0]
        elif op == 1:
            arr[arr[idx + 3]] = a + b
        elif op == 2:
            arr[arr[idx + 3]] = a * b
            
    return arr[0]


def part_one(data_input):
    input_list = list(int(char) for char in data_input[0].split(","))
    
    # As per instruc, replace 1st with 12 and 2 with 2
    input_list[1] = 12
    input_list[2] = 2
    
    intcode_list = perform_intcode(input_list)
    
    return intcode_list[0]


def part_two(data_input):
    data_arr = list(int(char) for char in data_input[0].split(","))
    
    data_arr[1] = 12
    data_arr[2] = 2
    
    for noun in range(100):
        for verb in range(100):
            data_arr[1] = noun
            data_arr[2] = verb
            output = process_array(data_arr)
            
            if output == 19690720:
                result = 100 * noun + verb
                break
    
    return result


if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(2, 2019)

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
