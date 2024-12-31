"""
Author: IchBinJade
Date  : 2024-12-30
AoC 2022 Day 21 - https://adventofcode.com/2022/day/21

Recursive expression evaluation and symbolic algebra with sympy
"""

import sys
import os
import time
import sympy

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file

NODES = {}
"""
{
    "node": [instruction, value],
    "root": [pppw + sjmn, 0],
    "dbpl": [None, "5"],
}
"""

OPS = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y
}

def do_yell(node_id):
    # Base case if the value is an integer
    if NODES[node_id][1] != 0:
        return NODES[node_id][1]
    
    instruction = NODES[node_id][0]
    if instruction is None:
        return NODES[node_id][1]
    
    if " " in instruction:
        # Evaluate operation
        l_node, op, r_node = instruction.split()
        l_val, r_val = do_yell(l_node), do_yell(r_node)
        
        if op == "+":
            result = l_val + r_val
        if op == "-":
            result = l_val - r_val
        if op == "*":
            result = l_val * r_val
        if op == "/":
            result = l_val // r_val
    else:
        result = int(instruction)
    
    NODES[node_id][1] = result
        
    return result


def part_one(data_input):
    global NODES

    for line in data_input:
        node_id, instr = line.split(": ")
        if instr.isdigit():
            NODES[node_id] = [None, int(instr)]
        else:
            NODES[node_id] = [instr, 0]
        
    root_value = do_yell("root")
    NODES = {}
        
    return root_value


def part_two(data_input):
    global NODES

    NODES["humn"] = sympy.Symbol("H")
    lines = [line.strip() for line in data_input]

    for node in lines:
        node_id, instr = node.split(": ")
        if node_id in NODES:
            continue
        if instr.isdigit():
            NODES[node_id] = sympy.Integer(instr)
        else:
            left, op, right = instr.split()
            if left in NODES and right in NODES:
                if node_id == "root":
                    solution = sympy.solve(NODES[left] - NODES[right])[0]
                    break
                NODES[node_id] = OPS[op](NODES[left], NODES[right])
            else:
                lines.append(node)
    
    return solution


if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(21, 2022)

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
