def pack_nums(voltages: list[int]):
    ret = 0
    for idx, num in enumerate(reversed(voltages)):
        ret += num * pow(10, idx)
    return ret


def largest_joltage(batteries: list[int], length):
    largest_joltage = batteries[:length]
    suffix = batteries[length:]
    for i in suffix:
        for j in range(len(largest_joltage) - 1):
            if largest_joltage[j] < largest_joltage[j + 1]:
                largest_joltage.pop(j)
                break

        largest_joltage.append(i)
        if len(largest_joltage) > length:
            largest_joltage.remove(min(largest_joltage))

    return pack_nums(largest_joltage)


def process(file, length):
    with open(file) as f:
        return sum(
            largest_joltage([int(num) for num in bank.strip()], length=length)
            for bank in f
        )


assert largest_joltage([int(num) for num in "987654321111111"], 12) == 987654321111
assert largest_joltage([int(num) for num in "811111111111119"], 12) == 811111111119
assert largest_joltage([int(num) for num in "234234234234278"], 12) == 434234234278
assert largest_joltage([int(num) for num in "818181911112111"], 12) == 888911112111
assert process("test.txt", 2) == 357
assert process("test.txt", 12) == 3121910778619
print(process("data.txt", 12))
