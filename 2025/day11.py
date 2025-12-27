"""
Author: IchBinJade
Date  : 2025-12-27
AoC 2025 Day 11 - https://adventofcode.com/2025/day/11
"""

import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file
from collections import deque
from functools import cache


DEVICES2 = {}

def count_paths(devices):
    count = 0
    queue = deque(["you"])
    while queue:
        current = queue.popleft()
        if current == "out":
            count += 1
            continue
        
        neighbours = devices.get(current, [])
        for neighbour in neighbours:
            queue.append(neighbour)
    
    return count


@cache
def count_paths_memoized(current_node, target_node):
    if current_node == target_node:
        return 1
    
    total = 0
    
    for neighbour in DEVICES2.get(current_node, []):
        total += count_paths_memoized(neighbour, target_node)
        
    return total


def count_paths_with_waypoints():
    # Potential Path 1: svr > dac > fft > out
    Leg1 = count_paths_memoized("svr", "dac")
    Leg2 = count_paths_memoized("dac", "fft")
    Leg3 = count_paths_memoized("fft", "out")
    Paths_A = Leg1 * Leg2 * Leg3
    
    # Potential Path 2: svr > fft > dac > out
    Leg4 = count_paths_memoized("svr", "fft")
    Leg5 = count_paths_memoized("fft", "dac")
    Leg6 = count_paths_memoized("dac", "out")
    Paths_B = Leg4 * Leg5 * Leg6
    
    return Paths_A + Paths_B


def part_one(data_input):
    devices = {}
    for line in data_input:
        key, values = line.split(":")[0], [value for value in line.split(":")[1].split()]
        devices[key] = values
    
    return count_paths(devices)


def part_two(data_input):
    global DEVICES2
    for line in data_input:
        key, values = line.split(":")[0], [value for value in line.split(":")[1].split()]
        DEVICES2[key] = values
        
    return count_paths_with_waypoints()



if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(11, 2025)

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
