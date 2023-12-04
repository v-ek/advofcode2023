with open("inputs/day3_input.txt") as file:
    lines = [line.strip() for line in file.readlines()]


def compute_neighborhood(coordinates_list: list[tuple[int, int]], max_x: int, max_y: int):
    neighborhood = set()
    neighbors = (
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1), 
        (1, -1),
        (1, 0), 
        (1, 1), 
    )
    for c_x, c_y in coordinates_list:
        for d_x, d_y in neighbors:
            new_coord = (c_x + d_x, c_y + d_y)
            if new_coord[0] < 0 or new_coord[0] > max_x or new_coord[1] < 0 or new_coord[1] > max_y:
                continue
            else:
                neighborhood.add(new_coord)
    neighborhood -= set(coordinates_list)
    return neighborhood

gear_ratios_to_sum = []
asterisk_coordinates = set()
numbers_w_neighborhoods = []
# cordinates to the left and down (left-handed?)
for row_index in range(depth := len(lines)):
    curr_digits = []
    curr_number_coordinates = []
    line = lines[row_index]
    for col_index in range(width := len(line)): 
        curr_coordinates = (col_index, row_index)
        char = line[col_index]
        if char.isdigit():
            curr_digits.append(char)
            curr_number_coordinates.append(curr_coordinates)
        else:
            if curr_number_coordinates:
                curr_number = int("".join(curr_digits))
                numbers_w_neighborhoods.append((curr_number, compute_neighborhood(curr_number_coordinates, width, depth)))
                curr_digits = []
                curr_number_coordinates = []
            if char == ".":
                continue
            elif char == "*":
                asterisk_coordinates.add(curr_coordinates)
        # Special case, number at the edge
        if col_index == width - 1:
            if curr_number_coordinates:
                curr_number = int("".join(curr_digits))
                numbers_w_neighborhoods.append((curr_number, compute_neighborhood(curr_number_coordinates, width, depth)))
                curr_digits = []
                curr_number_coordinates = []


for coordinate in asterisk_coordinates:
    candidate_gear = [entry[0] for entry in numbers_w_neighborhoods if coordinate in entry[1]]
    if len(candidate_gear) == 2:
        gear_ratios_to_sum.append(candidate_gear[0] * candidate_gear[1])

print(sum(gear_ratios_to_sum))