"""
Author: IchBinJade
Date  : 2024-12-15
AoC 2024 Day 14 - https://adventofcode.com/2024/day/14

TODO: Start and solve part 2
"""

import sys
import os
import time
import re

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file


def get_quadrants(grid):
    h = len(grid)
    w = len(grid[0])
    
    # Remove the middle rows, as per instructions
    if h % 2 != 0:
        grid = grid[:(h // 2)] + grid[(h // 2 + 1):]
    if w % 2 != 0:
        grid = [row[:(w // 2)] + row[(w // 2 + 1):] for row in grid]
        
    # Recalc grid dimensions before splitting
    h = len(grid)
    w = len(grid[0])
    mid_h = h // 2
    mid_w = w // 2
    
    top_left = [row[:mid_w] for row in grid[:mid_h]]
    top_right = [row[mid_w:] for row in grid[:mid_h]]
    bottom_left = [row[:mid_w] for row in grid[mid_h:]]
    bottom_right = [row[mid_w:] for row in grid[mid_h:]]
    
    quad_list = [top_left, top_right, bottom_left, bottom_right]
    
    return quad_list


def move_robots(bots):
    # make a grid: start with test dimensions of 11 x 7
    #width = 11
    #height = 7
    width = 101
    height = 103
    grid = [[0 for _ in range(width)] for _ in range(height)]
    #print(f"starting grid >>> {grid}")
    
    for bot in bots:
        x, y, dx, dy = bot
        x = x % width
        y = y % height
        grid[y][x] += 1
        for _ in range(100):
            next_x = (x + dx) % width
            next_y = (y + dy) % height
            grid[next_y][next_x] += 1
            if grid[y][x] > 0:
                grid[y][x] -= 1
            x, y = next_x, next_y
    
    # print(f"final grid >>> {grid}")      
    return grid


def parse_input(raw_input):
    input_str = "\n".join(raw_input)
    bot_list = []
    for _, bot in enumerate(input_str.split("\n")):
            numbers = re.findall(r"-?\d+", bot)
            numbers_tuple = tuple(map(int, numbers))
            bot_list.append(numbers_tuple)
    
    return bot_list

def part_one(data_input):
    total = 1
    bot_list = parse_input(data_input)

    final_grid = move_robots(bot_list)

    quadrants = get_quadrants(final_grid)
    #print(f"quadrants >>> {quadrants}")
    for quad in quadrants:
        #print(f"quad >>> {quad}")
        bots = sum([sum(row) for row in quad])
        # print(f"bots in quad >>> {bots}")
        total *= bots

    return total


def part_two(data_input):

    
    return None

TEST_INPUT = ['p=0,4 v=3,-3', 'p=6,3 v=-1,-3', 'p=10,3 v=-1,2', 'p=2,0 v=2,-1', 'p=0,0 v=1,3', 'p=3,0 v=-2,-2', 'p=7,6 v=-1,-3', 'p=3,0 v=-1,-2', 'p=9,3 v=2,3', 'p=7,3 v=-1,2', 'p=2,4 v=2,-3', 'p=9,5 v=-3,-3']

if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(14, 2024)
    
    #input_data = TEST_INPUT

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
