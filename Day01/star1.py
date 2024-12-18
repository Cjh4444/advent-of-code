list1 = []
list2 = []
with open("data.txt") as f:
    for line in f:
        nums = line.split()
        list1.append(int(nums[0]))
        list2.append(int(nums[1]))

    difference = 0

    for i, j in zip(sorted(list1), sorted(list2)):
        difference += abs(i - j)
    print(difference)
