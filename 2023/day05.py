"""
Author: IchBinJade
Date  : 2024-12-07
AoC 2023 Day 5 - https://adventofcode.com/2023/day/5

Thanks to @hyper-neutrino on YouTube for the explanation on overlaps
"""

import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file

def get_data_mappings(data_input):
    mapping_dict = {}
    curr_type = None
    curr_range = []
    
    for line in data_input:
        if line == "": continue  # Skip blank lines
        
        if "map:" in line:
            # If there's a current map, store it
            if curr_type:
                mapping_dict[curr_type] = curr_range
            
            # Extract the current map type and reset its range
            curr_type = line.replace(" map:", "")
            curr_range = []
        else:
            # Otherwise, append the data to the current map's range
            curr_range.extend([line.strip()])
            
    # Don't forget to add the last mapping at the end
    if curr_type:
        mapping_dict[curr_type] = curr_range

    return mapping_dict


def get_seed_mappings(seed, mappings):
    """ 
    For each seed, map the number through the different planting
    types and return the final location reference
    """
    final_location = 0
    mapping_ref = seed

    for map_ranges in mappings.values():
        for range_val in map_ranges:
            try:
                destination_start, source_start, range_length = map(int, range_val.split())
            except ValueError:
                print(f"Error splitting range_val {range_val} >>> {ValueError}")
                continue # skip this range

            # If the x-to-y number is within the range, assign destination mapping ref
            if source_start <= mapping_ref < source_start + range_length:
                mapping_ref = mapping_ref - source_start + destination_start
                break

    final_location = mapping_ref

    return final_location


def part_one(data_input):
    seeds = [int(seed) for seed in data_input[0].split()[1:] if seed.isdigit()]
    mappings = get_data_mappings(data_input)

    locations = []
    for seed in seeds:
        locations.append(get_seed_mappings(seed, mappings))    

    return min(locations)


def part_two(data_input):
    sections = "\n".join(data_input).split("\n\n")
    
    seeds = sections[0]
    seeds = list(map(int, seeds.split(":")[1].split()))
    mappings = sections[1:]

    intervals = []
    for idx in range(0, len(seeds), 2):
        intervals.append((seeds[idx], seeds[idx] + seeds[idx + 1]))     

    for type_block in mappings:
        ranges = []
        for line in type_block.splitlines()[1:]:
            ranges.append(list(map(int, line.split())))
        to_add =  []
        while len(intervals) > 0:
            seed_start, seed_end = intervals.pop()
            for i, j, k in ranges:
                overlap_start = max(seed_start, j)
                overlap_end = min(seed_end, j + k)
                if overlap_start < overlap_end:
                    # Append the transformation
                    to_add.append((overlap_start - j + i, overlap_end - j + i))
                    if overlap_start > seed_start:
                        intervals.append((seed_start, overlap_start))
                    if seed_end > overlap_end:
                        intervals.append((overlap_end, seed_end))
                    break
            else:
                to_add.append((seed_start, seed_end))
           
        intervals = to_add

    return (min(intervals)[0])



if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(5, 2023)

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
