with open("inputs/day5_test.txt") as file:
    lines = [line.strip() for line in file.readlines()]

maps = {}
seeds = []
seeds_with_paths = {}
for line in lines:
    if line and line[0].isdigit():
        dest_start, source_start, length = [int(entry) for entry in line.split(" ")]
        for idx in range(length):
            maps[map_type][source_start + idx] = dest_start + idx
    elif line.startswith("seeds:"):
        seeds = [int(number) for number in line.split(":")[1].split(" ") if number != ""]
    elif line.startswith(" "):
        continue
    elif line.endswith("map:"):
        map_type = line.split(" ")[0]
        maps[map_type] = {}  # initialize an empty dict

seeds_with_paths = {}
for seed in seeds:
    seeds_with_paths[seed] = {}
    previous_mapped_value = seed
    for map_type, value_map in maps.items():
        source_type, _, target_type = map_type.split("-")
        seeds_with_paths[seed][target_type] = value_map.get(previous_mapped_value, previous_mapped_value)
        previous_mapped_value = seeds_with_paths[seed][target_type]

print(min((value["location"] for value in seeds_with_paths.values())))