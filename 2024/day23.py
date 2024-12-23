"""
Author: IchBinJade
Date  : 2024-12-23
AoC 2024 Day 23 - https://adventofcode.com/2024/day/23

Utilises: DFS
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
        for computer_2 in neighbours_1:
            for computer_3  in neighbours_1:
                if computer_2 == computer_3:
                    continue
                if computer_2 in graph[computer_3]:
                    connected = tuple(sorted([computer_1, computer_2, computer_3]))
                    amigos.add(connected)
    
    return amigos


def find_connected_components(graph):
    sets = set()
    
    def dfs(node, required):
        key = tuple(sorted(required))
        if key in sets:
            return
        sets.add(key)
        
        for neighbour in graph[node]:
            if neighbour not in required and all(neighbour in graph[query] for query in required):
                dfs(neighbour, {*required, neighbour})
        
    
    for node in graph:
        dfs(node, {node})
            
    return sets
    

def part_one(data_input):
    total = 0

    graph = {}
    for connection in data_input:
        node_1, node_2 = connection.split("-")
        if node_1 not in graph:
            graph[node_1] = set()
        if node_2 not in graph:
            graph[node_2] = set()
        graph[node_1].add(node_2)
        graph[node_2].add(node_1)

    threes_list = locate_three_amigos(graph)

    for network in sorted(threes_list):
        for node in network:
            if node.startswith("t"):
                total += 1
                break
        
    return total


def part_two(data_input):
    graph = {}
    for connection in data_input:
        node_1, node_2 = connection.split("-")
        if node_1 not in graph:
            graph[node_1] = set()
        if node_2 not in graph:
            graph[node_2] = set()
        graph[node_1].add(node_2)
        graph[node_2].add(node_1)
    
    sets = find_connected_components(graph)
    
    largest = max(sets, key=len)

    return ",".join(sorted(largest))


if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(23, 2024)

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
