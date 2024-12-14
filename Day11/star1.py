with open("data.txt") as f:
    stones = f.readline().split()

    for i in range(25):
        # print(stones)
        temp_stones = []
        for stone in stones:
            if stone == "0":
                temp_stones.append("1")
            elif len(stone) % 2 == 0:
                temp_stones.append(str(int(stone[: len(stone) // 2])))
                temp_stones.append(str(int(stone[len(stone) // 2 :])))
            else:
                temp_stones.append(str(int(stone) * 2024))
        stones = temp_stones
    # print(stones)
    print(len(stones))
