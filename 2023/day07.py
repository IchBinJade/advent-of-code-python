"""
Author: IchBinJade
Date  : 2024-12-07
AoC 2023 Day 7 - https://adventofcode.com/2023/day/7

Helpful note (thanks @hyper-neutrino):
------------

Visit https://www.asciitable.com/ for character precedence
"""

import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file
from collections import Counter

HAND_RANKINGS = {"Five": 6, "Four": 5, "Full": 4, "Three": 3, "Two": 2, "One": 1, "High": 0}
CARD_MAPPINGS = {"T": "A", "J": "B", "Q": "C", "K": "D", "A": "E"}
JOKER_MAPPINGS = {"T": "A", "J": "*", "Q": "C", "K": "D", "A": "E"}

def get_hand_strength(hand):
    # Get a list of counts for each value
    counts = [hand.count(card) for card in hand]

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
    
    return 0

def get_hand_strength_with_jokers(hand):
    # Strip J's from the hand before checking counts. If count + no_of_j's makes up the hands, return hand rank
    jokers_count = hand.count("J")
    hand = [card for card in hand if card != "J"]
    counts = sorted(Counter(hand).values(), reverse=True)
    
    # If no cards are left after removing jokers, treat as an empty hand
    if not counts:
        counts = [0]
  
    # Add jokers to the counts and check for hand rankings
    if counts[0] + jokers_count == 5:
        return HAND_RANKINGS["Five"]      # Five of a Kind
    if counts[0] + jokers_count == 4:
        return HAND_RANKINGS["Four"]      # Four of a Kind
    if counts[0] + jokers_count == 3:
        if len(counts) > 1 and counts[1] == 2:
            return HAND_RANKINGS["Full"]  # Full House
        return HAND_RANKINGS["Three"]     # Three of a Kind
    if counts[0] + jokers_count == 3:
        return HAND_RANKINGS["Three"]     # Three of a Kind (with jokers)
    if counts[0] == 2 and (jokers_count > 0 or len(counts) > 1 and counts[1] == 2):
        return HAND_RANKINGS["Two"]       # Two Pairs (with jokers)
    if counts[0] == 2 or jokers_count:
        return HAND_RANKINGS["One"]       # One Pair (with jokers)
    else:
        return HAND_RANKINGS["High"]      # High card (with jokers)
    
    return 0
            
def organise_hand(hand):
    # Get hand strength first
    typed_hand = get_hand_strength(hand)
    # Then organise by card strength
    card_rank = [CARD_MAPPINGS.get(card, card) for card in hand]
    
    return (typed_hand, card_rank)


def organise_hand_with_jokers(hand):
    # Change how "J"s are mapped, using *
    typed_hand =  get_hand_strength_with_jokers(hand)
    card_rank = [JOKER_MAPPINGS.get(card, card) for card in hand]
    return (typed_hand, card_rank)


def part_one(data_input):
    total = 0
    hands_list = []

    # Get list of tuples of the hand, bid combo
    for line in data_input:
        hand = line.split()[0]
        bid = int(line.split()[1])
        hands_list.append((hand, bid))  
    
    # Sort the hands
    hands_list.sort(key=lambda hand: organise_hand(hand[0]))
    
    # Now they're sorted, calc winnings
    for rank, (hand, bid) in enumerate(hands_list, 1):
        total += rank * bid    
        
    return total


def part_two(data_input):
    total = 0
    hands_list = []

    # Get list of tuples of the hand, bid combo
    for line in data_input:
        hand = line.split()[0]
        bid = int(line.split()[1])
        hands_list.append((hand, bid))
    
    # Sort the hands
    hands_list.sort(key=lambda hand_bid: organise_hand_with_jokers(hand_bid[0]))
    
    # Now they're sorted, calc winnings
    for rank, (hand, bid) in enumerate(hands_list, 1):
        total += rank * bid    
        
    return total



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
