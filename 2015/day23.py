"""
Author: IchBinJade
Date  : 2025-01-06
AoC 2015 Day 23 - https://adventofcode.com/2015/day/23

Simulate register-based computations for a 'computer'
"""

import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file


def perform_instructions(instructions, a, b):
    computer = {
        "a": a,
        "b": b
    }
    
    idx = 0
    
    while 0 <= idx < len(instructions):
        line = instructions[idx]
        if len(line.split()) == 3:
            instr, reg, offset = line.replace(",", "").split()
            offset = int(offset)
        else:
            if "jmp" in line:
                instr, offset = line.strip(", ").split()
                offset = int(offset)
            else:
                instr, reg = line.strip(", ").split()
        
        if instr == "hlf":
            computer[reg] //= 2
        elif instr == "tpl":
            computer[reg] *= 3
        elif instr == "inc":
            computer[reg] += 1
        elif instr == "jmp":
            idx += offset - 1
        elif instr == "jie":
            if computer[reg] % 2 == 0:
                idx += offset - 1
        elif instr == "jio":
            if computer[reg] == 1:
                idx += offset - 1
                
        idx += 1
            
    return computer


def part_one(data_input):
    a, b = 0, 0
    updated_computer = perform_instructions(data_input, a, b)
    
    return updated_computer["b"]  


def part_two(data_input):
    a, b = 1, 0
    updated_computer = perform_instructions(data_input, a, b)
    
    return updated_computer["b"] 


if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(23, 2015)

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
