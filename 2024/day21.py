"""
Author: IchBinJade
Date  : 2024-12-23
AoC 2024 Day 21 - https://adventofcode.com/2024/day/21

Utilises: BFS and recursion (and mind melting capabilities from the hours and hours it took to solve!)
"""

import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file
from collections import deque, defaultdict


def convert_to_nodes(pad):
    directions_map = {}
    rows = len(pad)
    cols = len(pad[0])
    
    dir_symbols = {
        "up": "^",
        "right": ">",
        "down": "v",
        "left": "<"
    }
    
    def get_valid_neighbour(r, c, direction):
        if direction == "up" and r > 0:
            return pad[r - 1][c], dir_symbols["up"]
        elif direction == "right" and c < cols - 1:
            return pad[r][c + 1], dir_symbols["right"]
        elif direction == "down" and r < rows - 1:
            return pad[r + 1][c], dir_symbols["down"]
        elif direction == "left" and c > 0:
            return pad[r][c - 1], dir_symbols["left"]
        return None, None
    
    # Build the dictionary
    for r in range(rows):
        for c in range(cols):
            pad_value = pad[r][c]
            if pad_value is None:
                continue
            
            directions = []
            for direction in ["up", "right", "down", "left"]:
                neighbour, symbol = get_valid_neighbour(r, c, direction)
                if neighbour is not None:
                    directions.append(f"{neighbour}{symbol}")
                    
            directions_map[pad_value] = tuple(directions)
            
    return directions_map


K_PAD = [
    ["7", "8", "9"],
    ["4", "5", "6"],
    ["1", "2", "3"],
    [None, "0", "A"]
]

D_PAD = [
    [None, "^", "A"],
    ["<", "v", ">"]
]

D_GRID = convert_to_nodes(D_PAD)

    
def find_path(pad, source, dest, cache={}):
    key = source, dest
    if key in cache:
        return cache[key]
    
    queue = deque([(source, "")])
    distance = defaultdict(lambda: float("inf"), {source: 0})
    paths = []
    
    while queue:
        pad_key, path = queue.popleft()
        if pad_key == dest:
            paths.append(path)
            continue

        for neighbour, direction in pad[pad_key]:
            new_dist = distance[pad_key] + 1
            if new_dist > distance[dest] or new_dist > distance[neighbour]:
                continue
            distance[neighbour] = new_dist
            queue.append((neighbour, path + direction))
            
    cache[key] = paths
    
    return paths


def interact_with_pads(pad, code, bots, curr_key="A", cache={}):
    """Recursively get the sequence to reach the code"""
    if not code:
        return 0
    
    key = code, bots, curr_key
    if key in cache:
        return cache[key]
    
    first_char = code[0]
    paths = find_path(pad, curr_key, first_char)
    
    if bots == 0:
        best = len(paths[0]) + 1
    else:
        best = min(interact_with_pads(D_GRID, path + "A", bots - 1) for path in paths)
        
    result = cache[key] = best + interact_with_pads(pad, code[1:], bots, first_char)
    return result
    

def part_one(data_input):
    total = 0
    num_grid = convert_to_nodes(K_PAD)
    
    for passcode in data_input:
        code_num = int(passcode[:-1])
        seq_length = interact_with_pads(num_grid, passcode, 2)
        total += code_num * seq_length
    
    return total


def part_two(data_input):
    total = 0
    num_grid = convert_to_nodes(K_PAD)
    
    for passcode in data_input:
        code_num = int(passcode[:-1])
        seq_length = interact_with_pads(num_grid, passcode, 25)
        total += code_num * seq_length
    
    return total


if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(21, 2024)

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
