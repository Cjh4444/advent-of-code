def operations(nums, goal, curr_num, count, operator):
    count += 1

    if operator == 0:
        curr_num *= nums[count]
    elif operator == 1:
        curr_num += nums[count]
    elif operator == 2:
        curr_num = int(str(curr_num) + str(nums[count]))

    if curr_num > goal:
        return False

    if count == len(nums) - 1:
        return goal == curr_num

    return (
        operations(nums, goal, curr_num, count, 0)
        or operations(nums, goal, curr_num, count, 1)
        or operations(nums, goal, curr_num, count, 2)
    )


total_results = 0

with open("data.txt") as f:
    for line in f:
        line = line.split(":")
        goal_num = int(line[0])
        nums = [int(x) for x in line[1].split()]
        total_results += (
            goal_num
            if operations(nums, goal_num, nums[0], 0, 0)
            or operations(nums, goal_num, nums[0], 0, 1)
            or operations(nums, goal_num, nums[0], 0, 2)
            else 0
        )

print(total_results)
