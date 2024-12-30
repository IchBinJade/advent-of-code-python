"""
Author: IchBinJade
Date  : 2024-12-30
AoC 2018 Day 5 - https://adventofcode.com/2018/day/5

Recursive string manipulation using stacks
"""

import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file

LETTERS = {
    1: "A, a", 2: "B, b", 3: "C, c", 4: "D, d", 5: "E, e", 6: "F, f", 7: "G, g", 8: "H, h", 
    9: "I, i", 10: "J, j", 11: "K, k", 12: "L, l", 13: "M, m", 14: "N, n", 15: "O, o", 16: "P, p", 
    17: "Q, q", 18: "R, r", 19: "S, s", 20: "T, t", 21: "U, u", 22: "V, v", 23: "W, w", 24: "X, x", 25: "Y, y", 26: "Z, z", }


def perform_reactions(polymers):    
    stack = []
    for char in polymers:
        if stack and ((char.islower() and stack[-1] == char.upper()) or (char.isupper()and stack[-1] == char.lower())):
            stack.pop()
        else:
            stack.append(char)
            
    return "".join(stack)


def part_one(data_input):
    input_str = "".join(data_input)

    reacted_str = perform_reactions(input_str)
    
    return len(reacted_str)


def part_two(data_input):
    input_str = "".join(data_input)
    reactions = []
    for letters_idx in range(1, 27):
        mod_str = input_str
        # Remove/replace A-Z or a-z then react
        for letter in range(2):
            mod_str = mod_str.replace(LETTERS[letters_idx].split(", ")[letter], "")
        reacted_str = perform_reactions(mod_str)
        reactions.append(reacted_str)
    
    return min([len(r_str) for r_str in reactions])


if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(5, 2018)

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
