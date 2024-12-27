"""
Author: IchBinJade
Date  : 2024-11-24
AoC 2021 Day 3 - https://adventofcode.com/2021/day/3

Utilises: Bitwise arithmetic

2024-12-27: Solved part 2
"""

import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file
from collections import Counter


def get_ratings(data_input, support_type):
    remaining_data = data_input
    bit_pos = 0
    
    while len(remaining_data) > 1:
        count = Counter(row[bit_pos] for row in remaining_data)
        if support_type == "oxygen":
            most_common = "1" if count["1"] >= count["0"] else "0"
        elif support_type == "co2":
            most_common = "0" if count["0"] <= count["1"] else "1"

        # Filter based on bit criteria
        remaining_data = [row for row in remaining_data if row[bit_pos] == most_common]
        bit_pos += 1
    
    return int(remaining_data[0], 2)


def part_one(data_input):
    gamma_bin = []
    epsilon_bin = []
    for col in range(len(data_input[0])):
        col_digits = [int(row[col]) for row in data_input]
        # Count occurrences and find most frequent
        count = Counter(col_digits)
        most_freq = count.most_common(1)[0][0]
        least_freq = count.most_common()[-1][0]
        gamma_bin.append(str(most_freq))
        epsilon_bin.append(str(least_freq))
    
    gamma = int("".join(gamma_bin), 2)
    epsilon = int("".join(epsilon_bin), 2)

    return gamma * epsilon


def part_two(data_input):
    oxygen_rating = get_ratings(data_input, "oxygen")
    co2_rating = get_ratings(data_input, "co2")
    
    return oxygen_rating * co2_rating


if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(3, 2021)

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
