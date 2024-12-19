from collections import deque
patterns = []

def count_combinations_to_make_goal(goal: str) -> int:
    n = len(goal)
    dp = [0] * (n + 1)
    dp[0] = 1
    
    for i in range(1, n + 1):
        for pattern in patterns:
            if i >= len(pattern) and goal[i - len(pattern):i] == pattern:
                dp[i] += dp[i - len(pattern)]
    
    return dp[n]

with open("test.txt") as f:
    patterns = f.readline().split(",")
    patterns = [pattern.strip() for pattern in patterns]
    f.readline()
    total = 0
    for i, line in enumerate(f):
        total += count_combinations_to_make_goal(line.strip())
    print(total)