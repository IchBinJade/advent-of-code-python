"""
Author: IchBinJade
Date  : 2025-01-19
AoC 2016 Day 19 - https://adventofcode.com/2016/day/19

Simulating a White Elephant party with a LinkedList structure for the Elf Circle

TODO: Progress and complete part 2
"""

import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file


class Elf:
    def __init__(self, value):
        self.idx = value
        self.next_elf = None
        self.no_of_presents = 1
        
        
class ElfCircle:
    def __init__(self, no_of_elves):
        self.head = None
        self.tail = None
        self.no_of_elves = no_of_elves
        self.make_circle(no_of_elves)
        
    def make_circle(self, no_of_elves):
        for idx in range(1, no_of_elves + 1):
            new_elf = Elf(idx)
            if not self.head:
                self.head = new_elf
                self.tail = new_elf
            else:
                self.tail.next_elf = new_elf
                self.tail = new_elf
                
        self.tail.next_elf = self.head
        
    def print_circle(self):
        curr = self.head
        while curr:
            print(f"Elf {curr.idx}: {curr.no_of_presents} presents")
            curr = curr.next_elf
            if curr == self.head:
                break
            
            
def steal_presents(circle: ElfCircle):
    current = circle.head
    while circle.no_of_elves > 1:
        elf_to_steal_from = current.next_elf
        
        current.next_elf = elf_to_steal_from.next_elf
        
        if elf_to_steal_from == circle.tail:
            circle.tail = current
            
        circle.no_of_elves -= 1
        
        current = current.next_elf
        
    return current.idx


def part_one(data_input):
    no_of_elves = int(data_input[0])

    circle = ElfCircle(no_of_elves)

    last_elf_standing = steal_presents(circle)
    
    return last_elf_standing


def part_two(data_input):
    no_of_elves = int(data_input[0])

    circle = ElfCircle(no_of_elves)

    
    
    return None

TEST_INPUT_1 = ['5']

if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(19, 2016)
    
    # input_data = TEST_INPUT_1

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
