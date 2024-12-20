board: list[list] = []
all_coords: set[tuple] = set()

def print_board():
    for row in board:
        print("".join(row))
        
directions = [(1,0), (-1,0), (0,1), (0,-1)]
def map_plot(coord, coords_set):
    coords_set.add(coord)
    
    for d in directions:
        ny, nx = coord[0] + d[0], coord[1] + d[1]
        if (ny in range(len(board)) and nx in range(len(board[0])) and
            board[coord[0]][coord[1]] == board[ny][nx] and (ny,nx) not in coords_set):
            coords_set.add((ny, nx))
            map_plot((ny,nx), coords_set)
    
    return coords_set

def has_edge_in_direction(coord, d, area_set):
    ny, nx = coord[0] + d[0], coord[1] + d[1]
    return not (ny in range(len(board)) and nx in range(len(board[0]))) or (ny,nx) not in area_set

def not_in_board(y,x):
    return not(y in range(len(board)) and x in range(len(board[0])))

# def has_edge_in_direction(coord, d, area_set):
#     ny, nx = coord[0] + d[0], coord[1] + d[1]    
#     return not (ny in range(len(board)) or nx in range(len(board[0]))) or (ny,nx) not in area_set

def find_perimeter(area_set):
    total = 0
    border_set = set()
    
    for coord in area_set:
        for d in directions:
            if has_edge_in_direction(coord, d, area_set):
                total += 1
                border_set.add(coord)  
    return total, border_set

"""
if checking left/right, go down
if checking up/down, go right
"""

def count_sides(border_set: set, area_set: set):
    temp = border_set.copy()
    side_count = 0
    
    while temp:
        coord = temp.pop()
        # print(coord)
        for d in directions:
            if has_edge_in_direction(coord, d, area_set):
                # print(f"    has an edge in {d}")
                if d[1] == 0:
                    if not has_edge_in_direction((coord[0], coord[1] + 1), d, area_set) or (coord[0],coord[1] + 1) not in area_set:
                        # print(f"        the coord {(coord[0], coord[1] + 1)} to the right doesn't have an edge to the {d} plus 1 side")
                        side_count += 1
                    # else:
                    #     print(f"        the coord {(coord[0], coord[1] + 1)} to the right does have an edge to the {d}")
                else:
                    if not has_edge_in_direction((coord[0] + 1, coord[1]), d, area_set) or (coord[0] + 1, coord[1]) not in area_set:
                        # print(f"        the coord {(coord[0] + 1, coord[1])} to the down doesn't have an edge to the {d}, plus 1 side")
                        side_count += 1
                    # else:
                    #     print(f"        the coord {(coord[0] + 1, coord[1])} to the down does have an edge to the {d}")
                    
    
    return side_count
        

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
    set_of_coords = map_plot(coord, set())
    
    perimeter, border_set = find_perimeter(set_of_coords)
    
    sides = count_sides(border_set, set_of_coords)
    print(f"{board[coord[0]][coord[1]]} {sides}")
    
    area = len(set_of_coords)
    total += area * sides
    
    # print(f"{coord=}")
    # print(f"crop: {board[coord[0]][coord[1]]}")
    # print(f"{area=}")
    # print(f"{perimeter=}")
    # print(f"{area*perimeter=}")
    
    
    all_coords.difference_update(set_of_coords)

print(total)
    
