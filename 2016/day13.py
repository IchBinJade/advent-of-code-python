"""
Author: IchBinJade
Date  : 2025-01-12
AoC 2016 Day 13 - https://adventofcode.com/2016/day/13

Find number of steps in shortest path, and unique locations within 50 steps

TODO: Refactor find_shortest_path to incorporate find_unique_locations logic
"""

import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file
from collections import deque

DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)] # Up, Down, Left, Right


def is_coord_open(x, y, num):
    new_num = x*x + 3*x + 2*x*y + y + y*y
    new_num += num
    bin_num = bin(new_num)
    bin_one_count = str(bin_num).count("1")
    
    return bin_one_count % 2 == 0


def find_shortest_path(designer_num, dest_coord):
    cr, cc = 1, 1
    step_count = 0
    
    queue = deque([(cr, cc, 0)])
    visited = set()
    
    while queue:
        cr, cc, step_count = queue.popleft()
        if (cr, cc) == dest_coord:
            return step_count
        
        for dr, dc in DIRECTIONS:
            nr, nc = cr + dr, cc + dc
            if is_coord_open(nr, nc, designer_num) and (nr, nc) not in visited:
                queue.append((nr, nc, step_count + 1))
                visited.add((nr, nc))


def find_unique_locations(designer_num):
    """ Find all unique locations reachable in at most 50 steps. """
    queue = deque([((1, 1), 0)])
    seen = set()

    while queue:
        (x, y), steps = queue.popleft()

        if steps > 50:
            continue
        
        seen.add((x, y))

        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or (nx, ny) in seen or not is_coord_open(nx, ny, designer_num):
                continue

            queue.append(((nx, ny), steps + 1))

    return len(seen)


def part_one(data_input):
    designer_num = int(data_input[0])
    # dest_coord = (7, 4) # Testing
    dest_coord = (31, 39)
    
    min_steps = find_shortest_path(designer_num, dest_coord)
    
    return min_steps


def part_two(data_input):
    designer_num = int(data_input[0])
    
    unique_locations = find_unique_locations(designer_num)
    
    return unique_locations


TEST_INPUT_1 = ["10"]

if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(13, 2016)
    
    # input_data = TEST_INPUT_1

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
