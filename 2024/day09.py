"""
Author: IchBinJade
Date  : 2024-12-10
AoC 2024 Day 9 - https://adventofcode.com/2024/day/9

TODO: Start and solve part 2
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


def organise_blocks(defrag_list):
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


def part_one(data_input):
    #print(data_input)
    defrag_list = defrag_disks(data_input)
    #print(f"defrag_list >>> {defrag_list}")

    ordered_list = organise_blocks(defrag_list)
    #print(f"defrag after ordering >>> {ordered_list}")
    
    # Calculate checksum, skipping empty spaces ('.')
    checksum = [idx * file_id for idx, file_id in enumerate(ordered_list) if file_id != "."]
    #print(f"checksum >>> {checksum}")

    return sum(checksum)


def part_two(data_input):
    pass


TEST_INPUT_1 = ['12345']
TEST_INPUT_2 = ['2333133121414131402']

if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(9, 2024)
    
    #input_data = TEST_INPUT_2

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
