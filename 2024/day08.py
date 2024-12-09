"""
Author: IchBinJade
Date  : 2024-12-08
AoC 2024 Day 8 - https://adventofcode.com/2024/day/8
"""

import sys
import os
import time
import re

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file
from itertools import combinations

def get_antenna_coords(grid):
    antenna_coords = {}
    for row_idx, row in enumerate(grid):
        for match in re.finditer(r"[a-zA-Z0-9]", "".join(row)):
            antenna = match.group()
            col_idx = match.start()
            if antenna not in antenna_coords:
                antenna_coords[antenna] = []
            antenna_coords[antenna].append((row_idx, col_idx))
    
    return antenna_coords


def part_one(data_input):
    count = 0
    grid = [list(row) for row in data_input]
    antinodes = set()
    
    # Get a dict of the antenna and their locations
    """ 
    {"A": [(0, 2), (3, 4)], "0": [(6, 1)]}
    """
    antennas_dict = get_antenna_coords(grid)
    #print(f"antennas_dict >>> {antennas_dict}")
    # For each pair in antenna_map.values(), using combinations, set the antinodes if within bounds
    for antenna_array in antennas_dict.values():
        for first_coord, second_coord in combinations(antenna_array, 2):
            #print(f"first_coord >>> {first_coord}")
            #print(f"second_coord >>> {second_coord}")
            # Calc antinode (an) one and two's row/col
            an_one_row, an_one_col = first_coord            
            an_two_row, an_two_col = second_coord
            
            antinode_one = (2 * an_one_row - an_two_row, 2 * an_one_col - an_two_col)
            antinode_two = (2 * an_two_row - an_one_row, 2 * an_two_col - an_one_col)

            # Bounds check
            if 0 <= antinode_one[0] < len(grid) and 0 <= antinode_one[1] < len(grid[0]):
                antinodes.add(antinode_one)
            if 0 <= antinode_two[0] < len(grid) and 0 <= antinode_two[1] < len(grid[0]):
                antinodes.add(antinode_two)
    #print(f"antinodes >>> {antinodes}")
    #count = len([0 for row, col in antinode_list if 0 <= row < len(grid) and 0 <= col < len(grid[0])]) // 2
    count = len(antinodes)
    # for array in antennas_dict.values():
    #     for i in range(len(array)):
    #         for j in range(i + 1, len(array)):
    #             r1, c1 = array[i]
    #             r2, c2 = array[j]
    #             antinodes.add((2 * r1 - r2, 2 * c1 - c2))
    #             antinodes.add((2 * r2 - r1, 2 * c2 - c1))

    # print(len([0 for r, c in antinodes if 0 <= r < len(grid) and 0 <= c < len(grid[0])]))
    
    return count


def part_two(data_input):
    count = 0
   
    
    return count


TEST_INPUT = ['............', '........0...', '.....0......', '.......0....', '....0.......', '......A.....', '............', '............', '........A...', '.........A..', '............', '............']


if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(8, 2024)
    
    #input_data = TEST_INPUT

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
