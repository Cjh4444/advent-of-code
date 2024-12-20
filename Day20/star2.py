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
    raise Exception("None")

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
    
    print(len(path))
    
    for start_idx, curr_coord in enumerate(path):
        print(start_idx)
        for end_idx, end_coord in enumerate(path[start_idx:]):
            dist = abs(end_coord[0] - curr_coord[0]) + abs(end_coord[1] - curr_coord[1])            
            if dist <= 20:
                saved = end_idx - dist
                if saved in num_sols_seconds:
                    num_sols_seconds[saved] = num_sols_seconds[saved] + 1
                else:
                    num_sols_seconds[saved] = 1
    
    # print(num_sols_seconds)
    # print(f"{num_sols_seconds[50]=}")
    # print(f"{num_sols_seconds[52]=}")
    # print(f"{num_sols_seconds[54]=}")
    # print(f"{num_sols_seconds[56]=}")
    # print(f"{num_sols_seconds[58]=}")
    # print(f"{num_sols_seconds[60]=}")
    # print(f"{num_sols_seconds[62]=}")
    # print(f"{num_sols_seconds[64]=}")
    # print(f"{num_sols_seconds[66]=}")
    # print(f"{num_sols_seconds[68]=}")
    # print(f"{num_sols_seconds[70]=}")
    # print(f"{num_sols_seconds[72]=}")
    # print(f"{num_sols_seconds[74]=}")
    # print(f"{num_sols_seconds[76]=}")
    
    
    total = 0
    for key in num_sols_seconds:
        if key >= 100:
            total += num_sols_seconds[key]
    print(total)