def print_board(board):
    for row in board:
        print("".join(row))
        
def map_plot(board, coords, coords_set):
    coords_set.add(coords)
    if coords[0] - 1 >= 0 and board[coords[0] - 1][coords[1]] == board[coords[0]][coords[1]] and (coords[0] - 1, coords[1]) not in coords_set:
        coords_set.add((coords[0] - 1, coords[1]))
        map_plot(board, (coords[0] - 1, coords[1]), coords_set)
    
    if coords[0] + 1 < len(board) and board[coords[0] + 1][coords[1]] == board[coords[0]][coords[1]] and (coords[0] + 1, coords[1]) not in coords_set:
        coords_set.add((coords[0] + 1, coords[1]))
        map_plot(board, (coords[0] + 1, coords[1]), coords_set)
    
    if coords[1] - 1 >= 0 and board[coords[0]][coords[1] - 1] == board[coords[0]][coords[1]] and (coords[0], coords[1] - 1) not in coords_set:
        coords_set.add((coords[0], coords[1] - 1))
        map_plot(board, (coords[0], coords[1] - 1), coords_set)
    
    if coords[1] + 1 < len(board[0]) and board[coords[0]][coords[1] + 1] == board[coords[0]][coords[1]] and (coords[0], coords[1] + 1) not in coords_set:
        coords_set.add((coords[0], coords[1] + 1))
        map_plot(board, (coords[0], coords[1] + 1), coords_set)
    
    return coords_set
    
        
def find_region_coords(board: list[list], region: str, region_coords: dict[str, list]):
    for r_idx , row in enumerate(board):
        for c_idx, space in enumerate(row):
            if space == region:
                region_coords.setdefault(region, []).append((r_idx, c_idx))

def find_num_sides(board, coord_set):    
    start_coord = coord_set.pop()
    
    while True:
        above = coord[0] - 1 < 0 or (coord[0] - 1, coord[1]) not in coord_set
        below = coord[0] + 1 >= len(board) or (coord[0] + 1, coord[1]) not in coord_set
        left = coord[1] - 1 < 0 or (coord[0], coord[1] - 1) not in coord_set
        right = coord[1] + 1 >= len(board[0]) or (coord[0], coord[1] + 1) not in coord_set
    
        if above + below + left + right == 0:
            start_coord = (start_coord[0] + 1, start_coord[0])
        else:
            break
        
    while above + below + left + right == 0:
        start_coord = (start_coord[0] + 1, start_coord[0])
    
    """
    0 - up
    1 - right
    2 - down
    3 - left
    """
    direction = -1
    if left:
        direction = 0
    elif above:
        direction = 1
    elif right:
        direction = 2
    elif below:
        direction = 3
    
    start_direction = direction
    current
    
    while: #ISSUE WITH THE INNER FENCES, TALK TO DAD
    
    
        
    
    
    
    region = board[coord[0]][coord[1]]
    above = coord[0] - 1 < 0 or board[coord[0] - 1][coord[1]] != region
    below = coord[0] + 1 >= len(board) or board[coord[0] + 1][coord[1]] != region
    left = coord[1] - 1 < 0 or board[coord[0]][coord[1] - 1] != region
    right = coord[1] + 1 >= len(board[0]) or board[coord[0]][coord[1] + 1] != region
    total += above + below + left + right
    
    return total


board: list[list] = []
all_coords: set[tuple] = set()

with open("data.txt") as f:
    for line in f:
        temp = list(line.strip())
        board.append(temp)

for i in range(len(board)):
    for j in range(len(board[0])):
        all_coords.add((i, j))
        
total = 0
while len(all_coords) > 0:
    coord = all_coords.pop()
    set_of_coords = map_plot(board, coord, set())
    
    perimeter = find_perimeter(board, set_of_coords)
    
    area = len(set_of_coords)
    total += area * perimeter
    
    # print(f"{coord=}")
    # print(f"crop: {board[coord[0]][coord[1]]}")
    # print(f"{area=}")
    # print(f"{perimeter=}")
    # print(f"{area*perimeter=}")
    
    
    all_coords.difference_update(set_of_coords)

print(total)
    
