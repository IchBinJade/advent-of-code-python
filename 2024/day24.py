"""
Author: IchBinJade
Date  : 2024-12-24
AoC 2024 Day 24 - https://adventofcode.com/2024/day/24

Utilises: Recursion and logical operators

2024-12-26: Solved part 2
"""

import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file

WIRES_DICT = {}
CALCS_DICT = {}

def calculate_wires(wire):
    if wire in WIRES_DICT:
        return WIRES_DICT[wire]
    
    # First check if the wires are actually keys to other wires
    operator, wire_1, wire_2 = CALCS_DICT[wire]
    
    # Calculate wire_1 and wire_2, recursively. 
    wire_1_value = calculate_wires(wire_1)
    wire_2_value = calculate_wires(wire_2)
    
    # Apply logical operator
    if operator == "AND":
        WIRES_DICT[wire] = wire_1_value & wire_2_value
    if operator == "OR":
        WIRES_DICT[wire] = wire_1_value | wire_2_value
    if operator == "XOR":
        WIRES_DICT[wire] = wire_1_value ^ wire_2_value

    return WIRES_DICT[wire]


def find_swaps():
    # Initialize the variables for the operations
    highest_z = "z00"
    operations = []

    for result_key, (operator, wire_1, wire_2) in CALCS_DICT.items():
        if result_key[0] == "z" and int(result_key[1:]) > int(highest_z[1:]):
            highest_z = result_key
        operations.append((wire_1, operator, wire_2, result_key))

    wrong = set()

    # Process the operations as per the conditions
    for wire_1, operator, wire_2, result_key in operations:
        if result_key[0] == "z" and operator != "XOR" and result_key != highest_z:
            wrong.add(result_key)
        if (
            operator == "XOR"
            and result_key[0] not in ["x", "y", "z"]
            and wire_1[0] not in ["x", "y", "z"]
            and wire_2[0] not in ["x", "y", "z"]
        ):
            wrong.add(result_key)
        if operator == "AND" and "x00" not in [wire_1, wire_2]:
            for sub_wire_1, sub_operator, sub_wire_2, sub_result_key in operations:
                if (result_key == sub_wire_1 or result_key == sub_wire_2) and sub_operator != "OR":
                    wrong.add(result_key)
        if operator == "XOR":
            for sub_wire_1, sub_operator, sub_wire_2, sub_result_key in operations:
                if (result_key == sub_wire_1 or result_key == sub_wire_2) and sub_operator == "OR":
                    wrong.add(result_key)
                    
    return wrong


def part_one(data_input):
    global WIRES_DICT, CALCS_DICT
    
    for line in data_input:
        if line == "":
            break # We've got the first part
        wire, value = line.split(": ")
        WIRES_DICT[wire] = int(value)
    
    empty_idx = data_input.index("")    
    for line in data_input[empty_idx + 1:]:
        wire_1, operator, wire_2, result_key = line.replace("->", "").split()
        CALCS_DICT[result_key] = tuple((operator, wire_1, wire_2))
    
    binary_list = []
    idx = 0
    while True:
        wire_key = f"z{idx:02}"
        if wire_key not in CALCS_DICT:
            break
        binary_list.append(calculate_wires(wire_key))
        idx += 1

    binary_num = "".join(map(str, binary_list[::-1]))
    
    return int(binary_num, 2)


def part_two(data_input):
    global WIRES_DICT, CALCS_DICT
    
    for line in data_input:
        if line == "":
            break # We've got the first part
        wire, value = line.split(": ")
        WIRES_DICT[wire] = int(value)
    
    empty_idx = data_input.index("")    
    for line in data_input[empty_idx + 1:]:
        wire_1, operator, wire_2, result_key = line.replace("->", "").split()
        CALCS_DICT[result_key] = tuple((operator, wire_1, wire_2))
    
    wrong = find_swaps()
                    
    return ",".join(sorted(wrong))    


if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(24, 2024)

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
