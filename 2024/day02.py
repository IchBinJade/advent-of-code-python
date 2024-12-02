"""
Author: IchBinJade
Date  : 2024-12-02
AoC 2024 Day 2 - https://adventofcode.com/2024/day/2
"""

import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file

def line_is_safe(diffs, inc=True):
    if inc:
        return all(1 <= num <= 3 for num in diffs)
    else:
        return all(-3 <= num <= -1 for num in diffs)


def report_is_safe(data_line, dampener=False):
    all_inc = False
    all_dec = False

    # Get the diff list
    diffs = [int(curr) - int(prev) for curr, prev in zip(data_line.split(" "), data_line.split(" ")[1:]) if curr.isdigit() and prev.isdigit()]

    all_inc = line_is_safe(diffs, inc=True)
    all_dec = line_is_safe(diffs, inc=False)

    # Part 2 - Create and check sublists. If at least 1 is safe, in either direction, return true
    if not all_inc and not all_dec and dampener:
        line = data_line.split(" ")
        for i in range(len(line)):
            # Create a new data_line by removing the i-th value from the original data_list
            modified_data_line = line[:i] + line[i+1:]

            # Generate the new diffs based on the modified data_line
            modified_diffs = [int(curr) - int(prev) for curr, prev in zip(modified_data_line, modified_data_line[1:]) if curr.isdigit() and prev.isdigit()]

            # Check if this new modified sequence is valid
            if line_is_safe(modified_diffs, inc=True) or line_is_safe(modified_diffs, inc=False):
                all_inc = line_is_safe(modified_diffs, inc=True)
                all_dec = line_is_safe(modified_diffs, inc=False)
                break  # Exit if a valid sequence is found after removing one number
            else:
                # If no valid sequence is found after removing one number, mark as unsafe
                all_inc = False
                all_dec = False

    return all_inc, all_dec


def part_one(data_input):
    count = 0
    for line in data_input:
        all_inc, all_dec = report_is_safe(line)
        if all_inc or all_dec:
            count += 1

    return count


def part_two(data_input):
    count = 0
    dampener = True

    for idx, line in enumerate(data_input):
        all_inc, all_dec = report_is_safe(line, dampener)
        if all_inc or all_dec:
            count += 1

    return count


if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(2, 2024)

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
