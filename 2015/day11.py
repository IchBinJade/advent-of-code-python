"""
Author: IchBinJade
Date  : 2025-01-01
AoC 2015 Day 11 - https://adventofcode.com/2015/day/11

String manipulation/generation with ord() and chr() functions
"""

import sys
import os
import time
import re

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file


def generate_next_string(curr_password):
    chars = list(curr_password)
    
    # Start from the last char
    i = len(chars) - 1
    while i >= 0:
        if chars[i] == "z":
            chars[i] = "a"
            i -= 1
        else:
            # "Increment" the character
            chars[i] = chr(ord(chars[i]) + 1)
            break
    
    return "".join(chars)


def has_straight(password):
    for i in range(len(password) - 2):
        if ord(password[i]) + 1 == ord(password[i + 1]) and ord(password[i + 1]) + 1 ==ord(password[i + 2]):
            return True
        
    return False


def meets_requirements(password):
    # Doesn't contain "i", "o" or "l"
    if any(char in password for char in "iol"):
        return False
    
    # Includes one increasing straight of min. 3 letters (abc, bcd, cde...)
    if not has_straight(password):
        return False
    
    # Contains at least 2 different non-overlapping pairs
    pairs = re.findall(r"(.)\1", password)
    pairs = set(pairs)
    if len(pairs) < 2:
        return False
    
    return True


def find_new_password(password, depth):
    for _ in range(depth):
        while True:
            # Iterate to next password
            new_password = generate_next_string(password)
            
            # Check if it's valid
            if meets_requirements(new_password):
                password = new_password
                break
            
            password = new_password
        
    return new_password
    

def part_one(data_input):
    curr_password = data_input[0]
    
    new_password = find_new_password(curr_password, 1)
    
    return new_password


def part_two(data_input):
    curr_password = data_input[0]
    
    new_password = find_new_password(curr_password, 2)
    
    return new_password


if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(11, 2015)

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
