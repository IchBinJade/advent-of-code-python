"""
Author: IchBinJade
Date  : 2025-01-01
AoC 2015 Day 13 - https://adventofcode.com/2015/day/13

Generate optimal seating with itertools.permutations()
"""

import sys
import os
import time
import re

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file
from itertools import permutations


def parse_input(data, add_me=False):
    people = set()
    happiness = {}
    for line in data:
        name1, name2 = line.split()[0].strip("."), line.split()[-1].strip(".")
        if "gain" in line:
            num = int(re.findall(r"\d+", line)[0])
        else:
            num = -int(re.findall(r"\d+", line)[0])

        people.update([name1, name2])
        happiness[(name1, name2)] = num

    if add_me:
        for person in people:
            happiness[("me", person)] = 0
            happiness[(person, "me")] = 0
        people.add("me")
        
    unique_names = list(people)
    
    return unique_names, happiness


def calc_seating(potential_seating, happiness):
    optimal = 0
    for seating in potential_seating:
        total = 0
        for idx in range(len(seating)):
            right = (idx + 1) % len(seating)
            total += happiness[(seating[idx], seating[right])]
            total += happiness[(seating[right], seating[idx])]
        
        optimal = max(optimal, total)
    
    return optimal


def part_one(data_input):
    unique_names, happiness = parse_input(data_input)

    potential_seating = permutations(unique_names)
    
    optimal_seating = calc_seating(potential_seating, happiness)
    
    return optimal_seating


def part_two(data_input):
    unique_names, happiness = parse_input(data_input, True)

    potential_seating = permutations(unique_names)
    
    optimal_seating = calc_seating(potential_seating, happiness)
    
    return optimal_seating


if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(13, 2015)

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
