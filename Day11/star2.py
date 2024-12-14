from functools import cache


def num_digits(num):
    return len(str(num))


def split_int(num, digit_count):
    divide = 10 ** (digit_count // 2)

    return (num // divide, num % divide)


@cache
def stone_result(stone: int):
    digit_count = num_digits(stone)

    if stone == 0:
        return (1,)
    elif stone == 1:
        return (2024,)
    elif digit_count % 2 == 0:
        first_half, second_half = split_int(stone, digit_count)
        return (first_half, second_half)
    else:
        return (stone * 2024,)

@cache
def stone_count_after_steps(stone: int, steps: int, memo: dict[int, int] = {}):
    if steps == 0:
        # print(stone)
        return 1

    # if stone in memo:
    #     return memo[stone]
    # else

    if stone == 0:
        return stone_count_after_steps(1, steps - 1)
        # memo[stone] = stone_count_after_steps(1, steps - 1)
        # return memo[stone]

    digit_count = num_digits(stone)
    if digit_count % 2 == 0:
        first_half, second_half = split_int(stone, digit_count)
        return (stone_count_after_steps(first_half, steps - 1) +
                stone_count_after_steps(second_half, steps - 1))
        # memo[stone] = (
        #     stone_count_after_steps(first_half, steps - 1) + 
        #     stone_count_after_steps(second_half, steps - 1)
        # )
        # return memo[stone]
    
    return stone_count_after_steps(stone * 2024, steps - 1)

    # memo[stone] = stone_count_after_steps(stone * 2024, steps - 1)
    # return memo[stone]



with open("data.txt") as f:
    stones = [int(x) for x in f.readline().split()]

    total = 0
    memo = []
    for stone in stones:
        total += stone_count_after_steps(stone, 75)

    print(total)
