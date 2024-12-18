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

def solve(start, end):
    heap = [(0, start[0], start[1], 0)]  # (score, y, x, direction)
    scores = {}

    while heap:
        score, y, x, direction = heapq.heappop(heap)

        # Stop early if we reach the endpoint with the best score
        if (y, x) == end:
            return score

        # Skip if this state was visited with a better score
        if (y, x, direction) in scores and scores[(y, x, direction)] <= score:
            continue

        # Record the best score for this state
        scores[(y, x, direction)] = score

        # Move forward in the current direction
        dy, dx = directions[direction]
        if maze[y + dy][x + dx] in (".", "E"):
            heapq.heappush(heap, (score + 1, y + dy, x + dx, direction))

        # Try turning left
        heapq.heappush(heap, (score + 1000, y, x, (direction + 1) % 4))

        # Try turning right
        heapq.heappush(heap, (score + 1000, y, x, (direction - 1) % 4))


with open("data.txt") as f:
    for line in f:
        maze.append(list(line.strip()))
        
    start, end = find_start_and_end()
        
    # print_maze()
    print(solve((start[0], start[1], 2), end))
        
