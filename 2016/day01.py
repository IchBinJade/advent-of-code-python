"""
Author: IchBinJade
Date  : 2025-01-07
AoC 2016 Day 1 - https://adventofcode.com/2016/day/1
"""

import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file


def part_one(data_input):
    x, y = 0, 0
    compass = ["N", "E", "S", "W"]
    facing_dir = 0
    
    for instr in data_input[0].split(", "):
        left_or_right, no_of_steps = instr[0], int(instr[1:])
        
        if left_or_right == "R":
            facing_dir = (facing_dir + 1) % 4
        else:
            facing_dir = (facing_dir - 1) % 4
            
        if compass[facing_dir] == "N":
            y += no_of_steps
        elif compass[facing_dir] == "E":
            x += no_of_steps
        elif compass[facing_dir] == "S":
            y -= no_of_steps
        elif compass[facing_dir] == "W":
            x -= no_of_steps

    blocks_away = abs(x) + abs(y)

    return blocks_away


def part_two(data_input):
    x, y = 0, 0
    compass = ["N", "E", "S", "W"]
    facing_dir = 0
    visited = set()
    visited.add((x, y))
    
    for instr in data_input[0].split(", "):
        left_or_right, no_of_steps = instr[0], int(instr[1:])
        
        if left_or_right == "R":
            facing_dir = (facing_dir + 1) % 4
        else:
            facing_dir = (facing_dir - 1) % 4
        
        for _ in range(no_of_steps):
            if compass[facing_dir] == "N":
                y += 1
            elif compass[facing_dir] == "E":
                x += 1
            elif compass[facing_dir] == "S":
                y -= 1
            elif compass[facing_dir] == "W":
                x -= 1
                
            if (x, y) in visited:
                return abs(x) + abs(y)
            visited.add((x, y))
        
    return None


if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(1, 2016)
    
    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
