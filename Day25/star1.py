locks = []
keys = []

def convert_schematic_to_height(schematic, key: bool):
    heights = [-1] * 5
    
    for level in schematic:
        for idx, x in enumerate(level):
            if x == "#":
                heights[idx] += 1
    
    return tuple(heights)

def key_works(lock, key):
    for l, k in zip(lock, key):
        if (5 - l - k) < 0:
            return False
    return True

with open("data.txt") as f:
    while True:
        schematic = [f.readline().strip() for i in range(7)]
        print(schematic)
        
        if schematic[0][0] == "#":
            locks.append(convert_schematic_to_height(schematic, True))
        else:
            keys.append(convert_schematic_to_height(schematic, False))
        
        if not f.readline():
            break
    
    total = 0
    for lock in locks:
        for key in keys:
            if key_works(lock, key):
                total += 1
    
    print(total)