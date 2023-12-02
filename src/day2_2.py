with open("inputs/day2_input.txt") as file:
    lines = [line.strip() for line in file.readlines()]

bag_counts = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

powers = []
for line in lines:
    power = 1
    preamble, games_str = line.split(":")
    id = preamble.split(" ")[-1]
    games = [game.strip() for game in games_str.replace(";", ",").strip().split(",")]
    for color in bag_counts.keys():
        power *= max((int(game.split(" ")[0]) for game in games if game.split(" ")[1] == color))
    powers.append(power)

print(sum(powers))