"""
Author: IchBinJade
Date  : 2024-12-28
AoC 2016 Day 9 - https://adventofcode.com/2016/day/9

String manipulation and "decompression" through recursion
"""

import sys
import os
import time
import re

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file
from functools import cache

MASK = r"\((\d+)x(\d+)\)"


def decompress(input_str):
    idx = 0
    while idx < len(input_str):
        match = re.search(MASK, input_str[idx:])
        if not match:
            yield len(input_str[idx:])
            break
        
        leading_chars = input_str[idx: idx + match.start()]
        yield len(leading_chars)
        
        num_chars_to_take, num_to_repeat = map(int, match.groups())
        sub_str = input_str[idx + match.end(): idx + match.end() + num_chars_to_take]
        
        decomp_len = sum(decompress(sub_str)) if sub_str else 0
        yield decomp_len * num_to_repeat
        
        idx += match.end() + num_chars_to_take
    

def part_one(data_input):
    input_str = "".join(data_input)
    result = []
    idx = 0
    
    while idx < len(input_str):
        if input_str[idx] == "(":
            closing_p_idx = input_str.index(")", idx)
            instruction = input_str[idx + 1: closing_p_idx]
            num_chars_to_take, num_to_repeat = map(int, instruction.split("x"))
            sub_str = input_str[closing_p_idx + 1: closing_p_idx + 1 + num_chars_to_take]
            result.extend(sub_str * num_to_repeat)
            idx = closing_p_idx + 1 + num_chars_to_take
        else:
            result.extend(input_str[idx])
            idx += 1
    
    return len("".join(result))


def part_two(data_input):
    input_str = "".join(data_input)
    result = sum(decompress(input_str))

    return result


if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(9, 2016)

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
