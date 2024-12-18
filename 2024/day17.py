"""
Author: IchBinJade
Date  : 2024-12-18
AoC 2024 Day 17 - https://adventofcode.com/2024/day/17
"""

import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file

def combo_parse(operand, A, B, C):
    # Parse operand
        if operand == 4:
            return A
        elif operand == 5:
            return B
        elif operand == 6:
            return C
        else:
            return operand
        

def simulate_program(registers, program):
    A = registers[0]
    B = registers[1]
    C = registers[2]
    output = []
    idx = 0
    
    #for idx in range(0, len(program), 2):
    while idx < len(program):
        #print(f"A, B, C = {A}, {B}, {C}")
        opcode, operand = program[idx], program[idx + 1]
        #print(f"idx = {idx} >>> opcode = {opcode} ; operand = {operand}")
        #print(f"output >>> {output}")
        
        if opcode == 0:  
            A = A >> combo_parse(operand, A, B, C)
        elif opcode == 1:  
            B = B ^ operand
        elif opcode == 2: 
            B = combo_parse(operand, A, B, C) % 8
        elif opcode == 3:  # Jump to operand_val if A != 0
            if A != 0:
                #print(f"Jumping to idx = {operand}")
                idx = operand
                continue
        elif opcode == 4:  
            B = B ^ C
        elif opcode == 5:  # Output operand_val % 8
            output.append(combo_parse(operand, A, B, C) % 8)
        elif opcode == 6:
            B = A >> combo_parse(operand, A, B, C)
        elif opcode == 7:
            C = A >> combo_parse(operand, A, B, C)
        
        idx += 2

    return output


def part_one(data_input):
    # print(data_input)
    blank_idx = data_input.index("")
    raw_reg = [row for row in data_input[:blank_idx]]
    raw_prog = [row for row in data_input[blank_idx + 1:]] 
    
    registers = [int(reg.split(": ")[1]) for reg in raw_reg]
    program = list(map(int, "".join(raw_prog).split(": ")[1].split(",")))
    
    #print(f"registers >>> {registers} ; program >>> {program}")
    output = simulate_program(registers, program)
    
    return ",".join(str(num) for num in output)


def part_two(data_input):
            
    return None    
    

TEST_INPUT_1 = ['Register A: 729', 'Register B: 0', 'Register C: 0', '', 'Program: 0,1,5,4,3,0']

if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(17, 2024)
    
    input_data = TEST_INPUT_1

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
