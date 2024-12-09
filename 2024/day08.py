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
    """Generate a dictionary of antenna types and their coordinates.
    
    The dictionary maps each antenna type (a string) to a list of coordinates
    (tuples) where that antenna is located in the grid.
    
    Example:
        {"A": [(0, 2), (3, 4)], "0": [(6, 1)]}
    
    Args:
        grid (list[list[str]]): A 2D grid of ground (".") and antenna characters 
                                 (a-z, A-Z, 0-9) as strings.
    
    Returns:
        dict: A dictionary where keys are antenna types (str) and values are 
              lists of tuples, where each tuple represents the coordinates of 
              an antenna (row, col).
    """
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
    """ Solve Part 1 by generating a dictionary of antenna types and coordinates, then for
    each pair of coordinates calculate the position of the antinodes. Add these antinode 
    positions to a set (to avoid duplicates) and return the length of the set.
    
    Args:
        data_input (list[str]): A list of ground (".") and antenna characters 
                                (a-z, A-Z, 0-9) as strings.
                                
    Returns:
        int: Integer length of the set of antinodes
    """
    count = 0
    grid = [list(row) for row in data_input]
    antinodes = set()
    
    antennas_dict = get_antenna_coords(grid)

    for antenna_array in antennas_dict.values():
        for first_coord, second_coord in combinations(antenna_array, 2):
            an_one_row, an_one_col = first_coord            
            an_two_row, an_two_col = second_coord
            
            antinode_one = (2 * an_one_row - an_two_row, 2 * an_one_col - an_two_col)
            antinode_two = (2 * an_two_row - an_one_row, 2 * an_two_col - an_one_col)

            # Bounds check
            if 0 <= antinode_one[0] < len(grid) and 0 <= antinode_one[1] < len(grid[0]):
                antinodes.add(antinode_one)
            if 0 <= antinode_two[0] < len(grid) and 0 <= antinode_two[1] < len(grid[0]):
                antinodes.add(antinode_two)

    count = len(antinodes)
    
    return count


def part_two(data_input):
    """ Solve Part 2 by generating a dictionary of antenna types and coordinates, then for
    each pair of coordinates calculate the position of the first antinode. Trace the line 
    in both directions (from first to second antenna and vice versa) adding other anti-
    nodes within bounds
    
    
    Args:
        data_input (list[str]): A list of ground (".") and antenna characters 
                                (a-z, A-Z, 0-9) as strings.
                                
    Returns:
        int: Integer length of the set of antinodes
    """
    count = 0
    grid = [list(row) for row in data_input]
    antinodes = set()
    antennas_dict = get_antenna_coords(grid)
    
    for antenna_array in antennas_dict.values():
        for first_coord, second_coord in combinations(antenna_array, 2):
            an_one_row, an_one_col = first_coord            
            an_two_row, an_two_col = second_coord
           
            row_diff = an_one_row - an_two_row
            col_diff = an_one_col - an_two_col

            for start_coord, direction in [(first_coord, (row_diff, col_diff)), (second_coord, (-row_diff, -col_diff))]:
                loop_row, loop_col = start_coord
                while 0 <= loop_row < len(grid) and 0 <= loop_col < len(grid[0]):
                    antinodes.add((loop_row, loop_col))
                    loop_row += direction[0]
                    loop_col += direction[1]
                
    count = len(antinodes)
    
    return count


if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(8, 2024)

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
