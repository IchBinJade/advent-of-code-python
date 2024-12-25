"""
Author: IchBinJade
Date  : 2024-12-24
AoC 2024 Day 24 - https://adventofcode.com/2024/day/24
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
    
    # Calculate wire_1 and wire_2, recursively. 
    # First check if the wires are actually keys to other wires
    operator, wire_1, wire_2 = CALCS_DICT[wire]
    # print(f"Calculating {wire}: {operator} {wire_1} {wire_2}")
    wire_1_value = calculate_wires(wire_1)
    wire_2_value = calculate_wires(wire_2)
    
    # Apply logical operator
    if operator == "AND":
        WIRES_DICT[wire] = wire_1_value & wire_2_value
    if operator == "OR":
        WIRES_DICT[wire] = wire_1_value | wire_2_value
    if operator == "XOR":
        WIRES_DICT[wire] = wire_1_value ^ wire_2_value
    # print(f"Wire {wire} calculated as {WIRES_DICT[wire]}")
    return WIRES_DICT[wire]


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
        
    # print(f"wires_dict = {WIRES_DICT}")
    # print(f"calc_dict = {CALCS_DICT}")
    
    binary_list = []
    idx = 0
    while True:
        wire_key = f"z{idx:02}"
        if wire_key not in CALCS_DICT:
            break
        binary_list.append(calculate_wires(wire_key))
        idx += 1
    # print(f"binary_list >>> {binary_list}")
    binary_num = "".join(map(str, binary_list[::-1]))
    
    # print(f"binary_num = {binary_num}")
    
    return int(binary_num, 2)


def part_two(data_input):
    pass

TEST_INPUT_1 = ['x00: 1', 'x01: 1', 'x02: 1', 'y00: 0', 'y01: 1', 'y02: 0', '', 'x00 AND y00 -> z00', 'x01 XOR y01 -> z01', 'x02 OR y02 -> z02']
TEST_INPUT_2 = ['x00: 1', 'x01: 0', 'x02: 1', 'x03: 1', 'x04: 0', 'y00: 1', 'y01: 1', 'y02: 1', 'y03: 1', 'y04: 1', '', 'ntg XOR fgs -> mjb', 'y02 OR x01 -> tnw', 'kwq OR kpj -> z05', 'x00 OR x03 -> fst', 'tgd XOR rvg -> z01', 'vdt OR tnw -> bfw', 'bfw AND frj -> z10', 'ffh OR nrd -> bqk', 'y00 AND y03 -> djm', 'y03 OR y00 -> psh', 'bqk OR frj -> z08', 'tnw OR fst -> frj', 'gnj AND tgd -> z11', 'bfw XOR mjb -> z00', 'x03 OR x00 -> vdt', 'gnj AND wpb -> z02', 'x04 AND y00 -> kjc', 'djm OR pbm -> qhw', 'nrd AND vdt -> hwm', 'kjc AND fst -> rvg', 'y04 OR y02 -> fgs', 'y01 AND x02 -> pbm', 'ntg OR kjc -> kwq', 'psh XOR fgs -> tgd', 'qhw XOR tgd -> z09', 'pbm OR djm -> kpj', 'x03 XOR y03 -> ffh', 'x00 XOR y04 -> ntg', 'bfw OR bqk -> z06', 'nrd XOR fgs -> wpb', 'frj XOR qhw -> z04', 'bqk OR frj -> z07', 'y03 OR x01 -> nrd', 'hwm AND bqk -> z03', 'tgd XOR rvg -> z12', 'tnw OR pbm -> gnj']

if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(24, 2024)
    
    # input_data = TEST_INPUT_1

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
