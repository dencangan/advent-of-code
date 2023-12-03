from utils.parser import parse_input, construct_2d_grid

input_list = parse_input('day3')
grid = construct_2d_grid(input_list)

def search(g, r, c):
    end = len(grid) - 1
    if r < 0 or c < 0 or r >= end or c >= end:
        return 0
    element = g[r][0][c]
    if element == '*' and element != '.':
        return r, c,
    else:
        return 0


def part2(grid):
    ans = {}
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
                    is_part_list = [x for x in is_part_list if x != 0][0]
                    if ans.get(is_part_list, None):
                        ans[is_part_list].append(int(digit))
                    else:
                        ans[is_part_list] = [int(digit)]
                    digit, is_part_list = '', []
                else:
                    digit, is_part_list = '', []

            if column == len(grid) - 1 and any(is_part_list):
                is_part_list = [x for x in is_part_list if x != 0][0]
                if ans.get(is_part_list, None):
                    ans[is_part_list].append(int(digit))
                else:
                    ans[is_part_list] = [int(digit)]
                digit, is_part_list = '', []

    res = 0
    for a, v in ans.items():
        if len(v) == 2:
            x = v[0] * v[1]
            res += x
    print(res)

part2(grid)