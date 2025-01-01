"""
Author: IchBinJade
Date  : 2025-01-01
AoC 2015 Day 15 - https://adventofcode.com/2015/day/15

Using itertools.product() to get combinations of "recipes"
"""

import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file
from itertools import product


def calc_scores(ingredients, inc_calories=False):
    scores = []
    ingredient_names = list(ingredients.keys())
    num_ingredients = len(ingredient_names)
    
    # Use product to generate all combos of ingredient spoons totalling 100
    for quantities in product(range(101), repeat=num_ingredients):
        if sum(quantities) == 100:
            total_capacity = sum(ingredients[ingredient_names[i]][0] * quantities[i] for i in range(num_ingredients))
            total_durability = sum(ingredients[ingredient_names[i]][1] * quantities[i] for i in range(num_ingredients))
            total_flavour = sum(ingredients[ingredient_names[i]][2] * quantities[i] for i in range(num_ingredients))
            total_texture = sum(ingredients[ingredient_names[i]][3] * quantities[i] for i in range(num_ingredients))
            
            # Treat any negative as a 0
            total_capacity = max(0, total_capacity)
            total_durability = max(0, total_durability)
            total_flavour = max(0, total_flavour)
            total_texture = max(0, total_texture)
            
            score = total_capacity * total_durability * total_flavour * total_texture
            if inc_calories:
                # Part 2 logic
                total_calories = sum(ingredients[ingredient_names[i]][4] * quantities[i] for i in range(num_ingredients))
                if total_calories == 500:
                    scores.append(score)
            else:
                scores.append(score)
    
    return scores


def part_one(data_input):
    ingredients = {}
    for line in data_input:
        ing, cap, dur, flav, tex = line.split()[0].strip(",").strip(":"), line.split()[2].strip(","), line.split()[4].strip(","), line.split()[6].strip(","), line.split()[8].strip(",")
        ingredients[ing] = (int(cap), int(dur), int(flav), int(tex))
    
    scores = calc_scores(ingredients)
    
    return max(scores)


def part_two(data_input):
    ingredients = {}
    for line in data_input:
        ing, cap, dur, flav, tex, cal = line.split()[0].strip(",").strip(":"), line.split()[2].strip(","), line.split()[4].strip(","), line.split()[6].strip(","), line.split()[8].strip(","), line.split()[-1]
        ingredients[ing] = (int(cap), int(dur), int(flav), int(tex), int(cal))
    
    scores = calc_scores(ingredients, True)
    
    return max(scores)


if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(15, 2015)

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
