with open("inputs/day2_input.txt") as file:
    lines = [line.strip() for line in file.readlines()]

bag_counts = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

valid_ids = []
for line in lines:
    continue_ = False
    preamble, games_str = line.split(":")
    id = preamble.split(" ")[-1]
    games = [game.strip() for game in games_str.replace(";", ",").strip().split(",")]
    for color in bag_counts.keys():
        if max((int(game.split(" ")[0]) for game in games if game.split(" ")[1] == color)) > bag_counts[color]:
            continue_ = True
            break

    if continue_:
        continue
    valid_ids.append(int(id))
print(sum(valid_ids))