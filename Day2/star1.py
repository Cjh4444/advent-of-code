def is_invalid(num: int):
    str_num = str(num)

    if len(str_num) % 2 == 1:
        return False

    first_half = str_num[0 : (len(str_num) // 2)]
    second_half = str_num[(len(str_num) // 2) : len(str_num)]

    return first_half == second_half


def process(file):
    total = 0
    with open(file) as f:
        ranges = f.readline().strip().split(",")
        for num_range in ranges:
            start, end = num_range.split("-")
            for i in range(int(start), int(end) + 1):
                if is_invalid(i):
                    total += i
    return total


assert process("test.txt") == 1227775554
print(process("data.txt"))
