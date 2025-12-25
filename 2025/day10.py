"""
Author: IchBinJade
Date  : 2025-12-23
AoC 2025 Day 10 - https://adventofcode.com/2025/day/10

Thanks again to @HyperNeutrino for making me realise it was
ok to bite the bullet and learn about Z3!
"""

import sys
import os
import time
import re
import z3

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file
from collections import deque


class SingleLight:
    def __init__(self, target):
        self.target_is_on = (target == "#")
        self.current_is_on = False # Default's "off"
        
    def toggle(self):
        self.current_is_on = not self.current_is_on
        
    def is_matching(self):
        return self.current_is_on == self.target_is_on

class LightRow:
    def __init__(self, diagram_str, buttons, joltage):
        self.lights = [SingleLight(char) for char in diagram_str]
        self.buttons = buttons # list of lists
        self.joltage = joltage
        
    def press_button(self, button_idx):
        idx_to_flip = self.buttons[button_idx]
        for idx in idx_to_flip:
            self.lights[idx].toggle()
    
    def does_it_match(self):
        return all(l.is_matching() for l in self.lights)
    
    def find_smallest_count_of_presses(self):
        target_state = tuple(l.target_is_on for l in self.lights)
        init_state =  tuple(False for _ in self.lights)
        queue = deque([(init_state, 0)])
        visited = {init_state}
        while queue:
            current_state, count = queue.popleft()
            if current_state == target_state:
                return count
            
            for button in self.buttons:
                new_state_list = list(current_state)
                for idx in button:
                    new_state_list[idx] = not new_state_list[idx]
                new_state = tuple(new_state_list)
                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, count + 1))
        
        return -1
    
    def find_smallest_joltage_presses(self):
        optimizer = z3.Optimize()
        button_vars = [z3.Int(f"button_{i}") for i in range(len(self.buttons))]
        
        # Constraint: Can't have negative presses
        for var in button_vars:
            optimizer.add(var >= 0)
            
        # Match joltage requirements; build equations for each counter idx
        for idx, target in enumerate(self.joltage):
            equation = 0
            for button_idx, button_indices in enumerate(self.buttons):
                if idx in button_indices:
                    equation += button_vars[button_idx]
                    
            optimizer.add(equation == target)
            
        total_presses = sum(button_vars)
        optimizer.minimize(total_presses)
        
        if optimizer.check() == z3.sat:
            model = optimizer.model()
            return model.eval(total_presses).as_long()
        
        return -1


def parse_line(line):
    diagram = re.search(r'\[([.#]+)\]', line).group(1)
    
    # Extract all button groups
    button_strings = re.findall(r'\(([\d,]+)\)', line)
    buttons = [[int(n) for n in b.split(',')] for b in button_strings]
    
    # Extract joltage
    joltage_str = re.search(r'\{([\d,]+)\}', line).group(1)
    joltage = [int(n) for n in joltage_str.split(',')]
    
    return LightRow(diagram, buttons, joltage)


def part_one(data_input):
    lights = [parse_line(line) for line in data_input]

    total = 0
    for light in lights:
        smallest = light.find_smallest_count_of_presses()
        if smallest == -1:
            print("Something's gone wrong")
            break
        total += smallest
    
    return total


def part_two(data_input):
    lights = [parse_line(line) for line in data_input]
    
    total = 0
    for light in lights:
        smallest = light.find_smallest_joltage_presses()
        if smallest == -1:
            print("Something's gone wrong")
            break
        total += smallest
    
    return total



if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(10, 2025)

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
