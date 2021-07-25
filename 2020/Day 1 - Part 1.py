input1 = open("inputs/Day1Input.txt", "r")
for line in input:
    input2 = open("inputs/Day1Input.txt", "r")
    for line2 in input2:
        sum = int(line) + int(line2)
        if sum == 2020:
            product = int(line) * int(line2)
    input2.close()

print(product)


