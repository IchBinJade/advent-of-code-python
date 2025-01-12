"""
Author: IchBinJade
Date  : 2025-01-12
AoC 2016 Day 11 - https://adventofcode.com/2016/day/11

Move combinations of items across elevator floors and bfs shortest steps to get
all items on top floor. Uses State class

TODO: Refactor to include pruning and/or avoid deepcopy - current execution time 
for both parts is over 1 hour
"""

import sys
import os
import time
import re
import copy

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file
from collections import deque
from itertools import combinations

CHIP_STR = r"(\w+)-compatible microchip"
GEN_STR = r"(\w+) generator"


class State:
    visited = set()
    def __init__(self):
        """
        Initialise State with lift position and floor contents

        Args:
            lift_pos (int): Current floor (0-3)
            floors (list[set]): List of sets representing items on the floor
        """
        self.floors = {
            4: set(),
            3: set(),
            2: set(),
            1: set()
        }
        self.lift_floor = 1
        self.steps_taken = 0
        self.previous_state = None
        
    def __repr__(self):
        return f"{self.lift_floor}:{';'.join(','.join(sorted(self.floors[idx])) for idx in range(1, 5))}"
    
    def __str__(self):
        """
        Return a string representation of the state
        """
        return_str = f"State: Step #{self.steps_taken}"
        for idx in range(4, 0, -1):
            floor_label = f"F{idx}"
            lift_status = "E " if self.lift_floor == idx else ".|"
            floor_items = ", ".join(self.floors[idx])
            floor_str = f"{floor_label} {lift_status}{floor_items}"
            return_str += "\n" + floor_str
            
        return return_str
    
    def __eq__(self, other):
        return isinstance(other, State) and self.floors == other.floors and self.lift_floor == other.lift_floor
    
    def __hash__(self):
        return hash((self.lift_floor, tuple(sorted(self.floors.items()))))
    
    def is_valid_floor(self, floor_idx):
        floor_items = self.floors[floor_idx]
        generators = {item[:-1] for item in floor_items if item[-1] == "G"}
        microchips = {item[:-1] for item in floor_items if item[-1] == "M"}
        if len(generators) == 0:
            return True
        for chip in microchips:
            if chip not in generators:
                return False
            
        return True

    def is_valid_state(self):
        if all(self.is_valid_floor(floor_idx) for floor_idx in self.floors) and 0 < self.lift_floor < 5:
            return True
        
        return False
    
    def generate_new_states(self):
        previous_state = self.previous_state
        self.previous_state = None
        
        for item in self.floors[self.lift_floor]:
            for new_floor in range(max(1, self.lift_floor - 1), min(5, self.lift_floor + 2)):
                new_state = copy.deepcopy(self)
                new_state.lift_floor = new_floor
                new_state.floors[self.lift_floor].remove(item)
                new_state.floors[new_floor].add(item)
                if new_state.is_valid_state() and repr(new_state) not in self.visited:
                    self.visited.add(repr(new_state))
                    new_state.previous_state = self
                    new_state.steps_taken += 1
                    yield new_state
                    
        for items in combinations(tuple(self.floors[self.lift_floor]), 2):
            for new_floor in range(max(1, self.lift_floor - 1), min(5, self.lift_floor + 2)):
                new_state = copy.deepcopy(self)
                new_state.lift_floor = new_floor
                new_state.floors[self.lift_floor] -= set(items)
                new_state.floors[new_floor] |= set(items)
                if new_state.is_valid_state() and repr(new_state) not in self.visited:
                    self.visited.add(repr(new_state))
                    new_state.previous_state = self
                    new_state.steps_taken += 1
                    yield new_state
                    
        self.previous_state = previous_state
        
        
def find_shortest_path_bfs(initial_state, goal_state):
    queue = deque()
    queue.append(initial_state)
    max_steps = 0
    
    while queue:
       state = queue.popleft()
       # print(f"processing state > {state}")
       if state == goal_state:
           return state.steps_taken
       
       for new_state in state.generate_new_states():
           max_steps = new_state.steps_taken
           queue.append(new_state)
           
    return None
        
        
def parse_input(data_input, P2=False):
    items = []
    for idx, line in enumerate(data_input):
        floor_items = []
        # Find chips
        chip_match = re.findall(CHIP_STR, line)
        for chip in chip_match:
            chip_str = chip[0] + "M"
            floor_items.append(chip_str.upper())
        # Find generators
        gen_match = re.findall(GEN_STR, line)
        for gen in gen_match:
            gen_str = gen[0] + "G"
            floor_items.append(gen_str.upper())
        
        if P2 and idx == 0:
            floor_items.extend(["EG", "EM", "DG", "DM"])
            
        items.append(tuple(floor_items))
        
    return tuple(items)
    

def part_one(data_input):
    initial_items = parse_input(data_input)
    print(f"P1 initial items = {initial_items}")
    
    initial_state = State()
    initial_state.visited.add(repr(initial_state))
    goal_state = State()
    goal_state.lift_floor = 4
    for idx, items in enumerate(initial_items):
        initial_state.floors[idx + 1] = set(items)
        goal_state.floors[4] |= set(items)
        
    min_steps = find_shortest_path_bfs(initial_state, goal_state)
    
    return min_steps


def part_two(data_input):
    initial_items = parse_input(data_input, P2=True)
    print(f"P2 initial items = {initial_items}")
    
    initial_state = State()
    initial_state.visited.add(repr(initial_state))
    goal_state = State()
    goal_state.lift_floor = 4
    for idx, items in enumerate(initial_items):
        initial_state.floors[idx + 1] = set(items)
        goal_state.floors[4] |= set(items)
        
    min_steps = find_shortest_path_bfs(initial_state, goal_state)
    
    return min_steps

TEST_INPUT_1 = ['The first floor contains a hydrogen-compatible microchip and a lithium-compatible microchip.', 'The second floor contains a hydrogen generator.', 'The third floor contains a lithium generator.', 'The fourth floor contains nothing relevant.']

if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(11, 2016)
    
    # input_data = TEST_INPUT_1

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
