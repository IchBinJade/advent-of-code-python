"""
Author: IchBinJade
Date  : 2024-12-15
AoC 2024 Day 14 - https://adventofcode.com/2024/day/14
"""

import sys
import os
import time
import re

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file
from collections import deque
from PIL import Image

def save_grid_as_image(grid, folder, step_number):
    filename = os.path.join(folder, f"image{step_number}.png")
    # Get the dimensions of the grid
    height = len(grid)
    width = len(grid[0])

    # Create a new image (mode '1' is 1-bit color, black and white)
    image = Image.new('1', (width, height))

    # Create a list of pixel values where 0 -> white and 1 -> black (robots)
    pixels = []
    for row in grid:
        for value in row:
            pixels.append(0 if value > 0 else 1)  # white for robot, black for empty

    # Put the pixel data into the image
    image.putdata(pixels)

    # Save the image to the specified file
    image.save(filename)


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
    width = 101
    height = 103
    grid = [[0 for _ in range(width)] for _ in range(height)]

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
     
    return grid


def find_easter_egg(bot_list):
    """ 
    Re-using part 1's function but moving every bot every second, instead of
    moving 1 bot for 100 seconds before moving to the next. And find the safety
    factor after each second, returning the lowest
    """
    width = 101
    height = 103
    grid = [[0 for _ in range(width)] for _ in range(height)]
    
    safety_factors_list = []
    min_safety = float('inf')
    best_time = 0
    step_number = 1 # For creating the grid image
    
    for time in range(1, width * height + 1):
        for idx, bot in enumerate(bot_list):
            x, y, dx, dy = bot
            x = x % width
            y = y % height
            next_x = (x + dx) % width
            next_y = (y + dy) % height
            grid[next_y][next_x] += 1
            if grid[y][x] > 0:
                grid[y][x] -= 1
            bot_list[idx] = (next_x, next_y, dx, dy)
        # PRINT GRID
        folder = "day14_images"
        save_grid_as_image(grid, folder, step_number)
        step_number += 1
            
        # Calc safety factor after this second
        quadrants = get_quadrants(grid)
        safety_factor = 1
        for quad in quadrants:
            bots_in_quad = sum([sum(row) for row in quad])
            safety_factor *= bots_in_quad
            
        safety_factors_list.append(safety_factor)
        if safety_factor < min_safety:
            min_safety = safety_factor
            best_time = time
            
    return best_time


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
    for quad in quadrants:
        bots = sum([sum(row) for row in quad])
        total *= bots

    return total


def part_two(data_input):
    bot_list = parse_input(data_input)
    result =  find_easter_egg(bot_list)
    return result


if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(14, 2024)

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
