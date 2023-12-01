def parse_input(day: str):
    file = open(f'{day}/input.txt', 'r')
    lines = file.readlines()
    input_list = []
    for l in lines:
        line = l.strip()
        input_list.append(line)
    return input_list
