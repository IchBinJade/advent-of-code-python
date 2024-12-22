"""
Author: IchBinJade
Date  : 2024-12-22
AoC 2024 Day 22 - https://adventofcode.com/2024/day/22

Utilises: Iterative number transformation
"""

import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file

def calc_new_secret(num):
    # Multiply by 64 then get bitwise xor and prune
    num = (num ^ (num * 64)) % 16777216
    # divide by 32, round down, then get bitwise xor and prune
    num = (num ^ (num // 32)) % 16777216
    # multuple by 2048, get bitwise xor and prune
    num = (num ^ (num * 2048)) % 16777216
    
    return num


def part_one(data_input):
    new_nums = []
    for secret in data_input:
        new_num = int(secret)

        for _ in range(2000):
            new_num =  calc_new_secret(new_num)
        new_nums.append(new_num)
          
    return sum(new_nums)


def part_two(data_input):
    banana_seq_totals = {}
    for secret in data_input:
        new_num = int(secret)
        buyer = [new_num % 10]
        
        for _ in range(2000):
            new_num = calc_new_secret(new_num)
            buyer.append(new_num % 10)
            
        # Check all possible sequences of the 4 price changes
        seen = set()
        for idx in range(len(buyer) - 4):
            diff1, diff2, diff3, diff4, diff5 = buyer[idx: idx + 5]
            sequence = (diff2 - diff1, diff3 - diff2, diff4 - diff3, diff5 - diff4)
            if sequence not in seen:
                seen.add(sequence)
                if sequence not in banana_seq_totals:
                    banana_seq_totals[sequence] = 0
                
                banana_seq_totals[sequence] += diff5
        
    return max(banana_seq_totals.values())


if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(22, 2024)

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
