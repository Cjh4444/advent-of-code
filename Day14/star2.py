import os
board_x = 101
board_y = 103


def robot_movement_after_seconds_eff(x: int, y: int, vx: int, vy: int, seconds: int):
    vx_after_sec = (vx * seconds) % board_x
    vy_after_sec = (vy * seconds) % board_y
    
    final_x = (x + vx_after_sec) % board_x
    final_y = (y + vy_after_sec) % board_y
    
    return final_x, final_y

def move_robot(x: int, y: int, vx: int, vy: int):
    final_x = (x + vx) % board_x
    final_y = (y + vy) % board_y
    
    return final_x, final_y

robots = []
with open("data.txt") as f:
    for line in f:
        p, v = line.split(" ")
        
        x,y = p.split("=")[1].split(",")
        vx,vy = v.split("=")[1].split(",")
        
        x, y, vx, vy = int(x), int(y), int(vx), int(vy)
        
        robots.append([x,y,vx,vy])
    
    loop = 0
    while True:
        board = [["."] * board_x for _ in range(board_y)]
        for robot in robots:
            x,y,vx,vy = robot
            board[y][x] = "X"
            robot[1], robot[0] = move_robot(x,y,vx,vy)
        
        for line in board:
            print("".join(line))
        print(f"{loop=}")
        loop += 1
        os.system("clear")