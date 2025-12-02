def is_invalid(num: int):
    str_num = str(num)

    for i in range(1, (len(str_num) // 2) + 1):
        equal = True
        chunk = str_num[:i]
        for j in range(i, len(str_num), i):
            if chunk == str_num[j : j + i]:
                continue
            equal = False
            break
        if equal:
            return True
    return False


def process(file):
    total = 0
    with open(file) as f:
        ranges = f.readline().strip().split(",")
        for num_range in ranges:
            start, end = num_range.split("-")
            for i in range(int(start), int(end) + 1):
                if is_invalid(i):
                    # print(f"{i} is invalid")
                    total += i
    return total


assert is_invalid(11)
assert is_invalid(22)
assert is_invalid(99)
assert is_invalid(111)
assert is_invalid(999)
assert is_invalid(1010)

assert process("test.txt") == 4174379265
print(process("data.txt"))
