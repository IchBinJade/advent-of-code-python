"""
Author: IchBinJade
Date  : 2025-01-01
AoC 2015 Day 10 - https://adventofcode.com/2015/day/10

Number-as-string manipulation/extending
"""

import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file


def look_and_say(input_str, process_count):
    for _ in range(process_count):
        new_str = ""
        count = 1
        for i in range(1, len(input_str)):
            if input_str[i] == input_str[i - 1]:
                count += 1
            else:
                new_str += f"{count}{input_str[i - 1]}"
                count = 1
        
        new_str += f"{count}{input_str[-1]}"
        input_str = new_str
        
    return input_str
    

def part_one(data_input):
    input_str = data_input[0]

    result = look_and_say(input_str, 40)
    
    return len(str(result))


def part_two(data_input):
    input_str = data_input[0]

    result = look_and_say(input_str, 50)
    
    return len(str(result))


if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(10, 2015)

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
