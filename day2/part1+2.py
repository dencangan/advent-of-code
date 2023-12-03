from utils.parser import parse_input

input_list = parse_input('day2')
input_res = {"red": 12, "green": 13, "blue":14}

parsed = {}
for game in input_list:
    game = game.split(';')
    for i, g in enumerate(game):
        game_data = {}
        if i == 0:
            game_number, g = g.split(':')
            if game_number not in parsed:
                game_number = int(game_number.replace('Game ', ''))
                parsed[game_number] = []
        game_value = g.replace(' ', '').split(',')
        num = ''
        alpha = ''
        game_value_container = []
        for cubes in game_value:
            for c in cubes:
                if c.isdigit():
                    num += c
                else:
                    alpha += c
            if num and alpha:
                game_value_container.append({alpha:int(num)})
            num = ''
            alpha = ''
        parsed[game_number].append(game_value_container)

res = {}
for game, data in parsed.items():
    res[game] = []
    for game_set in data:
        possible = []
        for cube_data in game_set:
            for colour, num in cube_data.items():
                remainder = input_res[colour] - num
                if remainder < 0:
                    res[game].append(False)
games = 0
for i, r in res.items():
    if len(r) == 0:
        games += i
print(games)

res2 = {}
for game, game_data in parsed.items():
    mini = {}
    for g in game_data:
        for gg in g:
            for colour, num in gg.items():
                mini.setdefault(colour, 0)
                if mini[colour] == 0:
                    mini[colour] = num
                else:
                    if num > mini[colour]:
                        mini[colour] = num
    res2[game] = mini

res2_results = 0
for i, v in res2.items():
    r = 1
    for vv in v.values():
        r *= vv
    res2_results += r
print(res2_results)