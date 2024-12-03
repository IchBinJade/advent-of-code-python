"""
Author: IchBinJade
Date  : 2024-11-26
AoC Day 4 - https://adventofcode.com/2023/day/4
"""

import sys
import os
import time
import re

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file

def parse_card(line):
    card_re = r"Card\s+\d+:\s+([\d\s]+)\s+\|\s+([\d\s]+)"
    match = re.search(card_re, line)

    if match:
        # Extract winning and chosen numbers as str, then split & convert to int
        winning_numbers = list(map(int, match[1].strip().split()))
        chosen_numbers = list(map(int, match[2].strip().split()))
        return {"winning_numbers": winning_numbers, "chosen_numbers": chosen_numbers}
    else:
        return None


def calc_matches(card_line):
    winning_numbers = card_line["winning_numbers"]
    chosen_numbers = card_line["chosen_numbers"]
    card_match = 0
    
    # Create sets and find intersection
    winning_set = set(winning_numbers)
    chosen_set = set(chosen_numbers)
    real_set = winning_set.intersection(chosen_set)
    card_match = len(real_set)

    return card_match


def part_one(input):
    total = 0
    for line in input:
        card = parse_card(line)
        if card:
            card_points = 0
            matches = calc_matches(card)
            for _ in range(matches):
                card_points = 1 if card_points == 0 else card_points * 2
            total += card_points

    return total


def part_two(data):
    total = 0

    # Initialise a dict of card refs and their copy count
    card_copies = {c_id + 1: 1 for c_id, _ in enumerate(data)}

    # Loop input, find matches, loop copies and increment next refs
    for card_idx, line in enumerate(data):
        card_ref = card_idx + 1
        card = parse_card(line)
        if card:
            matches = calc_matches(card)
            no_of_copies = card_copies[card_ref]
            for copy in range(no_of_copies):
                for next_ref in range(card_ref + 1, card_ref + 1 + matches):
                    if next_ref <= len(data): # Don't exceed input bounds
                        card_copies[next_ref] += 1
    
    return sum(card_copies.values())


if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(4, 2023)

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
