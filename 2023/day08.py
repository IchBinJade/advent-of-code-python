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
from itertools import cycle
from math import lcm


def get_linked_dict(raw_input):
    """
    Create a DLL-type dictionary that looks like:

    GRAPH = {
        node: (left, right),
    }
    
    Args:
        raw_input(str): A string of the node parents and left, right children
        
    Returns:
        node_dict(dict): A dictionary where keys are node names, and values are tuples representing 
                         the left and right child nodes.
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
    """
    Part 1: Traverse nodes, from start node, until node "ZZZ" is found

    Args:
        instruction (str): A string of "L" and "R" characters representing the directions to follow.
        graph (dict): A dictionary where keys are node names, and values are tuples representing 
                      the left and right child nodes.
        start_node (str): Start node of "AAA" to start the traversal from

    Returns:
        count (int): Number of moves taken while traversing
    """
    count = 0
    move_idx = 0
    curr_node = start_node
    
    while curr_node != "ZZZ":
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


def do_sync_traversal(instruction, graph, start_nodes_list):
    """ 
    Part 2: Traverse multiple start nodes simultaneously. ALL nodes
    have to end up as nodes ending with "Z".

    Args:
        instruction (str): A string of "L" and "R" characters representing the directions to follow.
        graph (dict): A dictionary where keys are node names, and values are tuples representing 
                      the left and right child nodes.
        start_nodes (list): A list of nodes to start the traversal from, each node being a string.

    Returns:
        steps_list (list[int]): List of number of moves taken while traversing
    """
    steps_list = []
    
    # Track the current positions of all nodes
    node_buffer = start_nodes_list[:]
    
    for move_idx, left_or_right in enumerate(cycle(instruction)):
        next_moves = []
        for node in node_buffer:
            left, right = graph[node]
            # Follow the instruction
            if left_or_right == "L":
                next_moves.append(left)
            else:
                next_moves.append(right)
        
        node_buffer = next_moves

        # If all nodes have reached Z, record their steps
        for node in node_buffer:
            if node.endswith("Z"):
                steps_list.append(move_idx + 1)
                
        # Stop if all nodes have reached Z
        if len(steps_list) == len(start_nodes_list):
            break
    
    return steps_list


def part_one(data_input):
    """Use a sort of DLL and traverse to get count"""
    instruction = data_input[0]
    graph = get_linked_dict(data_input[2:])
    start_node = "AAA"
    
    return do_traversal(instruction, graph, start_node)


def part_two(data_input):
    #print(data_input)
    instruction = data_input[0]
    graph = get_linked_dict(data_input[2:])
    start_nodes = [node for node in graph if node.endswith("A")]
    
    steps_list = do_sync_traversal(instruction, graph, start_nodes)
    
    return lcm(*steps_list)


TEST_INPUT_1 = ['RL', '', 'AAA = (BBB, CCC)', 'BBB = (DDD, EEE)', 'CCC = (ZZZ, GGG)', 'DDD = (DDD, DDD)', 'EEE = (EEE, EEE)', 'GGG = (GGG, GGG)', 'ZZZ = (ZZZ, ZZZ)']

TEST_INPUT_2 = ['LR', '', '11A = (11B, XXX)', '11B = (XXX, 11Z)', '11Z = (11B, XXX)', '22A = (22B, XXX)', '22B = (22C, 22C)', '22C = (22Z, 22Z)', '22Z = (22B, 22B)', 'XXX = (XXX, XXX)']

if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(8, 2023)
    
    # input_data = TEST_INPUT_1

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    # input_data = TEST_INPUT_2
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
