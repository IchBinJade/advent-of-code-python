"""
Author: IchBinJade
Date  : 2025-01-01
AoC 2015 Day 9 - https://adventofcode.com/2015/day/9

Calculate distances between towns utilising itertools.permutations()
"""

import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file
from itertools import permutations


def calc_distances(potential_routes, routes_dict):
    distances = []
    for route in potential_routes:
        total_dist = 0
        for i in range(len(route) - 1):
            town1 = route[i]
            town2 = route[i + 1]
            total_dist += routes_dict[town1][town2]

        distances.append(total_dist)
    
    return distances


def part_one(data_input):
    routes = {}
    unique_towns = set()
    for line in data_input:
        town1, town2, dist = line.split()[0], line.split()[2], line.split()[4]
        unique_towns.add(town1)
        unique_towns.add(town2)
        if town1 not in routes:
            routes[town1] = {}
        if town2 not in routes:
            routes[town2] = {}
        routes[town1][town2] = int(dist)
        routes[town2][town1] = int(dist)

    unique_towns = list(unique_towns)
    
    potential_routes = permutations(unique_towns)
    
    distances = calc_distances(potential_routes, routes)
    
    return min(distances)


def part_two(data_input):
    routes = {}
    unique_towns = set()
    for line in data_input:
        town1, town2, dist = line.split()[0], line.split()[2], line.split()[4]
        unique_towns.add(town1)
        unique_towns.add(town2)
        if town1 not in routes:
            routes[town1] = {}
        if town2 not in routes:
            routes[town2] = {}
        routes[town1][town2] = int(dist)
        routes[town2][town1] = int(dist)

    unique_towns = list(unique_towns)
    
    potential_routes = permutations(unique_towns)
    
    distances = calc_distances(potential_routes, routes)
    
    return max(distances)


if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(9, 2015)

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
