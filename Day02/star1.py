num_safe = 0

with open("data.txt") as f:
    for line in f:
        nums = [int(num) for num in line.split()]

        safe = True
        if nums[0] < nums[1]:
            for i, j in zip(nums, nums[1:]):
                if i >= j or i + 3 < j:
                    # print(f"{i} to {j} is not safe!")
                    safe = False
                    break
        else:
            for i, j in zip(nums, nums[1:]):
                if i <= j or i > j + 3:
                    # print(f"{i} to {j} is not safe!")
                    safe = False
                    break

        if safe:
            # print(f"{nums} is safe")
            num_safe += 1
        # else:
        #     # print(f"{nums} is not safe")

print(num_safe)
