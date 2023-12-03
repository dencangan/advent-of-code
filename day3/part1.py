from utils.parser import parse_input, construct_2d_grid

input_list = parse_input('day3')
grid = construct_2d_grid(input_list)


def search(g, r, c):
    end = len(grid) - 1
    if r < 0 or c < 0 or r >= end or c >= end:
        return False
    element = g[r][0][c]
    if not element.isdigit() and element != '.':
        return True
    else:
        return False


def part1(grid):
    ans = []
    for row in range(len(grid)):
        number_of_cols = len(grid[0][0])
        is_part_list = []
        digit = ''
        for column in range(number_of_cols):
            row_element = grid[row][0]
            element_search = grid[row][0][column]
            if element_search.isdigit():
                digit += row_element[column]
                # down
                is_part_list.append(search(grid, row + 1, column))
                # up
                is_part_list.append(search(grid, row - 1, column))
                # right
                is_part_list.append(search(grid, row, column + 1))
                # left
                is_part_list.append(search(grid, row, column - 1))
                # up right
                is_part_list.append(search(grid, row - 1, column + 1))
                # down right
                is_part_list.append(search(grid, row + 1, column + 1))
                # up left
                is_part_list.append(search(grid, row + 1, column - 1))
                # down left
                is_part_list.append(search(grid, row - 1, column - 1))
            else:
                if any(is_part_list):
                    ans.append(int(digit))
                    digit, is_part_list = '', []
                else:
                    digit, is_part_list = '', []
            if column == len(grid) - 1 and any(is_part_list):
                ans.append(int(digit))
                digit, is_part_list = '', []

    print(sum(ans))

part1(grid)