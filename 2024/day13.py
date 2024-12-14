"""
Author: IchBinJade
Date  : 2024-12-14
AoC 2024 Day 13 - https://adventofcode.com/2024/day/13

TODO: Start and solve part 2
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
            # Check if new position matches prize position
            if new_x == px and new_y == py:
                total_cost = 3 * a_press + b_press
                min_tokens = min(min_tokens, total_cost)
                
    if min_tokens == float('inf'):
        return 0
    
    return min_tokens


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
    #print(data_input)
    button_prize_numbers = parse_input(data_input)
    #print(f"button_prize_numbers >>> {button_prize_numbers}")
    for game in button_prize_numbers:
        result = find_prize(game)
        total += result
        #print(f"result >>> {result}")

    return total


def part_two(data_input):
    pass


TEST_INPUT = ['Button A: X+94, Y+34', 'Button B: X+22, Y+67', 'Prize: X=8400, Y=5400', '', 'Button A: X+26, Y+66', 'Button B: X+67, Y+21', 'Prize: X=12748, Y=12176', '', 'Button A: X+17, Y+86', 'Button B: X+84, Y+37', 'Prize: X=7870, Y=6450', '', 'Button A: X+69, Y+23', 'Button B: X+27, Y+71', 'Prize: X=18641, Y=10279']

if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(13, 2024)
    
    #input_data = TEST_INPUT

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
