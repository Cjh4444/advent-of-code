from collections import Counter

list1 = []
list2 = []
with open("data.txt") as f:
    for line in f:
        nums = line.split()
        list1.append(int(nums[0]))
        list2.append(int(nums[1]))

counter_2 = Counter(list2)

similarity = 0

for i in list1:
    similarity += i * counter_2.get(i, 0)

print(similarity)
