from collections import deque


def press_button(lights: str, button: tuple[int]) -> str:
    new_lights = list(lights)

    for idx in button:
        new_lights[idx] = "#" if new_lights[idx] == "." else "."

    return "".join(new_lights)


def find_combination(machine):
    goal = machine[0]
    buttons = machine[1]
    blank = "." * len(machine[0])

    if goal == blank:
        return [goal]

    paths = deque([[blank]])

    while True:
        path = paths.popleft()

        if path[0] == blank and len(path) > 2:
            continue

        for button in buttons:
            new_path = path[:]

            new_path[0] = press_button(new_path[0], button)
            new_path.append(button)

            if new_path[0] == goal:
                print(f"found path, {new_path}")
                return new_path
            paths.append(new_path)


def process(file):
    with open(file) as f:
        machines = []

        for line in f:
            data = line.split()

            buttons = [
                tuple(map(int, button[1:-1].split(","))) for button in data[1:-1]
            ]
            # joltages = tuple(map(int, data[-1][1:-1].split(",")))

            machines.append([data[0][1:-1], buttons])
            # machines.append([data[0][1:-1], buttons, joltages])

        ret = sum(len(find_combination(machine)[1:]) for machine in machines)
        print(ret)
        return ret


assert process("test.txt") == 7
process("data.txt")
