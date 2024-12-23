"""
Author: IchBinJade
Date  : 2024-12-23
AoC 2024 Day 23 - https://adventofcode.com/2024/day/23
"""

import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file


def locate_three_amigos(graph):
    amigos = set()
    
    for computer_1 in graph:
        neighbours_1 = graph[computer_1]
        # For each pair, 2 and 3, check if they're connected via neighbours
        for computer_2 in neighbours_1:
            for computer_3  in neighbours_1:
                # if duplicate pair, skip
                if computer_2 == computer_3:
                    continue
                # check if 2 and 3 neighbours of each other
                if computer_2 in graph[computer_3]:
                    # we've found a set of 3, set new amigo to sorted tuple then add to set
                    connected = tuple(sorted([computer_1, computer_2, computer_3]))
                    amigos.add(connected)
    
    return amigos


def part_one(data_input):
    total = 0
    
    # Create a graph of nodes from the input
    graph = {}
    # Loop input
    for connection in data_input:
        # set first and second computers
        node_1, node_2 = connection.split("-")
        # check if either computers already in graph and add if not
        if node_1 not in graph:
            graph[node_1] = set()
        if node_2 not in graph:
            graph[node_2] = set()
        # add computers to graph
        graph[node_1].add(node_2)
        graph[node_2].add(node_1)
        
    # Find sets of 3
    threes_list = locate_three_amigos(graph)
    # print("LIST OF CONNECTED COMPS:")
    # for row in sorted(threes_list):
    #     print(*row, sep=",")

    for network in sorted(threes_list):
        for node in network:
            if node.startswith("t"):
                total += 1
                break
        
    return total


def part_two(data_input):

    return None

TEST_INPUT = ['kh-tc', 'qp-kh', 'de-cg', 'ka-co', 'yn-aq', 'qp-ub', 'cg-tb', 'vc-aq', 'tb-ka', 'wh-tc', 'yn-cg', 'kh-ub', 'ta-co', 'de-co', 'tc-td', 'tb-wq', 'wh-td', 'ta-ka', 'td-qp', 'aq-cg', 'wq-ub', 'ub-vc', 'de-ta', 'wq-aq', 'wq-vc', 'wh-yn', 'ka-de', 'kh-ta', 'co-tc', 'wh-qp', 'tb-vc', 'td-yn']

if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(23, 2024)
    
    input_data = TEST_INPUT

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
