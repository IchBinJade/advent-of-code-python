"""
Author: IchBinJade
Date  : 2024-12-30
AoC 2022 Day 11 - https://adventofcode.com/2022/day/11

Simulate Monkey in the Middle with OOP. Part 2 involves LCM
(Least Common Multiple) and modular arithmetic

(Really, really enjoyed this one! "Maths is fun" - Ms S. Mason)
"""

import sys
import os
import time
import re
import math

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file
from collections import deque

class Monkey:
    def __init__(self, id, start_items, instruction, test, if_true, if_false):
        self.id = id
        self.start_items = start_items
        self.instruction = instruction
        self.test_int = test
        self.true_throw = if_true
        self.false_throw = if_false
        self.items = deque(start_items)
        self.inspection_count = 0
        
        # Precompute instruction
        op_type, value = self.instruction.split(" ")
        self.op_type = op_type
        self.op_value = int(value) if value.isdigit() else None
        
    def __repr__(self):
        return print(f"Monkey {self.id}: Starting items: {self.start_items}, "
                    f"Operation: {self.instruction}, Test: {self.test_int}, "
                    f"If true: throw to {self.true_throw}, If false: throw to {self.false_throw}")
        
    def inspect(self, item):
        """Inspect item and perform instruction"""
        if self.op_type == "*":
            return item * (self.op_value if self.op_value is not None else item)
        elif self.op_type == "+":
            return item + (self.op_value if self.op_value is not None else item)
        
        return item
    
    def do_test(self, item):
        return item % self.test_int == 0
    
    def do_throw(self, item, monkeys):
        """Which monkey ID are we throwing to based on the test"""
        target = self.true_throw if self.do_test(item) else self.false_throw
        
        # Throw it
        monkeys[target].items.append(item)
        
    def inspect_and_throw(self, monkeys, P2=False):
        while self.items:
            item = self.items.popleft()
            self.inspection_count += 1
            # Perform instruction then "manage" worry
            new_item = self.inspect(item)
            if not P2:
                new_item = new_item // 3
            else:
                new_item = new_item % P2 # Track worry mod LCM
            
            self.do_throw(new_item, monkeys)
    

def create_monkey(data):
    # Helper function to create Monkey object
    monkey_id = int(re.search(r"Monkey (\d+):", data[0]).group(1))
    starting_items = list(map(int, re.search(r"Starting items: (.+)", data[1]).group(1).split(", ")))
    operation = re.search(r"Operation: new = old (.+)", data[2]).group(1)
    test = int(re.search(r"Test: divisible by (\d+)", data[3]).group(1))
    if_true = int(re.search(r"If true: throw to monkey (\d+)", data[4]).group(1))
    if_false = int(re.search(r"If false: throw to monkey (\d+)", data[5]).group(1))
    
    return Monkey(monkey_id, starting_items, operation, test, if_true, if_false)


def parse_input(data):
    monkeys = {}
    monkey_data = []
    for line in data:
        if line == "":
            if monkey_data:
                new_monkey = create_monkey(monkey_data)
                monkeys[new_monkey.id] = new_monkey
                monkey_data = []
        else:
            monkey_data.append(line.strip())
            
    # Handle the last monkey
    if monkey_data:
        new_monkey = create_monkey(monkey_data)
        monkeys[new_monkey.id] = new_monkey
        
    return monkeys


def get_lcms(monkeys):
    """Get the LCM of all the test values"""
    lcm = 1
    for monkey in monkeys.values():
        lcm = lcm * monkey.test_int // math.gcd(lcm, monkey.test_int)
        
    return lcm


def simulate_rounds(monkeys, rounds, P2):
    for _ in range(rounds):
        for _, monkey in monkeys.items():
            monkey.inspect_and_throw(monkeys, P2)


def part_one(data_input):
    monkeys_dict = parse_input(data_input)

    simulate_rounds(monkeys_dict, 20, False)
    sorted_monkeys = sorted(monkeys_dict.values(), key=lambda x: x.inspection_count, reverse=True)
    
    first_active = sorted_monkeys[0].inspection_count
    second_active = sorted_monkeys[1].inspection_count
        
    return first_active * second_active


def part_two(data_input):
    monkeys_dict = parse_input(data_input)

    # Calc LCM of divisors
    mod = get_lcms(monkeys_dict)
    
    simulate_rounds(monkeys_dict, 10000, mod)
    sorted_monkeys = sorted(monkeys_dict.values(), key=lambda x: x.inspection_count, reverse=True)
    
    first_active = sorted_monkeys[0].inspection_count
    second_active = sorted_monkeys[1].inspection_count
        
    return first_active * second_active


if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(11, 2022)

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
