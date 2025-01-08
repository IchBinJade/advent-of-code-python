"""
Author: IchBinJade
Date  : 2025-01-08
AoC 2016 Day 4 - https://adventofcode.com/2016/day/4

Part 2 implements a caesar cipher decryption algorithm - fun times!
"""

import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file
from collections import Counter


def caesar_decrypt(encrypted_name, sector):
    decrypted_name = ""
    alpha = "abcdefghijklmnopqrstuvwxyz"
    
    for char in encrypted_name:
        if char in alpha:
            pos = alpha.find(char)
            new_pos = (pos + sector) % 26
            new_char = alpha[new_pos]
            decrypted_name += new_char
        elif char == "-":
            decrypted_name += " "
    
    return decrypted_name


def part_one(data_input):
    total = 0
    
    for line in data_input:
        e_name, csum = line.split("[")
        encrypted_name, sector_id = "-".join(e_name.split("-")[0:-1]), e_name.split("-")[-1]
        checksum = csum.strip("]")
        
        letter_counts = Counter(char for char in encrypted_name if char != "-")
        sorted_letter_count = sorted(letter_counts.items(), key=lambda x: (-x[1], x[0]))
        sorted_checksum = "".join([x[0] for x in sorted_letter_count[:5]])

        if sorted_checksum == checksum:
            total += int(sector_id)
        
    return total


def part_two(data_input):
    """Implementing a caesar cipher decryption - https://www.scaler.com/topics/caesar-cipher-python/"""
    
    for line in data_input:
        e_name, _ = line.split("[")
        encrypted_name, sector_id = "-".join(e_name.split("-")[0:-1]), int(e_name.split("-")[-1])
        
        decrypted_name = caesar_decrypt(encrypted_name, sector_id)
        
        if "north" in decrypted_name:
            return sector_id
    
    return None


if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(4, 2016)

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
