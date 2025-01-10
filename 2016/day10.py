"""
Author: IchBinJade
Date  : 2025-01-10
AoC 2016 Day 10 - https://adventofcode.com/2016/day/10

Simulation based iterative solution using dict of arrays to track/store bot state/chips
"""

import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file


def parse_input(instructions):
    bots = {}
    for line in instructions:
        if line.startswith("value"):
            instruction = line.split()
            try:
                bots[int(instruction[-1])].append(int(instruction[1]))
            except KeyError:
                bots[int(instruction[-1])] = [int(instruction[1])]
    
    return bots


def move_microchips(bots, instructions, P2=False):
    output = {}
    changed = True
    
    while changed:
        changed = False
        for instruction in instructions:
            if instruction.startswith("bot"):
                instruction = instruction.split()

                bot = int(instruction[1])
                lo_bot, hi_bot = int(instruction[6]), int(instruction[-1])
                
                if bot in bots.keys() and len(bots[bot]) >= 2:
                    changed = True
                    if instruction[5] == "bot":
                        if lo_bot in bots.keys():
                            bots[lo_bot].append(min(bots[bot]))
                        else:
                            bots[lo_bot] = [min(bots[bot])]
                    else:
                        if lo_bot in output.keys():
                            output[lo_bot].append(min(bots[bot]))
                        else:
                            output[lo_bot] = [min(bots[bot])]
                    
                    if instruction[-2] == "bot":
                        if hi_bot in bots.keys():
                            bots[hi_bot].append(max(bots[bot]))
                        else:
                            bots[hi_bot] = [max(bots[bot])]
                    else:
                        if hi_bot in output.keys():
                            output[hi_bot].append(max(bots[bot]))
                        else:
                            output[hi_bot] = [max(bots[bot])]
                    
                    bots[bot] = []
                    
                for check_bot in bots:
                    if 17 in bots[check_bot] and 61 in bots[check_bot] and not P2:
                        return check_bot
    
    return output


def part_one(data_input):
    bots = parse_input(data_input)
    
    bot_id = move_microchips(bots, data_input)
    
    return bot_id


def part_two(data_input):
    bots = parse_input(data_input)
    
    output = move_microchips(bots, data_input, P2=True)
    
    total = output[0][0] * output[1][0] * output[2][0]
    
    return total


if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(10, 2016)

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
