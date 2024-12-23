from itertools import product
from functools import cache

num_pad_coords = {
    "9": (0,2),
    "8": (0,1),
    "7": (0,0),
    "6": (1,2),
    "5": (1,1),
    "4": (1,0),
    "3": (2,2),
    "2": (2,1),
    "1": (2,0),
    "A": (3,2),
    "0": (3,1),
    " ": (3,0)
}

directional_pad_coords = {
    "A": (0,2),
    "^": (0,1),
    " ": (0,0),
    ">": (1,2),
    "v": (1,1),
    "<": (1,0)
}


def build_paths():
    def build_path(start_char, goal_char, dictionary):
        start_char_coord = dictionary[start_char]
        y_diff, x_diff = start_char_coord[0] - dictionary[goal_char][0], start_char_coord[1] - dictionary[goal_char][1]
        
        up = y_diff >= 0
        left = x_diff >= 0
        
        vert_char = "^" if up else "v"
        hoz_char = "<" if left else ">"
        
        path_set = []
        
        p1 = vert_char * abs(y_diff) + hoz_char * abs(x_diff)
        if test_path(start_char_coord, p1, dictionary):
            path_set.append(p1 + "A")
        
        p2 = hoz_char * abs(x_diff) + vert_char * abs(y_diff)
        if test_path(start_char_coord, p2, dictionary):
            path_set.append(p2 + "A")
        
        if path_set:
            return path_set
        else:
            raise Exception(start_char, goal_char, p1, p2)
    
    def test_path(start_coord, path, dictionary):
        directions = {
            "^": (-1,0),
            "v": (1,0),
            "<": (0,-1),
            ">": (0,1)
        }
        coord = start_coord
        for move in path:
            d = directions[move]
            coord = (coord[0] + d[0], coord[1] + d[1])
            if coord == dictionary[" "]:
                return False
        return True

    buttons_to_path = {}
    
    for x in [num_pad_coords, directional_pad_coords]:
        for start_button in x:
            if start_button == " ":
                continue
            for end_button in x:
                if end_button == " ":
                    continue
                buttons_to_path[(start_button, end_button)] = build_path(start_button, end_button, x)
    return buttons_to_path
    
paths = build_paths()
path_lengths = {k: len(v[0]) for k,v in paths.items()}

@cache
def find_min_length(path, depth):
    if (depth == 1):
        return sum([path_lengths[(start, end)] for start, end in zip("A" + path, path)])

    length = 0
    for start, end in zip("A" + path, path):
        length += min([find_min_length(path, depth - 1) for path in paths[(start,end)]])
    
    return length

with open("data.txt") as f:
    total = 0
    
    for code in f:
        code = code.strip()        
        possibilities = [paths[(start, goal)] for start, goal in zip("A" + code, code)]
        all_strings = ["".join(parts) for parts in product(*possibilities)]            
        
        total += min([find_min_length(string, 25) for string in all_strings]) * int(code[:3])
    print(total)
