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
CARD_RANKINGS = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}

TEST_INPUT = ["32T3K 765", "T55J5 684", "KK677 28", "KTJJT 220", "QQQJA 483"]

class CamelCard:
    def __init__(self, value):
        self.value = value
        # rank for the tie breaker?
        self.card_rank = CARD_RANKINGS[value]

    def __str__(self):
        debug_card_str = f"Card: {self.value}, rank={self.card_rank} ; "
        card_str = self.value
        return self.value


class CamelHand:
    def __init__(self, hand):
        self.hand = [CamelCard(value) for value in hand]
        self.card_ranks = sorted([card.card_rank for card in self.hand], reverse=True)

    def __str__(self):
        hand_str = ''.join(str(card) for card in self.hand)
        #hand_strength_str = ', '.join(str(score) for score in self.get_hand_strength())
        #return_str = f"Current Hand: {[hand_str]}; Current hand ranking: {self.card_ranks}; Current hand strength: {self.get_hand_strength()}"
        return hand_str

    # Calc hand strength
    def organise_hand(self):
        # Get a list of counts for each value
        card_values = [card.value for card in self.hand]
        counts = Counter(card_values)
        count_values = sorted(counts.values(), reverse=True)

        if 5 in count_values:
            return HAND_RANKINGS["Five"]      # Five of a Kind
        if 4 in count_values:
            return HAND_RANKINGS["Four"]      # Four of a Kind
        if 3 in count_values:
            if 2 in count_values:
                return HAND_RANKINGS["Full"]  # Full House
            else:
                return HAND_RANKINGS["Three"] # Three of a Kind
        if count_values.count(2) == 4:
            return HAND_RANKINGS["Two"]       # Two Pairs
        if 2 in count_values:
            return HAND_RANKINGS["One"]       # One Pair
        else:
            return HAND_RANKINGS["High"]      # High card

    def get_strength(self):
        return (self.organise_hand(), self.card_ranks)

    def tie_break(self, other_hand):
        for self_card, other_card in zip(self.card_ranks, other_hand.card_ranks):
            if self_card > other_card:
                return True  # Self hand is stronger
            elif self_card < other_card:
                return False  # Other hand is stronger
        return False
        

def part_one(data_input):
    hands_list = []
    rank_list = []

    # Parse lines and create CamelHand objects
    for line in data_input:
        raw_hand, bid = line.split(" ")
        hand = CamelHand(raw_hand)
        hands_list.append((hand, hand.organise_hand(), int(bid)))

        #print(hands_list)

    # Classify the hand rank
    hands_list.sort(key=lambda x: (x[0].organise_hand(), x[0].card_ranks), reverse=True)

    # After sorting, apply tie-breaking for hands with equal strength
    for i in range(1, len(hands_list)):
        if hands_list[i][1] == hands_list[i - 1][1]:  # If strengths are equal
            if not hands_list[i - 1][0].tie_break(hands_list[i][0]):
                hands_list[i - 1], hands_list[i] = hands_list[i], hands_list[i - 1]

    for rank, (hand, _, bid) in enumerate(hands_list, 1):
        winnings = (len(hands_list) - rank + 1) * bid  # Reverse the rank so that the strongest gets the highest rank
        rank_list.append((str(hand), len(hands_list) - rank + 1, bid, winnings))  # Reverse the rank

    print(f"rank_list: {rank_list}")

    total = sum(rank[3] for rank in rank_list)

    return total


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
