from collections import deque

maze = []

def print_maze():
    for line in maze:
        print("".join(line))
    print()

def find_start_and_end():
    sy = sx = ey = ex = -1
    
    for y_idx, row in enumerate(maze):
        for x_idx, space in enumerate(row):
            if space == "S":
                sy = y_idx
                sx = x_idx
            if space == "E":
                ey = y_idx
                ex = x_idx
    return (sy,sx), (ey,ex)

directions = [(1,0), (-1,0), (0,1), (0,-1)]

def solve(start, end) -> list:
    
    stack = deque([start])
    visited = set([start])
    parent = {}

    while stack:
        current = stack.pop()

        if current == end:
            path = [current]
            while current in parent:
                current = parent[current]
                path.append(current)
            return path[::-1]

        for d in directions:
            ny, nx = current[0] + d[0], current[1] + d[1]

            if ny in range(len(maze)) and ny in range(len(maze[0])) and \
               maze[ny][nx] in (".","E") and (ny, nx) not in visited:
                stack.append((ny, nx))
                visited.add((ny, nx))
                parent[(ny, nx)] = current
    return None

with open("data.txt") as f:
    for line in f:
        maze.append(list(line.strip()))
    
    print_maze()
    
    start, end = find_start_and_end()
    
    print(start, end)
        
    path = solve(start, end)
    
    num_sols_seconds: dict[int, int] = {}
    print("solved")
    
    idx_lookup = {}
    
    for idx, coord in enumerate(path):
        idx_lookup[coord] = idx
    
    for idx, coord in enumerate(path): # type: ignore
        for d in directions:
            cy, cx = coord[0] + d[0] * 2, coord[1] + d[1] * 2 
            if (cy, cx) in idx_lookup:
                t = idx_lookup[(cy, cx)]
                if t < idx:
                    continue
                
                saved = t - idx - 2
                
                if saved in num_sols_seconds:
                    num_sols_seconds[saved] = num_sols_seconds[saved] + 1
                else:
                    num_sols_seconds[saved] = 1
    
    # print(num_sols_seconds)
    
    total = 0
    for key in num_sols_seconds:
        if key >= 100:
            total += num_sols_seconds[key]
    print(total)