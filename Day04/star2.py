def roll_at_position(map, row, col) -> bool:
    if (row > len(map) - 1 or row < 0) or (col > len(map[row]) - 1 or col < 0):
        return False

    return map[row][col] == "@"


def num_accessible(map: list[list[str]]) -> int:
    kernel = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    num_accessible = 0
    for row in range(len(map)):
        for col in range(len(map[row])):
            if not roll_at_position(map, row, col):
                continue

            kernel_results = [
                roll_at_position(map, row + pos[0], col + pos[1]) for pos in kernel
            ]
            num_rolls = sum(kernel_results)

            if num_rolls < 4:
                num_accessible += 1
                map[row][col] = "."

    return num_accessible


def process(file):
    with open(file) as f:
        map = [list(line.strip()) for line in f]

        total = 0

        while rolls_accessible := num_accessible(map):
            total += rolls_accessible

        return total


assert process("test.txt") == 43
print(process("data.txt"))
