input1 = open("inputs/Day1Input.txt", "r")
for line in input1:
    input2 = open("inputs/Day1Input.txt", "r")
    for line2 in input2:
        input3 = open("inputs/Day1Input.txt", "r")
        for line3 in input3:
            sum = int(line) + int(line2) + int(line3)
            if sum == 2020:
                product = int(line) * int(line2) * int(line3)
                break
        input3.close()
    input2.close()

print(product)


