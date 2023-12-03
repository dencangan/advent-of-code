import os

def parse_input(day: str):
    file = open(os.path.join(os.path.dirname(os.path.dirname(__file__)), f'{day}/input.txt'), 'r')
    lines = file.readlines()
    input_list = []
    for l in lines:
        line = l.strip()
        input_list.append(line)
    return input_list

def construct_2d_grid(input_list: list):
    grid = []
    for line in input_list:
        grid.append([line])
    return grid