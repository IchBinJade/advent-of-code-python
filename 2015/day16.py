"""
Author: IchBinJade
Date  : 2025-01-02
AoC 2015 Day 16 - https://adventofcode.com/2015/day/16

Dictionary values comparison with regex for input parsing
"""

import sys
import os
import time
import re

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file

TICKET_TAPE = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1
}

THE_SUES = []

SUE_STRING = r"Sue \d+: (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)"


def parse_input(data_input):
    for line in data_input:
        match = re.match(SUE_STRING, line)
        key1, val1, key2, val2, key3, val3 = match.group(1, 2, 3, 4, 5, 6)
        val1, val2, val3 = int(val1), int(val2), int(val3)
        
        THE_SUES.append({key1: val1, key2: val2, key3: val3})
        
        
def find_sue_match(aunt):
    # P1: If all of the aunt's values match any of the ticker tape values, return true
    for key, val in aunt.items():
        if TICKET_TAPE[key] != val:
            return False
        
    return True


def p2_find_sue_match(aunt):
    # P2: Match ticker tape values but cats/trees must be > value and poms/goldfish < value
    for key, val in aunt.items():
        if key in ["cats", "trees"]:
            if TICKET_TAPE[key] >= val:
                return False
        elif key in ["pomeranians", "goldfish"]:
            if TICKET_TAPE[key] <= val:
                return False
        else:
            if TICKET_TAPE[key] != val:
                return False
    
    return True


def part_one(data_input):
    parse_input(data_input)
    
    aunts_matched = []
    for idx, aunt in enumerate(THE_SUES):
        if find_sue_match(aunt):
            aunts_matched.append(idx + 1)
            
    assert len(aunts_matched) == 1
    
    return aunts_matched[0]


def part_two(data_input):
    THE_SUES.clear()
    
    parse_input(data_input)
    
    aunts_matched = []
    for idx, aunt in enumerate(THE_SUES):
        if p2_find_sue_match(aunt):
            aunts_matched.append(idx + 1)

    assert len(aunts_matched) == 1
    
    return aunts_matched[0]


if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(16, 2015)

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
