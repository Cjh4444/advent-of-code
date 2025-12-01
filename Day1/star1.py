def process(file):
    with open(file) as f:
        counter = 0
        pointer = 50
        for line in f:
            direction = line[:1]
            distance = int(line[1:])

            if direction == "L":
                pointer = (pointer - distance) % 100
            elif direction == "R":
                pointer = (pointer + distance) % 100
            else:
                print("what the fuck is going on here")

            if pointer == 0:
                counter += 1
        return counter


assert process("test.txt") == 3
print(process("data.txt"))
