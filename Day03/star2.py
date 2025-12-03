def pack_nums(voltages: list[int]):
    ret = 0
    for idx, num in enumerate(reversed(voltages)):
        ret += num * pow(10, idx)
    return ret


def largest_joltage(batteries: list[int]):
    largest_joltage = batteries[:12]
    suffix = batteries[12:]
    for i in suffix:
        for j in range(len(largest_joltage) - 1):
            if largest_joltage[j] < largest_joltage[j + 1]:
                largest_joltage.pop(j)
                break

        largest_joltage.append(i)
        if len(largest_joltage) > 12:
            largest_joltage.remove(min(largest_joltage))

    return pack_nums(largest_joltage)


def process(file):
    with open(file) as f:
        return sum(largest_joltage([int(num) for num in bank.strip()]) for bank in f)


assert largest_joltage([int(num) for num in "987654321111111"]) == 987654321111
assert largest_joltage([int(num) for num in "811111111111119"]) == 811111111119
assert largest_joltage([int(num) for num in "234234234234278"]) == 434234234278
assert largest_joltage([int(num) for num in "818181911112111"]) == 888911112111
assert process("test.txt") == 3121910778619
print(process("data.txt"))
