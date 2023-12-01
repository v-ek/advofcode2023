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
            print(f"left: {line[idx]}")
            left = line[idx]
        if line[-idx-1].isdigit() and not right:
            print(f"right: {line[-idx-1]}")
            right = line[-idx-1]

print(numbers[-10:])
print(sum(numbers))