with open("inputs/day5_input.txt") as file:
    lines = [line.strip() for line in file.readlines()]

maps = {}
seeds_with_paths = {}
map_type = None
for line in lines:
    if line.startswith("seeds:"):
        seeds_with_paths = {int(number): [int(number)] for number in line.split(":")[1].split(" ") if number != ""}
    elif line.endswith("map:"):
        map_type = line.split(" ")[0]
        maps[map_type] = []
    elif line and line[0].isdigit():
        maps[map_type].append(tuple([int(entry) for entry in line.split(" ")]))
    elif not line and map_type:
        for seed, path in seeds_with_paths.items():
            for map in maps[map_type]:
                if path[-1] >= map[1] and path[-1] <= map[1] + map[2]:
                    mapped_value = path[-1] + map[0] - map[1]
                    path.append(mapped_value)
                    break
            else:
                path.append(path[-1])  # Maps to the same value
else:
    for seed, path in seeds_with_paths.items():
        for map in maps[map_type]:
            if path[-1] >= map[1] and path[-1] <= map[1] + map[2]:
                mapped_value = path[-1] + map[0] - map[1]
                path.append(mapped_value)
                break
        else:
            path.append(path[-1])  # Maps to the same value

print(seeds_with_paths)
print(min((path[-1] for path in seeds_with_paths.values())))