with open("inputs/day6_input.txt") as file:
    lines = [line.strip() for line in file.readlines()]

times = []
distances = []
for line in lines:
    if line.startswith("Time:"):
       times = [int(number) for number in line.split(":")[1].split(" ") if number != ""]
    elif line.startswith("Dist"):
        distances = [int(number) for number in line.split(":")[1].split(" ") if number != ""]

races = list(zip(times, distances))
ways_to_win = [0] * len(races)
for idx in range(len(races)):
    race = races[idx]
    for speed in range(1, race[0]):
        distance = speed * (race[0] - speed)
        if distance > race[1]:
            ways_to_win[idx] += 1
product = 1
for way_to_win in ways_to_win:
    product *= way_to_win

print(product)
    