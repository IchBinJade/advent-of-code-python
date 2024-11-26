"""
Author: IchBinJade
Date  : 2024-11-24
AoC 2021 Day 3 - https://adventofcode.com/2021/day/3
"""

import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file
from collections import Counter

def part_one(input):
    gamma_bin = []
    epsilon_bin = []
    for col in range(len(input[0])):
        col_digits = [int(row[col]) for row in input]
        # Count occurrences and find most frequent
        count = Counter(col_digits)
        most_freq = count.most_common(1)[0][0]
        least_freq = count.most_common()[-1][0]
        gamma_bin.append(str(most_freq))
        epsilon_bin.append(str(least_freq))
    
    gamma = int("".join(gamma_bin), 2)
    epsilon = int("".join(epsilon_bin), 2)

    return gamma * epsilon


def part_two(input):

    return None


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
