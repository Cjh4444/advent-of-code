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

def find_paths(start_char, goal_char, using_num_pad: bool):
    dictionary = num_pad_coords if using_num_pad else directional_pad_coords
    
    start_char_coord = dictionary[start_char]
    y_diff, x_diff = start_char_coord[0] - dictionary[goal_char][0], start_char_coord[1] - dictionary[goal_char][1]
    
    up = y_diff >= 0
    left = x_diff >= 0
    
    path_set = set()
    
    find_paths_help(start_char_coord, abs(y_diff), up, abs(x_diff), left, path_set, dictionary)
    
    return path_set

def find_paths_help(coord, y_diff, up: bool, x_diff, left, path_set, dictionary, string = ""):
    if coord == dictionary[" "]:
        return
    
    if not (y_diff or x_diff):
        path_set.add(string + "A")
        return

    if y_diff:
        vert_char, d = ("^", -1) if up else ("v", 1)
        find_paths_help((coord[0] + d, coord[1]), y_diff - 1, up, x_diff, left, path_set, dictionary, string + vert_char)
    
    if x_diff:
        hoz_char, d = ("<", -1) if left else (">", 1)
        find_paths_help((coord[0], coord[1] + d), y_diff, up, x_diff - 1, left, path_set, dictionary, string + hoz_char)

with open("data.txt") as f:
    total = 0
    for code in f:
        code = code.strip()
        all_strings = find_paths("A", code[0], True)

        for start, goal in zip(code, code[1:]):
            temp = []
            for string in all_strings:
                for additional in find_paths(start, goal, True):
                    temp.append(string + additional)
            all_strings = temp
        print(len(all_strings))
        
        for i in range(2):
            bing = []
            for dir_string in all_strings:
                temp_all_strings = find_paths("A", dir_string[0], False)
                for start, goal in zip(dir_string, dir_string[1:]):
                    temp = []
                    for string in temp_all_strings:
                        for additional in find_paths(start, goal, False):
                            temp.append(string + additional)
                    temp_all_strings = temp
                bing.extend(temp_all_strings)
            all_strings = bing
            print(len(all_strings))

        
        total += len(min(all_strings, key=len)) * int(code[:3])
        print("completed string")
    print(total)





        