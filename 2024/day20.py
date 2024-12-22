"""
Author: IchBinJade
Date  : 2024-12-22
AoC 2024 Day 20 - https://adventofcode.com/2024/day/20

Utilises: BFS & 'teleporting'
"""

import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file

DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def find_path(start_pos, grid):
    queue = [start_pos]
    
    dist_matrix = {(start_pos): 0}
    
    for row, col in queue:
        dist = dist_matrix[(row, col)]
        for dr, dc in DIRECTIONS:
            next_row, next_col = row + dr, col + dc
            if 0 <= next_row < len(grid) and 0 <= next_col < len(grid[0]):
                if (next_row, next_col) not in dist_matrix and grid[next_row][next_col] != "#":
                    queue.append((next_row, next_col))
                    dist_matrix[(next_row, next_col)] = dist + 1
    
    return dist_matrix


def calc_cheat_times(dist_matrix, dist):
    cheat_times = {}
    
    for row, col in dist_matrix:
        for dr, dc in DIRECTIONS:
            next_row, next_col = row + (dist * dr), col + (dist * dc)
            if (next_row, next_col) in dist_matrix:
                if dist_matrix[(row, col)] > dist_matrix[(next_row, next_col)]:
                    new_time = dist_matrix[(row, col)] - dist_matrix[(next_row, next_col)] - dist
                    if new_time > 0:
                        cheat_times[((row, col), (next_row, next_col))] = new_time
    
    return cheat_times


def calc_new_cheat_times(dist_matrix, dist=20):
    cheat_times = {}
    
    for row, col in dist_matrix:
        for dr in range(-dist, dist + 1, 1):
            for dc in range(-dist, dist + 1, 1):
                if abs(dr) + abs(dc) <= 20:
                    next_row, next_col = row + dr, col + dc
                    if (next_row, next_col) in dist_matrix:
                        if dist_matrix[(row, col)] > dist_matrix[(next_row, next_col)]:
                            new_time = dist_matrix[(row, col)] - dist_matrix[(next_row, next_col)] - abs(dr) - abs(dc)
                            if new_time > 0:
                                cheat_times[((row, col), (next_row, next_col))] = new_time
    
    return cheat_times
    

def part_one(data_input):
    grid = [list(row) for row in data_input]
    
    for idx, row in enumerate(grid):
        if "S" in row:
            start_pos = (idx, row.index("S"))
        
    dist_matrix = find_path(start_pos, grid)
    # for row in dist_matrix:
    #     print(*row, sep="")
    cheats = calc_cheat_times(dist_matrix, dist=2)
    
    count = 0
    for timings in cheats:
        saved = cheats[timings]
        if saved >= 100:
            count += 1
    
    return count


def part_two(data_input):
    grid = [list(row) for row in data_input]
    
    for idx, row in enumerate(grid):
        if "S" in row:
            start_pos = (idx, row.index("S"))
        
    dist_matrix = find_path(start_pos, grid)
    
    cheats = calc_new_cheat_times(dist_matrix, dist=20)
    
    count = 0
    for timings in cheats:
        saved = cheats[timings]
        if saved >= 100:
            count += 1
    
    return count
    

if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(20, 2024)
    
    # input_data = TEST_INPUT

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
