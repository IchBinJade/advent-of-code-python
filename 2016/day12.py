"""
Author: IchBinJade
Date  : 2025-01-12
AoC 2016 Day 12 - https://adventofcode.com/2016/day/12

Simulate register-based computations for a 'computer'.
"""

import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file


def perform_instructions(instructions, P2=False):
    if P2:
        register = {"a": 0, "b": 0, "c": 1, "d": 0}
    else:
        register = {"a": 0, "b": 0, "c": 0, "d": 0}
    
    idx = 0
    
    while 0 <= idx < len(instructions):
        instruction = instructions[idx]
        if instruction.startswith("cpy"):
            _, val_or_reg, reg = instruction.split()
            if val_or_reg.isdigit():
                value = int(val_or_reg)
            else:
                value = register[val_or_reg]
            register[reg] = int(value)
        elif instruction.startswith("inc"):
            _, reg = instruction.split()
            register[reg] =  register[reg] + 1
        elif instruction.startswith("dec"):
            _, reg = instruction.split()
            register[reg] = register[reg] - 1
        elif instruction.startswith("jnz"):
            _, val_or_reg, jump_to = instruction.split()
            if val_or_reg.isdigit():
                value = int(val_or_reg)
            else:
                value = register[val_or_reg]
            if value != 0: 
                idx += int(jump_to)
                continue
            
        idx += 1
    
    return register


def part_one(data_input):
    register = perform_instructions(data_input)
    return register["a"]


def part_two(data_input):
    register = perform_instructions(data_input, P2=True)
    return register["a"]


if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(12, 2016)

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
