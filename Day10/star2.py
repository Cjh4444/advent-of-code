import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds


def pad_button(button, size):
    ret = [0] * size

    for val in button:
        ret[val] = 1

    return ret


def find_combination(machine):
    A = np.array(machine[1])
    b = np.array(machine[0])

    A_eq = A.T
    c = np.ones(A_eq.shape[1])

    constraints = LinearConstraint(A_eq, b, b)
    bounds = Bounds(0, np.inf)
    integrality = np.ones_like(c, dtype=int)

    result = milp(c=c, constraints=constraints, bounds=bounds, integrality=integrality)

    return result.fun


def process(file):
    with open(file) as f:
        machines = []

        for line in f:
            data = line.split()

            buttons = [list(map(int, button[1:-1].split(","))) for button in data[1:-1]]
            joltages = list(map(int, data[-1][1:-1].split(",")))

            buttons = [pad_button(button, len(joltages)) for button in buttons]

            # machines.append([data[0][1:-1], buttons])ç
            machines.append([joltages, buttons])

        ret = sum(find_combination(machine) for machine in machines)
        print(ret)
        return ret


assert process("test.txt") == 33
process("data.txt")
