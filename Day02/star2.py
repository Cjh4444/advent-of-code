num_safe = 0


def check_safe(nums):
    change_index = -1
    if nums[0] < nums[1]:
        for idx, (i, j) in enumerate(zip(nums, nums[1:])):
            if i >= j or i + 3 < j:
                # print(f"{i} to {j} is not safe!")
                change_index = idx
                break
    else:
        for idx, (i, j) in enumerate(zip(nums, nums[1:])):
            if i <= j or i > j + 3:
                # print(f"{i} to {j} is not safe!")
                change_index = idx
                break
    return change_index


with open("data.txt") as f:
    for line in f:
        nums = [int(num) for num in line.split()]

        safe = True

        old_idx = check_safe(nums)
        if old_idx != -1:
            print(f"{nums} is not safe", end="\n   ")
            new_nums_idx_pop = nums
            new_nums_idx_pop_plus_one = nums

            new_nums_idx_pop.pop(old_idx)
            idx = check_safe(nums)
            if idx == -1:
                # print(f"{nums} is safe if {old_idx} is removed")
                num_safe += 1
            else:
                try:
                    new_nums_idx_pop_plus_one.pop(old_idx + 1)
                    idx = check_safe(nums)
                    if idx == -1:
                        # print(f"{nums} is safe if {old_idx} is removed")
                        num_safe += 1
                except:
                    pass
            # else:
            #     print(f"{nums} is not safe")
        else:
            # print(f"{nums} is safe")
            num_safe += 1


print(num_safe)
