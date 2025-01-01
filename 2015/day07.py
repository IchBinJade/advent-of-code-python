"""
Author: IchBinJade
Date  : 2025-01-01
AoC 2015 Day 7 - https://adventofcode.com/2015/day/7

Bitwise operations on "wire" values
"""

import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file

"""
Possible operators:
AND = &
OR = |
NOT = ~
LSHIFT = <<
RSHIFT = >>
"""

# Lambda dict of bitwise ops when wire isn't a number
OPERATORS = {
    "AND": lambda x, y: x & y,
    "OR": lambda x, y: x | y,
    "NOT": lambda x: ~x,
    "LSHIFT": lambda x, y: x << y,
    "RSHIFT": lambda x, y: x >> y
}

WIRES = {}


def calc_wire(instruction):
    parts = instruction.split()
    
    if len(parts) == 1: # Wire's already an int
        return int(parts[0]) if parts[0].isdigit() else WIRES[parts[0]]
    elif len(parts) == 2: # NOT operation
        return OPERATORS["NOT"](int(parts[1]) if parts[1].isdigit() else WIRES[parts[1]])
    else: # Binary operation
        x, op, y = parts
        x_val = int(x) if x.isdigit() else WIRES[x]
        y_val = int(y) if y.isdigit() else WIRES[y]
        return OPERATORS[op](x_val, y_val)
    

def part_one(data_input):
    while len(WIRES) < len(data_input):
        for line in data_input:
            instr, key = line.split(" -> ")
            if instr.isdigit():
                WIRES[key] = int(instr)
            else:
                if key not in WIRES:
                    try:
                        WIRES[key] = calc_wire(instr)
                    except KeyError:
                        continue # Wire currently missing, try again later
    
    return WIRES["a"]


def part_two(data_input):
    # Reset the wires
    WIRES.clear()
    
    while len(WIRES) < len(data_input):
        for line in data_input:
            instr, key = line.split(" -> ")
            if key == "b":
                instr = "46065" # Set wire b to P1's result
            if instr.isdigit():
                WIRES[key] = int(instr)
            else:
                if key not in WIRES:
                    try:
                        WIRES[key] = calc_wire(instr)
                    except KeyError:
                        continue # Wire currently missing, try again later
    
    return WIRES["a"]


if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(7, 2015)

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
