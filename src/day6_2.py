with open("inputs/day6_input.txt") as file:
    lines = [line.strip() for line in file.readlines()]

for line in lines:
    if line.startswith("Time:"):
       time = int("".join([number for number in line.split(":")[1].split(" ") if number != ""]))
    elif line.startswith("Dist"):
        distance = int("".join([number for number in line.split(":")[1].split(" ") if number != ""]))

for speed in range(0, time):
    if speed * (time - speed) > distance:
        min_speed = speed
        break

for speed in range(time, 0, -1):
    if speed * (time - speed) > distance:
        max_speed = speed
        break

print(max_speed - min_speed +1) 
    