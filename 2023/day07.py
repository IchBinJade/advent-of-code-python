"""
Author: IchBinJade
Date  : 2024-12-02
AoC 2023 Day 7 - https://adventofcode.com/2023/day/7
"""

import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file
from collections import Counter

CARD_RANKINGS = {"A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "T": 10, "J": 11, "Q": 12, "K": 13}

class CamelCard:
    def __init__(self, value):
        self.value = value
        # rank for the tie breaker?
        self.card_rank = CARD_RANKINGS[str(value)]


class CamelHand:
    def __init__(self, hand):
        self.hand = []
        self.card_ranks = []
        self.hand_strength = int()
        for idx, _ in enumerate(hand):
            character = hand[idx]
            #print(f"character >>> {character}")
            card = CamelCard(character)
            self.hand.append(card)
            self.card_ranks.append((card.value, card.card_rank))
        #print(f"self.hand >>> {self.hand}")
        #print(f"rankings >>> {self.card_ranks}")

    def __str__(self):
        return f" Current hand ranking: {self.card_ranks}; Current hand strength: {self.hand_strength}"

    # Calc hand strength
    def get_hand_strength(self):
        counts = Counter(self.hand)
        return list(counts)
        

def part_one(data_input):
    hands_list = []
    bids_list = []
    for line in data_input:
        #print(f"line >>> {line}")
        raw_hand, bid = line.split(" ")
        #hand = CamelHand(line.split(" "[0]))
        #bid = line.split(" ")[1]
        hand = CamelHand(raw_hand)
        hands_list.append(hand)
        bids_list.append(int(bid))
        print(hand)
    #hands_list = [CamelHand(hand) for hand.split(" ")[0] in data_input]
    #bids_list = [int(bid) for bid.split(" ")[1] in data_input]
    #print(f"hands_list >>> {hand.hand}")
    print(f"bids_list >>> {bids_list}")
    print(f"hand.get_hand_strength >>> {hand.get_hand_strength()}")
    return None


def part_two(data_input):
    

    return None



if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(7, 2023)

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
