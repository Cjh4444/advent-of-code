with open("inputs/Day1Input.txt") as f:
    inputs = [int(line.strip()) for line in f]
    for line in inputs:
        for line2 in inputs:
            sum = int(line) + int(line2)
            if sum == 2020:
                product = int(line) * int(line2)
    print(product)


