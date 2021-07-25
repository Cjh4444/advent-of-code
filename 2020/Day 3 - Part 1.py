
def count_trees(input):
    input = [list(line.strip()) for line in input]
    y = 0
    length = len(input[0])
    tree_count = 0

    for row in input:
        if row[y % length] == "#":
            tree_count += 1
        y += 3
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


assert(count_trees(testinput) == 7)

with open("inputs/Day3Input.txt") as f:
    print(count_trees(f))

    
