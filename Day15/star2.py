board = []
moves = []

def print_board():
    for line in board:
        print("".join(line))
    print()

def find_robot():
    for y_idx, row in enumerate(board):
        for x_idx, space in enumerate(row):
            if space == "@":
                return y_idx, x_idx
    return -1, -1

def calc_board_total():
    total = 0
    for y_idx, row in enumerate(board):
        for x_idx, space in enumerate(row):
            if space == "[":
                total += y_idx * 100 + x_idx
    return total

def widen_board():
    wide_board = []
    for r in range(len(board)):
        wide_board.append([])
        for space in board[r]:
            if space == "#":
                wide_board[r].append("#")
                wide_board[r].append("#")
            elif space == "O":
                wide_board[r].append("[")
                wide_board[r].append("]")
            elif space == ".":
                wide_board[r].append(".")
                wide_board[r].append(".")
            elif space == "@":
                wide_board[r].append("@")
                wide_board[r].append(".")
    return wide_board

def push_hoz(d,y,x):
    if d[1] == 0:
        return
    
    while board[y][x] == "]" or board[y][x] == "[":
        x += d[1]
    
    if board[y][x] == ".":
        if d[1] < 0:
            board[y][x] = "["
        elif d[1]:
            board[y][x] = "]"
        
        while board[y][x] != "@":
            x -= d[1]
            if board[y][x] == "[":
                board[y][x] = "]"
            elif board[y][x] == "]":
                board[y][x] = "["
        board[y][x] = "."
        board[y][x + d[1]] = "@"
        return True
    else:
        return False

def push_vert(d,ry,rx):
    all_coords = []
    box_coords = []
    
    box_coords.append((ry + d[0], rx, board[ry + d[0]][rx]))
        
    if board[ry + d[0]][rx] == "[":
        box_coords.append((ry + d[0], rx + 1, "]"))
    else:
        box_coords.append((ry + d[0], rx - 1, "["))

    all_coords.append(box_coords)
    
    while len(box_coords):
        new_box_coords = []
        for coord in box_coords:
            if board[coord[0] + d[0]][coord[1]] == "#":
                return False
            if board[coord[0] + d[0]][coord[1]] == ".":
                continue
            
            new_box_coords.append((coord[0] + d[0], coord[1], board[coord[0] + d[0]][coord[1]]))
            
            if board[coord[0] + d[0]][coord[1]] == "[":
                new_box_coords.append((coord[0] + d[0], coord[1] + 1, "]"))
            else:
                new_box_coords.append((coord[0] + d[0], coord[1] - 1, "["))
            
        box_coords = new_box_coords
        all_coords.append(box_coords)
    
    for i in all_coords:
        for j in i:
            board[j[0]][j[1]] = "."
    
    for i in all_coords:
        for j in i:
            board[j[0] + d[0]][j[1]] = j[2]
    
    board[ry][rx] = "."
    board[ry + d[0]][rx] = "@"
    return True
        
            
            
with open("data.txt") as f:
    board_finished = False
    for line in f:
        if line == "\n":
            board_finished = True
            continue
            
        if not board_finished:
            board.append(list(line.strip()))
        else:
            moves.extend(list(line.strip()))
    
    print_board()
    board = widen_board()
    print_board()
    
    robot_y, robot_x = find_robot()
    
    directions = {
        "^": (-1,0),
        "v": (1,0),
        "<": (0,-1),
        ">": (0,1)
    }
        
    for move in moves:
        d = directions[move]        
        space_ahead_coord = [robot_y + d[0],robot_x + d[1]]
        space_ahead = board[space_ahead_coord[0]][space_ahead_coord[1]]
        
        if space_ahead == "#":
            continue
        elif space_ahead == ".":
            board[robot_y][robot_x] = "."
            board[robot_y + d[0]][robot_x + d[1]] = "@"
            robot_y, robot_x = robot_y + d[0], robot_x + d[1]
        elif space_ahead == "[" or space_ahead == "]":
            if d[0] == 0:
                if push_hoz(d,space_ahead_coord[0],space_ahead_coord[1]):
                    robot_y, robot_x = robot_y + d[0], robot_x + d[1]
            elif d[1] == 0:
                if push_vert(d,robot_y, robot_x):
                    robot_y, robot_x = robot_y + d[0], robot_x + d[1]
        # print_board()
                    
print(f"{calc_board_total()=}")
        
        
    
