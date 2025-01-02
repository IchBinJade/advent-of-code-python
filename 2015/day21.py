"""
Author: IchBinJade
Date  : 2025-01-02
AoC 2015 Day 21 - https://adventofcode.com/2015/day/21

Find gold spend to defend your RPG character; uses itertools.combinations()
and dictionaries of tuples
"""

import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file
from itertools import combinations


WEAPONS = {
    (8, 4, 0),
    (10, 5, 0),
    (25, 6, 0),
    (40, 7, 0),
    (74, 8, 0)
}

ARMOUR = {
    (13, 0, 1),
    (31, 0, 2),
    (53, 0, 3),
    (75, 0, 4),
    (102, 0, 5),
    (0, 0, 0)
}

RINGS = {
    (25, 1, 0),
    (50, 2, 0),
    (100, 3, 0),
    (20, 0, 1),
    (40, 0, 2),
    (80, 0, 3),
    (0, 0, 0),
    (0, 0, 0)
}


def fight_boss(player, boss):
    p_hp, p_damage, p_armour = player[0], player[1], player[2]
    b_hp, b_damage, b_armour = boss[0], boss[1], boss[2]
    
    while True:
        # Attack boss
        b_hp -= max(p_damage - b_armour, 1)
        if b_hp <= 0:
            return True
        
        # Attack player
        p_hp -= max(b_damage - p_armour, 1)
        if p_hp <= 0:
            return False


def part_one(data_input):
    """ Limits:
    - Only 1 weapon
    - Armor 0 or 1
    - 0-2 rings, but 1 of each item
    """
    # Objective: What is the least amount of gold spend to win?
    boss = []
    for line in data_input:
        boss.append(int(line.split()[-1]))
    
    win_costs = []
    for w_cost, w_damage, _ in WEAPONS:
        for a_cost, _, a_armour in ARMOUR:
            for ring1, ring2 in combinations(RINGS, 2):
                damage = w_damage + ring1[1] + ring2[1]
                armour = a_armour + ring1[2] + ring2[2]
                player = [100, damage, armour]
                if fight_boss(player, boss):
                    win_costs.append(w_cost + a_cost + ring1[0] + ring2[0])
    
    return min(win_costs)


def part_two(data_input):
    """ Limits:
    - Only 1 weapon
    - Armor 0 or 1
    - 0-2 rings, but 1 of each item
    """
    # Objective: (Dirty Shopkeeper) What is the most gold you spend and still lose?
    boss = []
    for line in data_input:
        boss.append(int(line.split()[-1]))
    
    loss_costs = []
    for w_cost, w_damage, _ in WEAPONS:
        for a_cost, _, a_armour in ARMOUR:
            for ring1, ring2 in combinations(RINGS, 2):
                damage = w_damage + ring1[1] + ring2[1]
                armour = a_armour + ring1[2] + ring2[2]
                player = [100, damage, armour]
                if not fight_boss(player, boss):
                    loss_costs.append(w_cost + a_cost + ring1[0] + ring2[0])
    
    return max(loss_costs)


if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(21, 2015)

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
