import re


def convert_mul_to_result(mul_string):
    temp = mul_string.split("(")
    temp = temp[1].split(")")
    num1, num2 = temp[0].split(",")
    return int(num1) * int(num2)


with open("data.txt") as f:
    muls = []
    for line in f:
        muls.extend(re.findall("mul\(\d+,\d+\)|do\(\)|don't\(\)", line))

    do = True
    total = 0
    for mul in muls:
        if mul == "do()":
            do = True
        elif mul == "don't()":
            do = False
        else:
            if do:
                total += convert_mul_to_result(mul)
    print(total)
