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

HAND_RANKINGS = {"Five": 6, "Four": 5, "Full": 4, "Three": 3, "Two": 2, "One": 1, "High": 0}
CARD_RANKINGS = {"A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "T": 10, "J": 11, "Q": 12, "K": 13}

class CamelCard:
    def __init__(self, value):
        self.value = value
        # rank for the tie breaker?
        self.card_rank = CARD_RANKINGS[str(value)]

    def __str__(self):
        debug_card_str = f"Card: {self.value}, rank={self.card_rank} ; "
        card_str = self.value
        return self.value


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
        hand_str = ''.join(str(card) for card in self.hand)
        #hand_strength_str = ', '.join(str(score) for score in self.get_hand_strength())
        return_str = f"Current Hand: {[hand_str]}; Current hand ranking: {self.card_ranks}; Current hand strength: {self.get_hand_strength()}"
        return hand_str

    # Calc hand strength
    def get_hand_strength(self):
        # First get card values of hand
        values = [card.value for card in self.hand]
        # Get a list of counts for each value
        counts = [values.count(card.value) for card in self.hand]

        # Return hand 'score' based on HAND_RANKINGS
        if 5 in counts:
            return HAND_RANKINGS["Five"]      # Five of a Kind
        if 4 in counts:
            return HAND_RANKINGS["Four"]      # Four of a Kind
        if 3 in counts:
            if 2 in counts:
                return HAND_RANKINGS["Full"]  # Full House
            else:
                return HAND_RANKINGS["Three"] # Three of a Kind
        if counts.count(2) == 4:
            return HAND_RANKINGS["Two"]       # Two Pairs
        if 2 in counts:
            return HAND_RANKINGS["One"]       # One Pair
        else:
            return HAND_RANKINGS["High"]      # High card

    def tie_break(self, other_hand):
        # Compare hands, card by card, from original order
        # For each card pair, compare the card rank. Cards are (value, rank)
        for self_card, other_card in zip(self.card_ranks, other_hand.card_ranks):
            if self_card[1] > other_card[1]:
                return True    # Self hand is stronger
            elif self_card[1] < other_card[1]:
                return False   # Other hand is stronger
        

def part_one(data_input):
    hands_list = []
    bids_list = []
    rank_list = []

    # Parse lines and create CamelHand objects
    for line in data_input:
        #print(f"line >>> {line}")
        raw_hand, bid = line.split(" ")
        #hand = CamelHand(line.split(" "[0]))
        #bid = line.split(" ")[1]
        hand = CamelHand(raw_hand)
        #hands_list.append(hand)
        #bids_list.append(int(bid))
        #print(hand.get_hand_strength())
        hands_list.append((str(hand), hand.get_hand_strength(), int(bid)))

        # Classify the hand rank


    print(f"hands_list: {hands_list}")

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
