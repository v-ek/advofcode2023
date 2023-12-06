with open("inputs/day4_input.txt") as file:
    lines = [line.strip() for line in file.readlines()]

number_of_cards = len(lines)
card_counts = {idx: 1 for idx in range(1, number_of_cards + 1)}

for line_number in range(1, number_of_cards + 1):
    line = lines[line_number - 1]
    preamble, numbers = line.split(":")
    card_numbers_str, correct_numbers_str = numbers.split("|")
    card_numbers = [number for number in card_numbers_str.split(" ") if number != ""]
    correct_numbers = [number for number in correct_numbers_str.split(" ") if number != ""]
    winning_numbers = [number for number in card_numbers if number in correct_numbers]
    for number in range(1, len(winning_numbers) + 1):
        if line_number + number > number_of_cards:
            break
        else:
            card_counts[line_number + number] += card_counts[line_number]

print(sum(card_counts.values()))