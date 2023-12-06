with open("inputs/day4_input.txt") as file:
    lines = [line.strip() for line in file.readlines()]


points_list = []
for line in lines:
    preamble, numbers = line.split(":")
    card_numbers_str, correct_numbers_str = numbers.split("|")
    card_numbers = [number for number in card_numbers_str.split(" ") if number != ""]
    correct_numbers = [number for number in correct_numbers_str.split(" ") if number != ""]
    winning_numbers = [number for number in card_numbers if number in correct_numbers]
    points = int(pow(2, len(winning_numbers) - 1)) if winning_numbers else 0
    points_list.append(points)

print(sum(points_list))