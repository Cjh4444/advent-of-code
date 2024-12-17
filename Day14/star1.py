board_x = 101
board_y = 103


def robot_movement_after_seconds(x: int, y: int, vx: int, vy: int, seconds: int):
    vx_after_sec = (vx * seconds) % board_x
    vy_after_sec = (vy * seconds) % board_y
    
    final_x = (x + vx_after_sec) % board_x
    final_y = (y + vy_after_sec) % board_y
    
    return final_x, final_y

with open("data.txt") as f:
    q1 = q2 = q3 = q4 = 0
    for line in f:
        p, v = line.split(" ")
        
        x,y = p.split("=")[1].split(",")
        vx,vy = v.split("=")[1].split(",")
        
        x, y, vx, vy = int(x), int(y), int(vx), int(vy)
        
        final_pos = robot_movement_after_seconds(x, y, vx, vy, 100)
        
        left = final_pos[0] in range((board_x - 1) // 2)
        right = final_pos[0] in range((board_x - 1) // 2 + 1, board_x)
        
        top = final_pos[1] in range((board_y - 1) // 2)
        bottom = final_pos[1] in range((board_y - 1) // 2 + 1, board_y)        
        
        if top:
            if left:
                q1 += 1
            elif right:
                q2 += 1
        elif bottom:
            if left:
                q3 += 1
            elif right:
                q4 += 1

    print(q1, q2, q3, q4)
    print(q1 * q2 * q3 * q4)
                