
def count_trees(input,right,down):
    y = 0
    length = len(input[1])
    tree_count = 0

    for i in range(0,len(input),down):
        if input[i][y % length] == "#":
            tree_count += 1
        y += right
    return tree_count


testinput = ["..##.......",
"#...#...#..",
".#....#..#.",
"..#.#...#.#",
".#...##..#.",
"..#.##.....",
".#.#.#....#",
".#........#",
"#.##...#...",
"#...##....#",
".#..#...#.#"]

assert(count_trees(testinput,3,1) == 7)

with open("inputs/Day3Input.txt") as f:
    value = [list(line.strip()) for line in f]
    r1d1 = count_trees(value,1,1)
    r3d1 = count_trees(value,3,1)
    r5d1 = count_trees(value,5,1)
    r7d1 = count_trees(value,7,1)
    r1d2 = count_trees(value,1,2)
    result = r1d1*r3d1*r5d1*r7d1*r1d2
    print(result)
    
