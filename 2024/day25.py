"""
Author: IchBinJade
Date  : YYYY-MM-DD
AoC YYYY Day X - https://adventofcode.com/20YY/day/X
"""

import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file


def parse_input(data_input):
    locks = []
    keys = []
    
    # Change to a string before transposing grids
    input_str = "\n".join(data_input)
    # print(f"input_str = {input_str}")
    for line in input_str.split("\n\n"):
        grid = line.splitlines()
        # Ignore the first and last row (grid[1:-1]) by slicing the list
        middle_rows = grid[1:-1]
        transposed = list(zip(*middle_rows))
        # print(f"grid = {grid}")
        column_heights = tuple([sum(1 for x in column if x == "#") for column in transposed])
        if grid[0][0] == "#":
            # locks.append(tuple([column.count("#") for column in transposed]))
            locks.append(column_heights)
        else:
            # keys.append(tuple([column.count(".") for column in transposed]))
            keys.append(column_heights)
    
    return locks, keys

def part_one(data_input):
    # print(data_input)
    total = 0
    locks, keys = parse_input(data_input)
    # print(f"locks = {locks}")
    # print(f"keys = {keys}")
    for lock in locks:
        for key in keys:
            if all(x + y <= 5 for x, y in zip(lock, key)):
                total += 1  # Count the pair if no overlap exists
    
    return total


def part_two(data_input):
    pass

TEST_INPUT = ['#####', '.####', '.####', '.####', '.#.#.', '.#...', '.....', '', '#####', '##.##', '.#.##', '...##', '...#.', '...#.', '.....', '', '.....', '#....', '#....', '#...#', '#.#.#', '#.###', '#####', '', '.....', '.....', '#.#..', '###..', '###.#', '###.#', '#####', '', '.....', '.....', '.....', '#....', '#.#..', '#.#.#', '#####']

if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(25, 2024)
    
    # input_data = TEST_INPUT

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
