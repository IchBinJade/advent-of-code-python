"""
Author: IchBinJade
Date  : 2025-01-02
AoC 2015 Day 19 - https://adventofcode.com/2015/day/19

More string manipulation; "atom" and "molecule" calibration/fabrication
"""

import sys
import os
import time
import re

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file

REPLACEMENT_STR = r"(\w+) => (\w+)"

def perform_calibration(replacements, original):
    molecules = set()
    for atom1, atom2 in replacements:
        for idx in range(len(original)):
            if original[idx: idx + len(atom1)] == atom1:
                new = original[:idx] + atom2 + original[idx + len(atom1):]
                molecules.add(new)
    
    return molecules


def reverse_replacements(replacements):
    rr = []
    for (atom1, atom2) in replacements:
        rr.append((atom2, atom1))
        
    return rr


def perform_fabrication(original, replacements):
    steps = 0
    orig = original

    while orig != "e":
        replaced = False
        
        for source, replacement in replacements:
            if replacement in orig:
                orig = orig.replace(replacement, source, 1)  # Apply the first replacement
                steps += 1
                replaced = True
                break  # Break to ensure only one replacement is made in each iteration

        if not replaced:
            break  # Exit if no replacement was applied
    
    return steps


def part_one(data_input):
    replacements = []
    for line in data_input[:-2]:
        match = re.findall(REPLACEMENT_STR, line)
        replacements.append(match[0])
    
    original_molecule = data_input[-1]
    
    unique_molecules = perform_calibration(replacements, original_molecule)
    
    return len(unique_molecules)


def part_two(data_input):
    replacements = []
    for line in data_input[:-2]:
        match = re.findall(REPLACEMENT_STR, line)
        replacements.append(match[0])
    
    original_molecule = data_input[-1]
    
    steps = perform_fabrication(original_molecule, replacements)
    
    return steps


if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(19, 2015)

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
