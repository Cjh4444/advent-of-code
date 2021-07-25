input = open("inputs/Day1Input.txt", "r")
for line in input:
    inputduplicate = open("inputs/Day1Input.txt", "r")
    for line2 in inputduplicate:
        sum = int(line) + int(line2)
        if sum == 2020:
            product = int(line) * int(line2)
    inputduplicate.close()

print(product)


