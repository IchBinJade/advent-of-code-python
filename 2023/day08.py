"""
Author: IchBinJade
Date  : 2024-12-07
AoC 2023 Day 8 - https://adventofcode.com/2023/day/8
"""

import sys
import os
import time
import re

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file


def get_linked_dict(raw_input):
    """
    Create a DLL-type dictionary that looks like:

    GRAPH = {
        node: (left, right),
    }
    """
    node_dict = {}
    
    for line in raw_input:
        #print(f"line >>> {line}")
        match_list = re.findall(r"\w{3}", line)
        
        #print(f"match_list >>> {match_list}")
        parent, left, right = match_list
        node_dict[parent] = tuple((left, right))
    
    return node_dict


def do_traversal(instruction, graph, start_node):
    count = 0
    move_idx = 0
    curr_node = start_node
    
    while curr_node != "ZZZ":
        # Assign current node's left/right kids
        left, right = graph[curr_node]
        # Follow the instruction
        if instruction[move_idx] == "L":
            curr_node = left
        else:
            curr_node = right
        # Move to next instruction, check bound and wrap around
        move_idx += 1
        if move_idx >= len(instruction):
            move_idx = 0

        count += 1
    
    return count


def part_one(data_input):
    """Use a sort of DLL and traverse to get count"""
    instruction = data_input[0]
    graph = get_linked_dict(data_input[2:])
    start_node = "AAA"
    
    return do_traversal(instruction, graph, start_node)


def part_two(data_input):
    pass


TEST_INPUT = ['RL', '', 'AAA = (BBB, CCC)', 'BBB = (DDD, EEE)', 'CCC = (ZZZ, GGG)', 'DDD = (DDD, DDD)', 'EEE = (EEE, EEE)', 'GGG = (GGG, GGG)', 'ZZZ = (ZZZ, ZZZ)']

if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(8, 2023)
    
    # input_data = TEST_INPUT

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
