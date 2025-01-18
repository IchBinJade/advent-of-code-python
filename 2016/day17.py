"""
Author: IchBinJade
Date  : 2025-01-18
AoC 2016 Day 17 - https://adventofcode.com/2016/day/17

Uses recursion to find the shortest path and the longest path in a 4x4 grid, where movement is 
determined by the state of doors that can open based on an MD5 hash of a passcode combined with 
the current path
"""

import sys
import os
import time
import hashlib

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file

TARGET = [3, 3]


def get_hash(name):
    m = hashlib.md5()
    m.update(name.encode())
    
    return m.hexdigest()


def get_open_doors(passcode, path):
    hash_value = get_hash(passcode + path)
    open_doors = []
    
    if hash_value[0] in "bcdef":
        open_doors.append("U")
    if hash_value[1] in "bcdef":
        open_doors.append("D")
    if hash_value[2] in "bcdef":
        open_doors.append("L")
    if hash_value[3] in "bcdef":
        open_doors.append("R")
    
    return open_doors


def find_shortest_path(passcode, coord, path=""):
    global SHORTEST
    
    if len(path) > 0 and path[-1] == "U":
        coord[1] -= 1
    elif len(path) > 0 and path[-1] == "D":
        coord[1] += 1
    elif len(path) > 0 and path[-1] == "L":
        coord[0] -= 1
    elif len(path) > 0 and path[-1] == "R":
        coord[0] += 1
    
    # Bounds check    
    if (coord[0] > 3 or coord[0] < 0) or (coord[1] > 3 or coord[1] < 0):
        return None
    elif coord == TARGET:
        if len(path) < SHORTEST:
            SHORTEST = len(path)
        return path
    
    open_doors = get_open_doors(passcode, path)
    
    final_path = None
    for door in open_doors:
        temp_path = path + door
        if len(temp_path) > SHORTEST:
            return None
        
        temp_coord = coord[:]
        end_path = find_shortest_path(passcode, temp_coord, temp_path)
        if final_path == None:
            final_path = end_path
        elif end_path != None and len(end_path) < len(final_path):
            final_path = end_path

    return final_path


def find_longest_path(passcode, coord, path=""):
    global LONGEST
    
    if len(path) > 0 and path[-1] == "U":
        coord[1] -= 1
    elif len(path) > 0 and path[-1] == "D":
        coord[1] += 1
    elif len(path) > 0 and path[-1] == "L":
        coord[0] -= 1
    elif len(path) > 0 and path[-1] == "R":
        coord[0] += 1
        
    # Bounds check    
    if (coord[0] > 3 or coord[0] < 0) or (coord[1] > 3 or coord[1] < 0):
        return None
    elif coord == TARGET:
        if len(path) > LONGEST:
            LONGEST = len(path)
        return path
    
    open_doors = get_open_doors(passcode, path)
    
    final_steps = None
    for door in open_doors:
        temp_path = path + door
        temp_coord = coord[:]
        end_steps = find_longest_path(passcode, temp_coord, temp_path)
        if final_steps == None:
            final_steps = end_steps
        elif end_steps != None and len(end_steps) > len(final_steps):
            final_steps = end_steps
    
    return final_steps


def part_one(data_input):
    global SHORTEST
    SHORTEST = 1000
    
    passcode = data_input[0]
    coord = [0, 0]
    
    shortest_path = find_shortest_path(passcode, coord)
    
    return shortest_path


def part_two(data_input):
    global LONGEST
    LONGEST = -1
    
    passcode = data_input[0]
    coord = [0, 0]
    
    longest_steps = find_longest_path(passcode, coord)
    
    return len(longest_steps)


if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(17, 2016)

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
