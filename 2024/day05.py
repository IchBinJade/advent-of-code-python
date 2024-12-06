"""
Author: IchBinJade
Date  : 2024-12-05
AoC 2024 Day 5 - https://adventofcode.com/2024/day/5

TODO: Complete part 2
"""

import sys
import os
import time
import itertools

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file

TEST_INPUT = ['47|53', '97|13', '97|61', '97|47', '75|29', '61|13', '75|53', '29|13', '97|29', '53|29', '61|53', '97|53', '61|29', '47|13', '75|47', '97|75', '47|61', '75|61', '47|29', '75|13', '53|13', '', '75,47,61,53,29', '97,61,53,29,13', '75,29,13', '75,97,47,61,53', '61,13,29', '97,13,75,29,47']

def is_order_valid(instruction, rules):
    """ 
    Check if the B page appears before the A page, in which case it isn't valid
    """
    for A, B in rules:
        if A in instruction and B in instruction:
            index_a = instruction.index(A)
            index_b = instruction.index(B)
            if index_b < index_a:
                return False
            
    return True


def find_valid_order(instruction, rules):
    """
    Try to find the valid order for the instruction using backtracking.
    """
    # Base case: If instruction is of length 1, it's trivially valid.
    if len(instruction) == 1:
        return instruction

    # Try placing each element in the order
    for i in range(len(instruction)):
        current_instruction = instruction[:i] + instruction[i+1:]  # Remove the element to try placing it later
        
        # Check if the rest of the instruction is valid
        if is_order_valid(current_instruction, rules):
            # Try placing the current element at the front
            ordered = find_valid_order(current_instruction, rules)
            if ordered is not None:
                return [instruction[i]] + ordered

    return None  # Return None if no valid ordering is found


def part_one(data_input):
    count = 0
    valid_instructions = []
    data_input = "\n".join(data_input)
    rules_input, instructions_input = data_input.split("\n\n", 1)
    rules = [(int(a), int(b)) for a, b in (line.split('|') for line in rules_input.splitlines())]
    
    # Loop the instructions and check validity
    for line in instructions_input.split("\n"):
        instruction = [int(page) for page in line.split(",")]
        if is_order_valid(instruction, rules):
            count += 1
            valid_instructions.append(line)
        
    return sum([int(instruction.split(",")[len(instruction.split(",")) // 2]) for instruction in valid_instructions])


def part_two(data_input):
    count = 0
    invalid_instructions = []
    data_input = "\n".join(data_input)
    rules_input, instructions_input = data_input.split("\n\n", 1)
    rules = [(int(a), int(b)) for a, b in (line.split('|') for line in rules_input.splitlines())]
    
    # Loop the instructions and check validity
    for line in instructions_input.split("\n"):
        instruction = [int(page) for page in line.split(",")]
        if not is_order_valid(instruction, rules):
            count += 1
            invalid_instructions.append(instruction)

    print(f"invalid_instructions >>> {invalid_instructions}")
 
    ordered_instructions = []
    for instruction in invalid_instructions:
        ordered_instruction = find_valid_order(instruction, rules)
        if ordered_instruction:
            ordered_instructions.append(ordered_instruction)

    print(f"ordered instructions >>> {ordered_instructions}")
    # Return the same sum as part_one but for invalid_instructions instead of valid_instructions
    return sum([instruction[len(instruction) // 2] for instruction in ordered_instructions])



if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(5, 2024)

    input_data = TEST_INPUT

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
