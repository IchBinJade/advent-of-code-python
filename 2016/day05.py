"""
Author: IchBinJade
Date  : 2025-01-08
AoC 2016 Day 5 - https://adventofcode.com/2016/day/5

MD5/hexdigest usage from hashlib
"""

import sys
import os
import time
import hashlib

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file


def do_hash(door_str, password, P2=False):
    result = hashlib.md5(door_str.encode())
    result_hex = result.hexdigest()
    if result_hex[:5] == "00000":
        if P2:
            pos = int(result_hex[5], 16)
            char = result_hex[6]
            if 0 <= pos < 8 and password[pos] is None:
                password[pos] = char
        else:
            password += result_hex[5]
        
    return password


def part_one(data_input):
    door_id = data_input[0]
    password = ""
    num = 0
    
    while len(password) < 8:
        door_str = door_id + str(num)
        password = do_hash(door_str, password)
            
        num += 1
        
    return password


def part_two(data_input):
    door_id = data_input[0]
    password = [None] * 8
    num = 0

    while True:
        door_str = door_id + str(num)
        password = do_hash(door_str, password, P2=True)
        
        if password.count(None) == 0:
            break
            
        num += 1
        
    return "".join(password)


if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(5, 2016)

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
