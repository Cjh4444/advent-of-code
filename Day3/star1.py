import re


def convert_mul_to_result(mul_string):
    temp = mul_string.split("(")
    temp = temp[1].split(")")
    num1, num2 = temp[0].split(",")
    return int(num1) * int(num2)


with open("data.txt") as f:
    muls = []
    for line in f:
        muls.extend(re.findall("mul\(\d+,\d+\)", line))

    print(sum([convert_mul_to_result(mul) for mul in muls]))
