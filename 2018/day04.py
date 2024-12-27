"""
Author: IchBinJade
Date  : 2024-12-27
AoC 2018 Day 4 - https://adventofcode.com/2018/day/4

Utilises: datetime manipulation, roster grid
"""

import sys
import os
import time
import datetime

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file


def print_roster(roster_timings):
    for date in sorted(roster_timings.keys()):
        print(f"{date} ", end="")
        for guard, sched in roster_timings[date].items():
            print(f"#{guard} ", end="")
            print("".join(sched))


def parse_input(data_input):
    sleep_start = None
    sleep_end = None
    roster_timings = {}
    curr_guard = None
    
    for line in data_input:
        stamp_str = " ".join(line.strip("[").split()[0:2])
        stamp_str = stamp_str.strip("]")
        timestamp = datetime.datetime.strptime(stamp_str, "%Y-%m-%d %H:%M")
        date_str = timestamp.strftime("%Y-%m-%d")

        # Handling time overflow (e.g., 23:58 becomes 00:00 of the next day)
        if timestamp.hour == 23:
            timestamp += datetime.timedelta(days=1)
            timestamp = timestamp.replace(hour=0, minute=0, second=0)
            date_str = timestamp.strftime("%Y-%m-%d")
            
        if "Guard" in line:
            guard_id = line.split()[3].strip("#")
            if date_str not in roster_timings:
                roster_timings[date_str] = {}
            if guard_id not in roster_timings[date_str]:
                roster_timings[date_str][guard_id] = ["."] * 60
            curr_guard = guard_id
        elif "falls asleep" in line and curr_guard:
            sleep_start = timestamp.minute
        elif "wakes up" in line and curr_guard:
            sleep_end = timestamp.minute
            for minute in range(sleep_start, sleep_end):
                roster_timings[date_str][curr_guard][minute] = "#"
            for minute in range(sleep_end, 60):
                roster_timings[date_str][curr_guard][minute] = "."
            
    return roster_timings


def process_roster(roster_timings):
    guard_sleep_sched = {}
    guard_sleep_times = {}
    
    for date in sorted(roster_timings.keys()):
        for guard, sched in roster_timings[date].items():
            this_sleep = sched.count("#")
            if guard not in guard_sleep_times:
                guard_sleep_times[guard] = this_sleep
            else:
                guard_sleep_times[guard] += this_sleep
                
            if guard not in guard_sleep_sched:
                guard_sleep_sched[guard] = [0] * 60
                
            for minute, status in enumerate(sched):
                if status == "#":
                    guard_sleep_sched[guard][minute] += 1
                    
    # Find sleepiest guard
    sleepiest_guard = max(guard_sleep_times, key=guard_sleep_times.get)
    most_sleep = guard_sleep_times[sleepiest_guard]
    
    # print(f"sleepiest guard was {sleepiest_guard} with total of {most_sleep}")
    
    # Then for that sleepiest guard, find the minute they were asleep the most
    sleep_array = guard_sleep_sched[sleepiest_guard]
    most_min_sleep = max(range(len(sleep_array)), key=lambda idx: sleep_array[idx])
    
    return sleepiest_guard, most_min_sleep


def find_sleepy_minute(roster_timings):
    # Track how many times a guard sleeps at each minute
    guard_sleep_mins = {}
    for date in sorted(roster_timings.keys()):
        for guard, sched in roster_timings[date].items():
            for minute, status in enumerate(sched):
                if status == "#":
                    if guard not in guard_sleep_mins:
                        guard_sleep_mins[guard] = [0] * 60
                    else:
                        guard_sleep_mins[guard][minute] += 1
                        
    # Find the guard with the most freq min of sleep
    max_sleep = 0
    sleep_guard = None
    sleep_min = None
    for guard, minute_counts in guard_sleep_mins.items():
        most_freq_min = max(range(len(minute_counts)), key=lambda idx: minute_counts[idx])
        sleep_count = minute_counts[most_freq_min]
        if sleep_count > max_sleep:
            max_sleep = sleep_count
            sleep_guard = guard
            sleep_min = most_freq_min
    
    return sleep_guard, sleep_min
    

def part_one(data_input):
    data_input.sort()

    roster_timings = parse_input(data_input)
    # print_roster(roster_timings)
    
    sleep_guard, sleepy_min = process_roster(roster_timings)
    
    return int(sleep_guard) * int(sleepy_min)


def part_two(data_input):
    data_input.sort()

    roster_timings = parse_input(data_input)
    # print_roster(roster_timings)
    
    sleep_guard, sleepy_min = find_sleepy_minute(roster_timings)
    
    return int(sleep_guard) * int(sleepy_min)


if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(4, 2018)

    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
