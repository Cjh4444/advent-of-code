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
            if space == "O":
                total += y_idx * 100 + x_idx
    return total

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
        elif space_ahead == "O":
            while (space_ahead == "O"):
                space_ahead_coord[0] += d[0]
                space_ahead_coord[1] += d[1]
                space_ahead = board[space_ahead_coord[0]][space_ahead_coord[1]]
            
            if space_ahead == ".":
                board[robot_y][robot_x] = "."
                board[robot_y + d[0]][robot_x + d[1]] = "@"
                robot_y, robot_x = robot_y + d[0], robot_x + d[1]
                board[space_ahead_coord[0]][space_ahead_coord[1]] = "O"
            else:
                continue        
                    
print(f"{calc_board_total()=}")
        
        
    
