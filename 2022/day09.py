"""
Author: IchBinJade
Date  : 2024-12-28
AoC 2022 Day 9 - https://adventofcode.com/2022/day/9

Moving nodes on a dynamic graph
"""

import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file


def do_movements(input_str, knots):
    visited = set([(0, 0)])
    chain = [[0, 0] for _ in range(knots)]
    
    for line in input_str.split(","):
        direction, d_len = line.split()
        d_len = int(d_len)

        dx = 1 if direction == "R" else -1 if direction == "L" else 0
        dy = 1 if direction == "U" else -1 if direction == "D" else 0

        for _ in range(d_len):
            # Move Head
            chain[0][0] += dx
            chain[0][1] += dy
            for i in range(1, knots):
                prev_node = chain[i - 1]
                curr_node = chain[i]
                
                # Calc diff between nodes
                diff_x = prev_node[0] - curr_node[0]
                diff_y = prev_node[1] - curr_node[1]
                
                if abs(diff_x) > 1 or abs(diff_y) > 1:
                    if diff_x == 0:  # Head is vertically aligned with the tail
                        curr_node[1] += diff_y // 2  # Move the tail up or down
                    elif diff_y == 0:  # Head is horizontally aligned with the tail
                        curr_node[0] += diff_x // 2  # Move the tail left or right
                    else:  # Head is diagonally displaced from the tail
                        curr_node[0] += 1 if diff_x > 0 else -1  # Move the tail left or right
                        curr_node[1] += 1 if diff_y > 0 else -1  # Move the tail up or down
                
                if i == knots - 1:
                    visited.add(tuple(curr_node))
    
    return visited


def part_one(data_input):
    input_str = ",".join(data_input)

    visited = do_movements(input_str, 2)
    
    return len(visited)


def part_two(data_input):
    input_str = ",".join(data_input)
    
    visited = do_movements(input_str, 10)
    
    return len(visited)


if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(9, 2022)

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
