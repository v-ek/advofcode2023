with open("inputs/day8_input.txt") as file:
    lines = [line.strip() for line in file.readlines()]

instruction = lines[0]
num_instructions = len(instruction)

# Build the network
network = {}
for line in lines[2:]:
    source, targets = (part.strip() for part in line.split("="))
    left_target, right_target = (part.strip() for part in targets[1:-1].split(","))
    network[source] = {"L": left_target, "R": right_target}

counter = 0
counter_trunc = 0
curr_node = "AAA"
while True:
    curr_instruction = instruction[counter_trunc]
    curr_node = network[curr_node][curr_instruction]
    counter += 1
    counter_trunc = counter % num_instructions

    if curr_node == "ZZZ":
        break

print(counter)
