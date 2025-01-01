"""
Author: IchBinJade
Date  : 2025-01-01
AoC 2015 Day 14 - https://adventofcode.com/2015/day/14

Reindeer racing with python OOP
"""

import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file

class Reindeer:
    def __init__(self, name, speed, dist_before_rest, rest_time):
        self.name = name
        self.speed = speed
        self.dist_before_rest = dist_before_rest
        self.is_resting = False
        self.rest_time = rest_time
        self.dist_travelled = 0
        self.time_spent_resting = 0
        self.time_without_rest = 0
        self.points = 0
        
    def move_one_second(self):
        if self.is_resting:
            self.time_spent_resting += 1
            if self.rest_time == self.time_spent_resting:
                self.time_spent_resting = 0
                self.time_without_rest = 0
                self.is_resting = False
        else:
            self.dist_travelled += self.speed
            self.time_without_rest += 1
            if self.time_without_rest == self.dist_before_rest:
                self.is_resting = True
                
    def get_distance_travelled(self):
        return self.dist_travelled
    
    def increment_points(self):
        self.points += 1
        
    def get_points(self):
        return self.points
    
    def get_name(self):
        return self.name


def calc_distances(reindeers, race_time):
    for sec in range(race_time):
        for reindeer in reindeers:
            reindeer.move_one_second()
            
    distances = []
    for reindeer in reindeers:
        distances.append(reindeer.get_distance_travelled())
    
    return max(distances)


def calc_points(reindeers, race_time):
    for sec in range(race_time):
        for reindeer in reindeers:
            reindeer.move_one_second()
        max_distance = max([reindeer.get_distance_travelled() for reindeer in reindeers])

        for reindeer in reindeers:
            if reindeer.get_distance_travelled() == max_distance:
                reindeer.increment_points()
    
    points = []
    for reindeer in reindeers:
        points.append(reindeer.get_points())
        # print(f"{reindeer.get_name()} has {reindeer.get_points()}")
        
    return max(points)


def part_one(data_input):
    # After 2503 seconds, what's the winning reindeer's distance
    reindeers = []
    for line in data_input:
        name, speed, dist_before_rest, rest_time = line.split()[0], line.split()[3], line.split()[6], line.split()[-2]
        reindeer = Reindeer(name, int(speed), int(dist_before_rest), int(rest_time))
        reindeers.append(reindeer)
    
    winning_distance = calc_distances(reindeers, 2503)
    
    return winning_distance


def part_two(data_input):
    # After 2503 seconds, what's the winning reindeer's score
    reindeers = []
    for line in data_input:
        name, speed, dist_before_rest, rest_time = line.split()[0], line.split()[3], line.split()[6], line.split()[-2]
        reindeer = Reindeer(name, int(speed), int(dist_before_rest), int(rest_time))
        reindeers.append(reindeer)
    
    winning_points = calc_points(reindeers, 2503)
    
    return winning_points


if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(14, 2015)

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
