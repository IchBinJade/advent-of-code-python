"""
Author: IchBinJade
Date  : 2025-12-01
AoC 2025 Day 1 - https://adventofcode.com/2025/day/1
"""

import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file


class Node:
    def __init__(self, value):
        self.idx = value
        self.next = None
        self.previous = None


class Dial:
    def __init__(self, start_value, size=100):
        self.start = start_value
        self.size = size
        self.head = Node(start_value)
        self.tail = None
        self.make_dial()
        self.set_head()
        
    def make_dial(self):
        self.head = None
        self.tail = None
        for idx in range(self.size):
            new_node = Node(idx)
            if not self.head:
                self.head = new_node
                self.tail = new_node
            else:
                self.tail.next = new_node
                new_node.previous = self.tail
                self.tail = new_node
                
        self.tail.next = self.head
        self.head.previous = self.tail
        
    def set_head(self):
        current =  self.head
        while True:
            if current.idx == self.start:
                self.head = current
                break
            
            current = current.next
            
            # Error catch
            if current == self.head:
                print(f"Errors: Start value {self.start} not found")
                
    def rotate_dial(self, direction, count):
        current = self.head
        
        if direction == "L":
            for _ in range(count):
                current = current.previous
        else:
            for _ in range(count):
                current = current.next
                
        self.head = current
        self.tail = self.head.previous
    
    def eval_zero_position(self):
        if self.head.idx == 0:
            return True
        return False
    
    def rotate_and_eval(self, direction, count):
        current = self.head
        zero_count = 0
        
        if direction == "L":
            for _ in range(count):
                current = current.previous
                if current.idx == 0:
                    zero_count += 1
        else:
            for _ in range(count):
                current = current.next
                if current.idx == 0:
                    zero_count += 1
                    
        self.head = current
        self.tail = self.head.previous
        
        return zero_count


def parse_instruction(instruction):
    direction = instruction[0]
    count = int(instruction[1:])
    
    return direction, count


def part_one(data_input):
    dial = Dial(50)
    
    no_of_directions = len(data_input)
    zero_count = 0
    
    for idx in range(no_of_directions):
        instruction = data_input[idx]
        direction, count = parse_instruction(instruction)
        dial.rotate_dial(direction, count)
        if dial.eval_zero_position():
            zero_count += 1
            
    return zero_count


def part_two(data_input):
    dial = Dial(50)
    
    no_of_directions = len(data_input)
    total_zero_count = 0
    
    for idx in range(no_of_directions):
        instruction = data_input[idx]
        direction, count = parse_instruction(instruction)
        total_zero_count += dial.rotate_and_eval(direction, count)
        
    return total_zero_count


if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(1, 2025)

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
