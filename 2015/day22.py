"""
Author: IchBinJade
Date  : 2025-01-06
AoC 2015 Day 22 - https://adventofcode.com/2015/day/22

Find min mana spend for magic RPG; utilises recursion
"""

import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file
from copy import deepcopy

MIN_MANA_SPENT = float("inf")
HARD = False

SPELLS = [
    {"name": "Magic Missile", "cost": 53, "damage": 4, "health": 0, "armour": 0, "mana": 0, "turns": 0},
    {"name": "Drain", "cost": 73, "damage": 2, "health": 2, "armour": 0, "mana": 0, "turns": 0},
    {"name": "Shield", "cost": 113, "damage": 0, "health": 0, "armour": 7, "mana": 0, "turns": 6},
    {"name": "Poison", "cost": 173, "damage": 3, "health": 0, "armour": 0, "mana": 0, "turns": 6},
    {"name": "Recharge", "cost": 229, "damage": 0, "health": 0, "armour": 0, "mana": 101, "turns": 5}
]
    
    
def simulate_fight(player_hp, player_mana, boss_hp, boss_dmg, active_spells=[], players_turn=True, mana_spent=0):
    global MIN_MANA_SPENT
    
    player_armour = 0
    
    if HARD and players_turn:
        player_hp -= 1
        if player_hp <= 0:
            return False
    
    new_active_spells = []
    for spell in active_spells:
        if spell["turns"] >= 0:
            boss_hp -= spell["damage"]
            player_hp += spell["health"]
            player_armour += spell["armour"]
            player_mana += spell["mana"]
                
        new_spell = deepcopy(spell)
        new_spell["turns"] -= 1
        if new_spell["turns"] > 0:
            new_active_spells.append(new_spell)
            
    if boss_hp <= 0:
        MIN_MANA_SPENT = min(MIN_MANA_SPENT, mana_spent)
        return True
        
    if mana_spent >= MIN_MANA_SPENT:
        return False
        
    if players_turn:
        for spell in SPELLS:
            spell_is_active = False
            for new_spell in new_active_spells:
                if new_spell["name"] == spell["name"]:
                    spell_is_active = True
                    break
                  
            spell_mana_cost = spell["cost"]
            if spell_mana_cost <= player_mana and not spell_is_active:
                active = deepcopy(new_active_spells)
                active.append(spell)
                new_mana = player_mana - spell_mana_cost
                new_mana_spent = mana_spent + spell_mana_cost
                simulate_fight(player_hp, new_mana, boss_hp, boss_dmg, active, False, new_mana_spent)
    else:
        damage = max(0, boss_dmg - player_armour)
        new_player_hp = player_hp - damage
        if new_player_hp > 0:
            simulate_fight(new_player_hp, player_mana, boss_hp, boss_dmg, new_active_spells, True, mana_spent)
        

def part_one(data_input):
    """What is the least amount of mana you can spend and still win the fight?"""
    global MIN_MANA_SPENT, HARD
    boss = [] # HP, Damage
    for line in data_input:
        boss.append(int(line.split()[-1]))
    
    BOSS_HP, BOSS_DMG = boss[0], boss[1]
    HARD = False
    MIN_MANA_SPENT = float("inf")
    simulate_fight(50, 500, BOSS_HP, BOSS_DMG)
            
    return int(MIN_MANA_SPENT)


def part_two(data_input):
    """
    HARD mode: At the start of each player turn (before any other effects apply), you lose 1 hit point.
    What is the least amount of mana you can spend and still win the fight?
    """
    global MIN_MANA_SPENT, HARD
    boss = [] # HP, Damage
    for line in data_input:
        boss.append(int(line.split()[-1]))
    
    BOSS_HP, BOSS_DMG = boss[0], boss[1]
    HARD = True
    MIN_MANA_SPENT = float("inf")
    simulate_fight(50, 500, BOSS_HP, BOSS_DMG)
            
    return int(MIN_MANA_SPENT)


if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(22, 2015)

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
