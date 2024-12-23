from itertools import product
from collections import Counter
import time
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

directions = {
    "^": (-1,0),
    "v": (1,0),
    "<": (0,-1),
    ">": (0,1)
}

def find_min_length_path(string, max_depth, using_num_pad):
    if (max_depth == 0):
        return len(string)
    
    start_char = "A"
    instructions = []
    for char in string:
        find_min_length

found_path = False

@cache
def find_paths_help(start_char, goal_char, using_num_pad: bool):
    global found_path
    found_path = False
    dictionary = num_pad_coords if using_num_pad else directional_pad_coords
    
    start_char_coord = dictionary[start_char]
    y_diff, x_diff = start_char_coord[0] - dictionary[goal_char][0], start_char_coord[1] - dictionary[goal_char][1]
    
    up = y_diff >= 0
    left = x_diff >= 0
    
    vert_char = "^" if up else "v"
    hoz_char = "<" if left else ">"
    
    path_set = set()
    
    p1 = vert_char * abs(y_diff) + hoz_char * abs(x_diff)
    if test_path(start_char_coord, p1, dictionary):
        path_set.add(p1 + "A")
    
    p2 = hoz_char * abs(x_diff) + vert_char * abs(y_diff)
    if test_path(start_char_coord, p2, dictionary):
        path_set.add(p2 + "A")
    
    if path_set:
        return path_set
    else:
        raise Exception(start_char, goal_char, using_num_pad, p1, p2)
    
    # find_paths_help(start_char_coord, abs(y_diff), up, abs(x_diff), left, path_set, dictionary)
    
    # print(path_set)
    # return path_set

def test_path(start_coord, path, dictionary):
    coord = start_coord
    for move in path:
        d = directions[move]
        coord = (coord[0] + d[0], coord[1] + d[1])
        if coord == dictionary[" "]:
            return False
    return True

with open("data.txt") as f:
    total = 0
    
    start_time = time.time()
    
    string_cache: dict[tuple[str, str], set[str]] = {}
    print("start building cache")
    # precalculate all paths
    for start_button in num_pad_coords:
        if start_button == " ":
            continue
        for end_button in num_pad_coords:
            if end_button == " ":
                continue
            string_cache[(start_button, end_button)] = find_paths(start_button, end_button, True)
    
    for start_button in directional_pad_coords:
        if start_button == " ":
            continue
        for end_button in directional_pad_coords:
            if end_button == " ":
                continue
            cache[(start_button, end_button)] = find_paths(start_button, end_button, False)
    
    print("end building cache")
    
    for code in f:
        code = code.strip()        
        sets = [cache[("A", code[0])]]
        for start, goal in zip(code, code[1:]):
            sets.append(cache[(start, goal)])
        all_strings = [''.join(parts) for parts in product(*sets)]            
        for i in range(2):
            bing = []
            shortest = 10000000000000000
            # print(len(all_strings))
            for dir_string in all_strings:
                sets = [cache[(start, goal)] for start, goal in zip(dir_string, dir_string[1:])]
                sets.append(cache[("A", dir_string[0])])
                temp_all_strings = [''.join(parts) for parts in product(*sets)]
                length = len(temp_all_strings[0])
                # print(length)
                if length < shortest:
                    # print("RESET LIST")
                    bing = []
                    shortest = len(temp_all_strings[0])
                elif length == shortest:
                    pass
                else:
                    continue
                bing.extend(temp_all_strings)
            all_strings = bing
            print("next loop")
            print(Counter(len(s) for s in all_strings))
            
        length = len(all_strings[0])
        complexity = length * int(code[:3])
        # print(length, int(code[:3]))
        total += complexity
        print("completed string")
    print(total)
    print(time.time() - start_time)