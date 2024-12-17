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

# robots = []
final_set = set()
with open("data.txt") as f:
    for line in f:
        p, v = line.split(" ")
        
        x,y = p.split("=")[1].split(",")
        vx,vy = v.split("=")[1].split(",")
        
        x, y, vx, vy = int(x), int(y), int(vx), int(vy)
        
        final_pos = robot_movement_after_seconds_eff(x,y,vx,vy,8168)
        final_set.add(final_pos)
        
        # robots.append([x,y,vx,vy])

    # safety_list = []
    # for step in range(10403):
    #     q1 = q2 = q3 = q4 = 0
    #     for robot in robots:
            
    #         left = robot[0] in range((board_x - 1) // 2)
    #         right = robot[0] in range((board_x - 1) // 2 + 1, board_x)
            
    #         top = robot[1] in range((board_y - 1) // 2)
    #         bottom = robot[1] in range((board_y - 1) // 2 + 1, board_y)        
            
    #         if top:
    #             if left:
    #                 q1 += 1
    #             elif right:
    #                 q2 += 1
    #         elif bottom:
    #             if left:
    #                 q3 += 1
    #             elif right:
    #                 q4 += 1
    #     print(f"did step {step}")
    #     safety_list.append((step, q1 * q2 * q3* q4))
    #     for idx in range(len(robots)):
    #         robots[idx][0], robots[idx][1] = move_robot(robots[idx][0], robots[idx][1], robots[idx][2], robots[idx][3])
    
    # print(sorted(safety_list, key=lambda x: x[1])[::-1])



board = [["."] * board_x for _ in range(board_y)]
    
print(board)

for i in range(board_y):
    for j in range(board_x):
        if (j, i) in final_set:
            board[i][j] = "X"

print(board)
            
with open('result.txt', 'w') as f:
    for line in board:
        f.write("".join(line) + "\n")


            

        
                