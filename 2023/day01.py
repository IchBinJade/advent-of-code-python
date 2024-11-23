"""
Author: IchBinJade
Date  : 2024-11-22
AoC Day 1 - https://adventofcode.com/2023/day/1
"""

import sys
import os
import time
import re

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file

def part_one(input):
    total = 0

    # Remove non-numeric characters
    for line in input:
        line = re.sub(r'\D', '', line)
        if len(line) > 0:
            first_digit = line[0]
            last_digit = line[-1] if len(line) > 0 else first_digit
            whole_num = first_digit + last_digit
            total += int(whole_num)

    return total


def part_two(input):
    total = 0
    
    # Setup a 'map' of number-word combos
    word_map = {
        "oneight": 18,
        "twone": 21,
        "eightwo": 82,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }

    for line in input:
        if len(line) > 0:
            # Replace words with corresponding numbers using the word_map
            for word, number in word_map.items():
                line = re.sub(rf'{word}', str(number), line)

            # Remove non-numeric characters after replacing words
            line = re.sub(r'\D', '', line)

            # Calculate total
            if len(line) > 0:
                first_digit = line[0]
                last_digit = line[-1] if len(line) > 0 else first_digit
                whole_num = first_digit + last_digit
                total += int(whole_num)

    return total



if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(1, 2023)

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
