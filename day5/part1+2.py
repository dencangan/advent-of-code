from utils.parser import parse_input
from collections import defaultdict

input_lines = parse_input("day5", False)

seeds = input_lines[0]
seeds = seeds.split(' ')[1:]
seeds = [int(x) for x in seeds]
data = {
    "seed-to-soil map:": [],
    "soil-to-fertilizer map:": [],
    "fertilizer-to-water map:": [],
    "water-to-light map:": [],
    "light-to-temperature map:": [],
    "temperature-to-humidity map:": [],
    "humidity-to-location map:": [],
}

current_map = ""
for line in input_lines[1:]:
    if line == "":
        continue
    elif line in data.keys():
        data[line] = []
        current_map = line
    else:
        line = line.split()
        line = [int(x) for x in line]
        data[current_map].append(tuple(line))


def get_ranges(data: dict):
    res = defaultdict(list)
    for map_name, map_data in data.items():
        for d in map_data:
            dest = d[0]
            source = d[1]
            map_range = d[2]
            source_range = range(source, source + map_range)
            dest_range = range(dest, dest + map_range)
            res[map_name].append((dest_range, source_range))
    return res


def get_seeds(s, map_names, full_map):
    seed_map = defaultdict(list)
    current = s
    for map_name in map_names:
        mapping = full_map[map_name]
        for i, m in enumerate(mapping):
            if current in m[1]:
                delta = current - m[1].start
                s_dest = m[0].start + delta
                seed_map[s].append(s_dest)
                break
            if i == len(mapping) - 1 and current not in m[1]:
                seed_map[s].append(current)
        current = seed_map[s][-1]
    return seed_map[s]

def minimum_location(seed_map: dict):
    minimum = float('inf')
    for i, v in seed_map.items():
        location = v[-1]
        if location < minimum:
            minimum = location
    return minimum

# part 1
ranges_res = get_ranges(data)

res_1 = defaultdict(list)
for s in seeds:
    z = get_seeds(s, ranges_res.keys(), ranges_res)
    res_1[s] = z

print(minimum_location(res_1))

# part 2
paired_list = []
for i in range(0, len(seeds)-1, 2):
    pair = (seeds[i], seeds[i+1])
    pair_range = range(pair[0], pair[0] + pair[1])
    paired_list.append(pair_range)

seed_to_soil = ranges_res['seed-to-soil map:']
new = defaultdict(set)
for m, r in ranges_res.items():
    for p in paired_list:
        for g in r:
            if p.start in g[0]:
                new[m].add(g[0])


res_2 = defaultdict(list)
for p in paired_list:
    print(p)
    for i in p:
        res_1[i] = get_seeds(i, ranges_res.keys(), ranges_res)

print(minimum_location(res_2))