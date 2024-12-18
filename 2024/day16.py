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
from collections import deque

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
                
                
def traverse_part_two(maze, start_pos):
    start_row, start_col = start_pos
    
    priority_q = [(0, start_row, start_col, 0, 1)]
    lowest_cost = {(start_row, start_col, 0, 1): 0}
    best_cost = float('inf')
    backtrack = {}
    end_states = set()
    
    while priority_q:
        cost, curr_row, curr_col, dr, dc = heapq.heappop(priority_q)
        
        if cost > lowest_cost.get((curr_row, curr_col, dr, dc), float('inf')): continue
        
        if maze[curr_row][curr_col] == "E":
            if cost > best_cost:
                break
            best_cost = cost
            end_states.add((curr_row, curr_col, dr, dc))
            
        # Explore directions
        DIRECTIONS = [(cost + 1, curr_row + dr, curr_col + dc, dr, dc), (cost + 1000, curr_row, curr_col, dc, -dr), (cost + 1000, curr_row, curr_col, -dc, dr)]
        for new_cost, new_row, new_col, new_dr, new_dc in DIRECTIONS:
            if maze[new_row][new_col] == "#": continue
            # Process if this is a cheaper way to reach the state
            if new_cost > lowest_cost.get((new_row, new_col, new_dr, new_dc), float('inf')): continue
            if new_cost < lowest_cost.get((new_row, new_col, new_dr, new_dc), float('inf')):
                backtrack[(new_row, new_col, new_dr, new_dc)] = set()
                lowest_cost[(new_row, new_col, new_dr, new_dc)] = new_cost
            
            # Record previous state for backtracking
            backtrack[(new_row, new_col, new_dr, new_dc)].add((curr_row, curr_col, dr, dc))
            heapq.heappush(priority_q, (new_cost, new_row, new_col, new_dr, new_dc))
            
        # Backtrack the end states to collect tiles in best paths
        states = deque(end_states)
        visited = set(end_states)
        
        while states:
            id = states.popleft()
            for last in backtrack.get(id, []):
                if last not in visited:
                    visited.add(last)
                    states.append(last)
                        
    return visited
    

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
    maze = [list(row) for row in data_input]
    # print("Maze:\n")
    # for row in maze:
    #     print(*row, sep="")
        
    for idx, row in enumerate(maze):
        if "S" in row:
            start_pos = (idx, row.index("S"))
            break
        
    best_tiles = traverse_part_two(maze, start_pos)
    
    return len({(row, col) for row, col, _, _ in best_tiles})


if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(16, 2024)

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
