def largest_joltage(batteries: list[int]):
    prefix = batteries[:1]
    prefix_max = prefix[0]
    suffix = batteries[1:]
    suffix.reverse()
    suffix_max = max(suffix)
    max_num = prefix_max * 10 + suffix_max
    for i in range(len(batteries) - 2):
        val = suffix.pop()
        prefix.append(val)
        if val > prefix_max:
            prefix_max = val

        suffix_max = max(suffix)

        if prefix_max * 10 + suffix_max > max_num:
            max_num = prefix_max * 10 + suffix_max

    return max_num


def process(file):
    with open(file) as f:
        return sum(largest_joltage([int(num) for num in bank.strip()]) for bank in f)


assert process("test.txt") == 357
print(process("data.txt"))
