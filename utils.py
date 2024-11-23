"""
Useful functions to help with puzzles
"""

import os

def get_input_file(day: int, year:int) -> str:
    # Construct the file path
    day_str = f"{day:02d}"
    cwd = os.path.dirname(__file__)
    input_folder = os.path.join(cwd, str(year), 'inputs')
    input_path = os.path.join(input_folder, f'day{day_str}.txt')

    # Check the file exists
    if not(os.path.exists(input_path)):
        raise FileNotFoundError(f"Can't find input file: {input_path}")
    
    return input_path

def get_list_from_file(day: int, year: int):
    # Get file and return list
    file_path = get_input_file(day, year)
    with open(file_path, 'r') as file:
        return file.read().splitlines()

