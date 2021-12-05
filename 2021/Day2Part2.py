RAW = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""

RAW_SPLIT = RAW.split("\n")

def fix_input_list(x):
    templist = []
    for input in x:
        templist.append(input.split())
    return templist

fixed_inputs = fix_input_list(RAW_SPLIT)

def get_position(x):
    coordinates = [0,0]
    aim = 0
    for item in x:
        if item[0] == "forward":
            coordinates[0] += int(item[1])
            coordinates[1] += (aim * int(item[1]))
        if item[0] == "down":
            aim += int(item[1])
        if item[0] == "up":
            aim -= int(item[1])
    return coordinates

def get_value(x):
    return x[0] * x[1]

assert get_value(get_position(fixed_inputs)) == 900

with open("inputs/Day2Input.txt") as f:
    inputs = [line.strip() for line in f]
    a = fix_input_list(inputs)
    print(get_value(get_position(a)))



        