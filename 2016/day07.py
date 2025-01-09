"""
Author: IchBinJade
Date  : 2025-01-09
AoC 2016 Day 7 - https://adventofcode.com/2016/day/7

Checking ABBA/ABA/BAB type sequences in lists of strings
"""

import sys
import os
import time
import re

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file

IP_STR = r"(\w+|\[.*?\])"


def contains_abba_seq(check_str):
    for i in range(len(check_str) - 3):
        if check_str[i] == check_str[i + 3] and check_str[i + 1] == check_str[i + 2] and check_str[i] != check_str[i + 1]:
            return True
        
    return False


def can_find_abba_seq(string_list):
    has_abba_inside = False
    has_abba_outside = False
    
    for check_str in string_list:
        if check_str.startswith("["):
            if contains_abba_seq(check_str[1:-1]):
                has_abba_inside = True
        else:
            if contains_abba_seq(check_str):
                has_abba_outside = True
                 
    if has_abba_outside and not has_abba_inside:
        return True
        
    return False


def contains_aba_seq(check_str):
    aba_seqs = []
    for i in range(len(check_str) - 2):
        if check_str[i] == check_str[i + 2] and check_str[i] != check_str[i + 1]:
            aba_seqs.append(check_str[i:i+3])
        
    return aba_seqs


def can_find_aba_seq(string_list):
    aba_outside = []
    bab_inside = []
    
    for check_str in string_list:
        if check_str.startswith("["):
            if contains_aba_seq(check_str[1:-1]):
                bab_inside.extend(contains_aba_seq(check_str[1:-1]))
        else:
            if contains_aba_seq(check_str):
                aba_outside.extend(contains_aba_seq(check_str))
                 
    for aba in aba_outside:
        linked_bab = aba[1] + aba[0] + aba[1]
        if linked_bab in bab_inside:
            return True
        
    return False


def part_one(data_input):
    # Find ABBA type sequences, only outside of brackets
    total = 0
    
    string_list = []
    for line in data_input:
        string_list.append(re.findall(IP_STR, line))
        
    for list_of_str in string_list:
        if can_find_abba_seq(list_of_str):
            total += 1
        
    return total


def part_two(data_input):
    # Find ABA type sequences with corresponding BAB sequences
    total = 0
    
    string_list = []
    for line in data_input:
        string_list.append(re.findall(IP_STR, line))
        
    for list_of_str in string_list:
        if can_find_aba_seq(list_of_str):
            total += 1
        
    return total


if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(7, 2016)

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
