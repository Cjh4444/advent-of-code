with open("inputs/Day1Input.txt") as f:
    inputs = [int(line.strip()) for line in f]
    for line in inputs:
        for line2 in inputs:
            for line3 in inputs:
                sum = int(line) + int(line2) + int(line3)
                if sum == 2020:
                    product = int(line) * int(line2) * int(line3)
                    break
    print(product)


