def process(file):
    with open(file) as f:
        counter = 0
        pointer = 50
        for line in f:
            direction = line[:1]
            distance = int(line[1:])

            # simple case for rotations that are more than a full rotation
            counter += distance // 100
            distance %= 100

            pre_mod_pointer = 0
            if direction == "L":
                pre_mod_pointer = pointer - distance
            elif direction == "R":
                pre_mod_pointer = pointer + distance
            else:
                print("what the fuck is going on here")

            if (pre_mod_pointer % 100) == 0:
                # we're going to land on zero
                counter += 1
            elif (pointer != 0) and (pre_mod_pointer > 99 or pre_mod_pointer < 0):
                # we're not currently on zero but we're going to pass over it
                counter += 1

            pointer = pre_mod_pointer % 100
        return counter


test_val = process("test.txt")
print(test_val)
assert test_val == 6
# print(process("data.txt"))
