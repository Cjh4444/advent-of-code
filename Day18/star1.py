from collections import deque

board = []
n = 7

for i in range(n):
    board.append([])
    for j in range(n):
        board[i].append(".")
        
def print_board():
    for row in board:
        print("".join(row))
    print()
    
def solve():
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    
    queue = deque()
    visited = set()
    queue.append((0,0,0))
    
    while queue:
        coord = queue.popleft()
        
        if (coord[0] == n - 1 and coord[1] == n - 1):
            return coord[2]
        
        for d in directions:
            if (coord[0] + d[0] in range(n) and
                coord[1] + d[1] in range(n) and
                board[coord[1] + d[1]][coord[0] + d[0]] != "#" and
                (coord[0] + d[0], coord[1] + d[1]) not in visited):
                
                queue.append((coord[0] + d[0], coord[1] + d[1], coord[2] + 1))
                visited.add((coord[0] + d[0], coord[1] + d[1]))
    return -1
    
with open("test.txt") as f:
    num_bytes = 12
    for i, line in enumerate(f):
        if i == num_bytes:
            break
        print(line)
        x, y = line.split(",")
        x, y = int(x), int(y)
        
        board[y][x] = "#"
    print(solve())
    

