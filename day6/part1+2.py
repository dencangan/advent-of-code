from utils.parser import parse_input

def hold_times_to_beat_best(time, distance):
    res = []
    for race_time, distance_to_beat in zip(time, distance):
        num = 0
        for i in range(race_time):
            travel_time = race_time - i
            td = i * travel_time
            if td >= distance_to_beat:
                num += 1
        res.append(num)
    return res


# Part 1
input_lines = parse_input('day6')
time = [int(t) for t in input_lines[0].split(' ')[1:] if t != '']
distance = [int(t) for t in input_lines[1].split(' ')[1:] if t != '']
res = hold_times_to_beat_best(time, distance)
r = 1
for i in res:
    r *= i
print(res)


# Part 2
# Lazy to parse
time = [52947594]
distance = [426137412791216]
res = hold_times_to_beat_best(time, distance)
print(res)
