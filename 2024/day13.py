"""
Author: IchBinJade
Date  : 2024-12-14
AoC 2024 Day 13 - https://adventofcode.com/2024/day/13

Utilises: Systems of linear equations (maths is fun!)
"""

import sys
import os
import time
import re

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file

def find_prize(game):
    min_tokens = float('inf')
    ax, ay, bx, by, px, py = game
    for a_press in range(101):
        for b_press in range(101):
            new_x = a_press * ax + b_press * bx
            new_y = a_press * ay + b_press * by
            if new_x == px and new_y == py:
                total_cost = 3 * a_press + b_press
                min_tokens = min(min_tokens, total_cost)
                
    if min_tokens == float('inf'):
        return 0
    
    return min_tokens


def find_prize_part_2(game):
    ax, ay, bx, by, px, py = game
    new_px = px + 10000000000000
    new_py = py + 10000000000000
    
    B = (new_px*ay - new_py*ax) // (ay*bx - by*ax)
    A = (new_px*by - new_py*bx) // (by*ax - bx*ay)
    
    new_x = A * ax + B * bx
    new_y = A * ay + B * by
    
    if new_x == new_px and new_y == new_py:
        total_cost = 3 * A + B
        return total_cost
    else:
        return 0  


def parse_input(data_input):
    data_str = "\n".join(data_input)
    number_list = []
    for idx, block in enumerate(data_str.split("\n\n")):
        numbers = re.findall(r"\d+", block)
        numbers_tuple = tuple(map(int, numbers))
        number_list.append(numbers_tuple)
    
    return number_list


def part_one(data_input):
    total = 0

    button_prize_numbers = parse_input(data_input)
    for game in button_prize_numbers:
        result = find_prize(game)
        total += result

    return total


def part_two(data_input):
    total = 0

    button_prize_numbers = parse_input(data_input)
    for game in button_prize_numbers:
        result = find_prize_part_2(game)
        total += result
    
    return total


if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(13, 2024)

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
