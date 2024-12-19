from collections import deque
patterns = []

def determine_if_pattern_makeable(goal: str):
    possible_paths = deque()
    for pattern in patterns:
        if goal.startswith(pattern):
            possible_paths.append(pattern)
    
    while possible_paths:
        path = possible_paths.popleft()
        
        if path == goal:
            return True
        
        for pattern in patterns:
            if goal.startswith(path + pattern):
                possible_paths.append(path + pattern)
    
    return False

def determine_if_pattern_makeable_dp(goal: str) -> bool:
    n = len(goal)
    dp = [False] * (n + 1)
    dp[0] = True
    
    for i in range(1, n + 1):
        for pattern in patterns:
            if i >= len(pattern) and dp[i - len(pattern)]:
                if goal[i - len(pattern):i] == pattern:
                    dp[i] = True
                    break

    return dp[n]

print("alphabet".startswith("alph"))

with open("test.txt") as f:
    patterns = f.readline().split(",")
    patterns = [pattern.strip() for pattern in patterns]
    print(patterns)
    f.readline()
    total = 0
    for line in f:
        if determine_if_pattern_makeable(line.strip()):
            total += 1
    