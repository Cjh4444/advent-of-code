list_of_spots = []

with open("all_spots.txt") as f:
    for row, line in enumerate(f):
        for col, space in enumerate(line):
            if space == "X" or space == "^":
                list_of_spots.append((row, col))

print(list_of_spots)
