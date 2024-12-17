"""
Author: IchBinJade
Date  : 2024-12-17
AoC 2024 Day 16 - https://adventofcode.com/2024/day/16

Utilises: Dijkstra's algorithm
"""

import sys
import os
import time
import heapq

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file

def traverse_part_one(maze, start_pos):
    cost = 0
    start_row, start_col = start_pos
    dr, dc = 0, 1 # As we start facing east
    priority_q = [(cost, start_row, start_col, dr, dc)]
    visited = {(start_row, start_col, dr, dc)}
    
    while priority_q:
        cost, curr_row, curr_col, dr, dc = heapq.heappop(priority_q)
        visited.add((curr_row, curr_col, dr, dc))
        
        if maze[curr_row][curr_col] == "E":
            return cost
        
        DIRECTIONS = [(cost + 1, curr_row + dr, curr_col + dc, dr, dc), (cost + 1000, curr_row, curr_col, dc, -dr), (cost + 1000, curr_row, curr_col, -dc, dr)]
        for new_cost, new_row, new_col, new_dr, new_dc in DIRECTIONS:
            if maze[new_row][new_col] != "#" and (new_row, new_col, new_dr, new_dc) not in visited:
                heapq.heappush(priority_q, (new_cost, new_row, new_col, new_dr, new_dc))
    

def part_one(data_input):
    maze = [list(row) for row in data_input]
    # print("Maze:\n")
    # for row in maze:
    #     print(*row, sep="")
        
    for idx, row in enumerate(maze):
        if "S" in row:
            start_pos = (idx, row.index("S"))
            break
        
    return traverse_part_one(maze, start_pos)


def part_two(data_input):
    
    pass

TEST_INPUT_1 = ['###############', '#.......#....E#', '#.#.###.#.###.#', '#.....#.#...#.#', '#.###.#####.#.#', '#.#.#.......#.#', '#.#.#####.###.#', '#...........#.#', '###.#.#####.#.#', '#...#.....#.#.#', '#.#.#.###.#.#.#', '#.....#...#.#.#', '#.###.#.#.#.#.#', '#S..#.....#...#', '###############']
TEST_INPUT_2 = ['#################', '#...#...#...#..E#', '#.#.#.#.#.#.#.#.#', '#.#.#.#...#...#.#', '#.#.#.#.###.#.#.#', '#...#.#.#.....#.#', '#.#.#.#.#.#####.#', '#.#...#.#.#.....#', '#.#.#####.#.###.#', '#.#.#.......#...#', '#.#.###.#####.###', '#.#.#...#.....#.#', '#.#.#.#####.###.#', '#.#.#.........#.#', '#.#.#.#########.#', '#S#.............#', '#################']

if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(16, 2024)
    
    # input_data = TEST_INPUT_2

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
