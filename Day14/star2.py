import os
import time
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
        
        x,y = robot_movement_after_seconds_eff(x,y,vx,vy,8000)
        
        robots.append([x,y,vx,vy])
    
    loop = 8000
    while True:
        board = [["."] * board_x for _ in range(board_y)]
        for robot in robots:
            x,y,vx,vy = robot
            robot[0], robot[1] = move_robot(x,y,vx,vy)
            
            try:
                board[y][x] = "X"
            except:
                raise Exception(y,x, "out of range")
            
        
        for line in board:
            print("".join(line))
        print(f"{loop=}")
        time.sleep(.1)
        loop += 1
        os.system("clear")
