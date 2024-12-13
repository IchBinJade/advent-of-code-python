"""
Author: IchBinJade
Date  : 2024-12-10
AoC 2024 Day 9 - https://adventofcode.com/2024/day/9
"""

import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file

def defrag_disks(disk_map):
    defrag_list = []
    field_id = 0
    for idx, character in enumerate(disk_map[0]):
        block = int(character)
        if idx % 2 == 0:
            defrag_list += [field_id] * block
            field_id += 1
        else:
            defrag_list += ["."] * block
    
    return defrag_list


def organise_bytes(defrag_list):
    empty_spaces = [idx for idx, pos in enumerate(defrag_list) if pos == "."]
    
    # Process the list by replacing "." with values popped from the end
    for idx in empty_spaces:
        while defrag_list[-1] == ".":
            defrag_list.pop()
        
        # Bounds check
        if len(defrag_list) <= idx: 
            break
        
        # Replace the "." with the last popped value
        defrag_list[idx] = defrag_list.pop()
        
    return defrag_list


def defrag_disks_with_details(disk_map):
    defrag_list = []
    block_count = 0
    block_map = {}
    
    for idx in range(len(disk_map)):
        if idx % 2 == 0:
            start_idx = len(defrag_list)
            block_size = int(disk_map[idx])
            defrag_list.extend([block_count] * block_size)
            block_map[block_count] = (start_idx, block_size)
            block_count += 1
        else:
            free_size = int(disk_map[idx])
            defrag_list.extend(['.'] * free_size)
    
    return defrag_list, block_map


def organise_blocks(defrag_list, block_map):
    for file_id in reversed(list(block_map.keys())):
        curr_idx, curr_size = block_map[file_id]
        free_idx, free_size = 0, 0
        can_move = True
        while free_size < curr_size and can_move:
            if free_idx >= curr_idx:
                can_move = False
            if defrag_list[free_idx] != ".":
                free_idx += 1
                free_size = 0
            elif defrag_list[free_idx + free_size] == ".":
                free_size += 1
            else:
                free_idx += free_size
                free_size = 0
                
        if can_move:
            for x in range(curr_size):
                defrag_list[free_idx + x] = file_id
                defrag_list[curr_idx + x] = "."
    
    return defrag_list


def part_one(data_input):
    defrag_list = defrag_disks(data_input)

    ordered_list = organise_bytes(defrag_list)
    
    checksum = [idx * int(file_id) for idx, file_id in enumerate(ordered_list) if file_id != "."]

    return sum(checksum)


def part_two(data_input):    
    defrag_str = "".join([str(ch) for ch in data_input])

    defrag_list, block_map = defrag_disks_with_details(defrag_str)
    
    ordered_list = organise_blocks(defrag_list, block_map)
    
    checksum = [idx * int(file_id) for idx, file_id in enumerate(ordered_list) if file_id != "."]

    return sum(checksum)



if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(9, 2024)

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
