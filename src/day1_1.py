with open("inputs/day1_input.txt") as file:
    lines = [line.strip() for line in file.readlines()]

numbers = []
for line in lines:
    left = None
    right = None
    for idx in range(0, len(line) + 1):  # Worst case we find the same digit anyhow
        if left and right:
            numbers.append(int(left + right))
            break
        if line[idx].isdigit() and not left:
            left = line[idx]
        if line[-idx-1].isdigit() and not right:
            right = line[-idx-1]

print(sum(numbers))