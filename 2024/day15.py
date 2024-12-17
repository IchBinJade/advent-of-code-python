"""
Author: IchBinJade
Date  : 2024-12-16
AoC 2024 Day 15 - https://adventofcode.com/2024/day/15

TODO: Start and solve part 2
"""

import sys
import os
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utils import get_list_from_file


def move_the_bot(grid, bot_pos, moves):
    row_count = len(grid)
    col_count = len(grid[0])
    row, col = bot_pos
    
    for move in moves:
        curr_row, curr_col = row, col
        boxes = [(curr_row, curr_col)]
        d_row = {"^": -1, "v": 1}.get(move, 0)
        d_col = {"<": -1, ">": 1}.get(move, 0)
        
        can_move = True
        
        while True:
            curr_row += d_row
            curr_col += d_col            
            if grid[curr_row][curr_col] == "#":
                can_move = False
                break
            if grid[curr_row][curr_col] == ".":
                break
            if grid[curr_row][curr_col] == "O":
                boxes.append((curr_row, curr_col))
        
        if can_move:
            grid[row][col] = "."
            grid[row + d_row][col + d_col] = "@"
            for box_row, box_col in boxes[1:]:
                grid[box_row + d_row][box_col + d_col] = "O"
            
            row += d_row
            col += d_col                     
    
    return grid


def part_one(data_input):
    blank_idx = data_input.index("")
    warehouse = [list(char for char in row) for row in data_input[:blank_idx]]
    moves = "".join(data_input[blank_idx + 1:])

    for idx, row in enumerate(warehouse):
        if "@" in row:
            bot_pos = (idx, row.index("@"))
            break
        
    final_grid = move_the_bot(warehouse, bot_pos, moves)
    # print("Final Grid:")
    # for row in final_grid:
    #     print(*row, sep="")
    
    # Get box coords = (100 * dist_from_top) + dist_from_left
    box_gps_list = []
    for row in range(len(final_grid)):
        for col in range(len(final_grid[row])):
            if final_grid[row][col] == "O":
                box_gps_list.append(100 * row + col)
    
    return sum(box_gps_list)


def part_two(data_input):
    result = 0
    
    return result

TEST_INPUT_1 = ['########', '#..O.O.#', '##@.O..#', '#...O..#', '#.#.O..#', '#...O..#', '#......#', '########', '', '<^^>>>vv<v>>v<<']
TEST_INPUT_2 = ['##########', '#..O..O.O#', '#......O.#', '#.OO..O.O#', '#..O@..O.#', '#O#..O...#', '#O..O..O.#', '#.OO.O.OO#', '#....O...#', '##########', '', '<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^', 'vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v', '><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<', '<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^', '^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><', '^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^', '>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^', '<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>', '^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>', 'v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^']

if __name__ == "__main__":
    t1 = time.time()

    # Get input data
    input_data = get_list_from_file(15, 2024)

    # input_data = TEST_INPUT_2
    
    # Get solutions
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    # Calc execution time
    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
