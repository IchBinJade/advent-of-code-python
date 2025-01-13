"""
Author: IchBinJade
Date  : 2025-01-13
AoC 2016 Day 14 - https://adventofcode.com/2016/day/14

MD5 hashing; part two involves key stretching
"""

import sys
import os
import time
import re
import hashlib

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file

TRIPLE_STR = r"(.)\1\1"


def do_hash(salt, idx):
    hash_str = salt + str(idx)
    result = hashlib.md5(hash_str.encode())
    result_str = result.hexdigest()
    
    return result_str


def find_quintuplet(hash_list, char):  
    quintuple = char * 5
    for hash in hash_list:
        if hash.find(quintuple) != -1:
            return True
            
    return False


def do_stretched_hash(salt, num):
    result = do_hash(salt, num)
    for _ in range(2016):
        result = hashlib.md5(result.encode()).hexdigest()
        
    return result


def find_pad_key(salt, P2=False):
    triples = re.compile(TRIPLE_STR)
    if P2:
        hash_list = [do_stretched_hash(salt, num) for num in range(1001)]
    else:
        hash_list = [do_hash(salt, num) for num in range(1001)]
    
    idx = 0
    key_cnt = 0

    while True:
        hash = triples.search(hash_list.pop(0))
        if hash:
            char = hash.group(1)
        
            if find_quintuplet(hash_list, char):
                key_cnt += 1
                
        if key_cnt >= 64:
            break

        idx += 1

        if P2:
            hash_list.append(do_stretched_hash(salt, idx + len(hash_list)))
        else:
            hash_list.append(do_hash(salt, idx + len(hash_list)))
        
    return idx
    

def part_one(data_input):
    salt = data_input[0]
    pad_index = find_pad_key(salt)
    return pad_index


def part_two(data_input):
    salt = data_input[0]
    pad_index = find_pad_key(salt, P2=True)
    return pad_index


if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(14, 2016)

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
