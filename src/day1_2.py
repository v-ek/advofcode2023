with open("inputs/day1_input.txt") as file:
    lines = [line.strip() for line in file.readlines()]

candidates = "1 2 3 4 5 6 7 8 9 one two three four five six seven eight nine".split(" ")
two_letter_map = {
    "on": "1",
    "tw": "2",
    "th": "3",
    "fo": "4",
    "fi": "5",
    "si": "6",
    "se": "7",
    "ei": "8",
    "ni": "9",
}

numbers = []
for line in lines:
    left_index = min(filter(lambda x : x >= 0, (line.find(candidate) for candidate in candidates)))
    right_index = max(filter(lambda x : x >= 0, (line.rfind(candidate) for candidate in candidates)))
    if line[left_index].isdigit():
        left = line[left_index]
    else:
        left = two_letter_map[line[left_index:left_index+2]]
    if line[right_index].isdigit():
        right = line[right_index]
    else:
        right = two_letter_map[line[right_index:right_index+2]]
    numbers.append(int(left + right))

print(sum(numbers))