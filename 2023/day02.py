"""
Author: IchBinJade
Date  : 2024-11-22
AoC Day 2 - https://adventofcode.com/2023/day/2
"""

import sys
import os
import time
import re

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from functools import reduce
from utils import get_list_from_file

MAX_COLOURS = {
    "red": 12,
    "green": 13,
    "blue": 14
}

def calc_game_id_sum(game_id_list):
    sum = 0
    for game in game_id_list:
        sum += int(game)
    return sum


def get_game_dict(game_list):
    games = {}

    # Loop game list and strip the games from each line, using it as a new key in 'games'
    for line in game_list:
        game_sections = line.split(": ")
        parse_game_id = game_sections[0].strip()
        game_id = re.sub(f'\D', '', parse_game_id) # remove non-numeric
        subsets = game_sections[1].split(";")
        games[game_id] = {
            'red': 0,
            'green': 0,
            'blue': 0
        }

        # Loop subsets and find the max value for each colour according to the max value from the subset
        for subset in subsets:
            # Match "amount color" expression globally
            matches = re.findall(r'(\d+) (\w+)', subset)

            if matches:
                for match in matches:
                    parse_amount, colour = match
                    amount = int(parse_amount)

                    if colour == 'red':
                        games[game_id]['red'] = max(games[game_id]['red'], amount)
                    elif colour == 'green':
                        games[game_id]['green'] = max(games[game_id]['green'], amount)
                    elif colour == 'blue':
                        games[game_id]['blue'] = max(games[game_id]['blue'], amount)

    return games


def part_one(input):
    # Find the max for each colour
    games = get_game_dict(input)

    # Get list of id's that have values that don't exceed the values in MAX_COLOURS
    game_list = [
        game_id for game_id, game_data in games.items()
        if game_data['red'] <= MAX_COLOURS['red'] and
        game_data['green'] <= MAX_COLOURS['green'] and
        game_data['blue'] <= MAX_COLOURS['blue']
    ]

    return calc_game_id_sum(game_list)


def part_two(input):
    # Find the max for each colour
    games = get_game_dict(input)

    # Calculate power per game
    power_list = [
        reduce(lambda power, colour: power * current_game[colour], current_game, 1)
        for game_id, current_game in games.items()
    ]

    return calc_game_id_sum(power_list)  



if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(2, 2023)

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")