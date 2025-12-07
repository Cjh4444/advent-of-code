def prod(nums: list[int]):
    product = nums[0]
    for num in nums[1:]:
        product *= num
    return product


symbol_to_function = {"*": prod, "+": sum}


def process(file):
    with open(file) as f:
        data = f.readlines()
        data = [line[:-1] for line in data]

        problems = [[]]
        total = 0
        skip_next = False
        for i in range(len(data[0]) - 1, -1, -1):
            if skip_next:
                skip_next = False
                continue
            num = "".join(line[i] for line in data[:-1])
            problems[len(problems) - 1].append(int(num))

            if data[-1][i] != " ":
                total += symbol_to_function[data[-1][i]](problems[len(problems) - 1])
                problems.append([])
                skip_next = True
        problems.pop()

        print(total)
        return total


assert process("test.txt") == 3263827
process("data.txt")
