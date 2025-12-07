def prod(nums: list[int]):
    product = nums[0]
    for num in nums[1:]:
        product *= num
    return product


def process(file):
    with open(file) as f:
        data = f.readlines()

        symbols = list(data.pop().strip().replace(" ", ""))

        problems = []

        first_row = True
        for line in data:
            nums = [int(num) for num in line.strip().split()]
            if first_row:
                for num in nums:
                    problems.append([num])
                first_row = False
            else:
                for num, problem in zip(nums, problems):
                    problem.append(num)

        total = 0
        for symbol, problem in zip(symbols, problems):
            if symbol == "*":
                total += prod(problem)
            elif symbol == "+":
                total += sum(problem)

        print(total)
        return total


assert process("test.txt") == 4277556
process("data.txt")
