"""
Author: IchBinJade
Date  : 2022-12-16
AoC Day 2 - https://adventofcode.com/2022/day/2
"""

import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file

def part_one(input):
    # What would your total score be if everything goes exactly according to your strategy guide?
    combos = {"A Y":8, "A X":4, "A Z":3, "B Y":5, "B X":1, "B Z":9, "C Y":2, "C X":7, "C Z":6}
    total_score = 0
    for play in input:
        total_score += combos[play]

    return total_score


def part_two(input):
    # What's the revised total score
    combos = {"A Y":4, "A X":3, "A Z":8, "B Y":5, "B X":1, "B Z":9, "C Y":6, "C X":2, "C Z":7}
    total_score = 0
    for play in input:
        total_score += combos[play]

    return total_score



if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(2, 2022)

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")