import heapq

maze = []
start = ()
end = ()

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


"""
0 - East (right)
1 - South (down)
2 - West (left)
3 - North (up)
"""
directions = {
        0: (0,1),
        1: (-1,0),
        2: (0,-1),
        3: (1,0)
    }

def solve(start: tuple[int, int], end: tuple[int, int]) -> tuple[int, set[tuple[int, int]]]:
    heap = [(0, start[0], start[1], 0, set())]  # (score, y, x, direction, visited cells)
    scores = {}
    best_score = float('inf')
    best_paths_cells = set()

    while heap:
        score, y, x, direction, visited = heapq.heappop(heap)

        # Add the current cell to the visited set
        visited = visited | {(y, x)}

        # If we reached the endpoint
        if (y, x) == end:
            if score < best_score:
                best_score = score
                best_paths_cells = visited  # reset best paths with new score
            elif score == best_score:
                best_paths_cells |= visited  # add cells of this path to best paths
            continue

        # Skip if this state was visited with a better or equal score
        if (y, x, direction) in scores and scores[(y, x, direction)] < score:
            continue

        # Record the best score for this state
        scores[(y, x, direction)] = score

        # Move forward in the current direction
        dy, dx = directions[direction]
        if maze[y + dy][x + dx] in (".", "E"):
            heapq.heappush(heap, (score + 1, y + dy, x + dx, direction, visited))

        # Try turning left (turning cost is 1000)
        heapq.heappush(heap, (score + 1000, y, x, (direction + 1) % 4, visited))

        # Try turning right (turning cost is 1000)
        heapq.heappush(heap, (score + 1000, y, x, (direction - 1) % 4, visited))

    return best_score, best_paths_cells


with open("data.txt") as f:
    for line in f:
        maze.append(list(line.strip()))
        
    start, end = find_start_and_end()
        
    # print_maze()
    score, res = solve(start, end)
    print(score, len(res))
        
