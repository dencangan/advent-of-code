from utils.parser import parse_input

input_list = parse_input('day1')

res = []
for line in input_list:
    left_index = 0
    right_index = len(line) - 1
    left_value = ''
    right_value = ''
    for _ in range(len(line)):
        left = line[left_index]
        right = line[right_index]
        if not left_value:
            if left.isdigit():
                left_value += left
            else:
                left_index += 1
        elif not right_value:
            if right.isdigit():
                right_value += right
            else:
                right_index -= 1
        if left_value and right_value:
            res.append(int(left_value + right_value))
            break

    if not left_value or not right_value:
        value = left_value + right_value
        value += value
        res.append(int(value))

print(res)
print(len(res))
print(sum(res))
