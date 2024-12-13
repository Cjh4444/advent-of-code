def find_antinode_locations(node1: tuple[int, int], node2: tuple[int, int]):
    hoz_diff = abs(node2[1] - node1[1])
    vert_diff = abs(node2[0] - node1[0])
    same_hoz = hoz_diff == 0
    same_vert = vert_diff == 0

    antinode1, antinode2 = (), ()

    if same_hoz and same_vert:
        pass
    elif same_hoz:
        # print("same hoz")
        if node1[0] > node2[0]:
            node1, node2 = node2, node1
        antinode1 = (node1[0] - vert_diff, node1[1])
        antinode2 = (node2[0] + vert_diff, node2[1])
    elif same_vert:
        # print("same vert")
        if node1[1] > node2[1]:
            node1, node2 = node2, node1
        antinode1 = (node1[0], node1[1] - hoz_diff)
        antinode2 = (node2[0], node2[1] + hoz_diff)
    else:
        if node2[1] > node1[1]:
            if node2[0] > node1[0]:
                # print("1")
                antinode1 = (node1[0] - vert_diff, node1[1] - hoz_diff)
                antinode2 = (node2[0] + vert_diff, node2[1] + hoz_diff)
            else:
                # print("2")
                antinode1 = (node1[0] + vert_diff, node1[1] - hoz_diff)
                antinode2 = (node2[0] - vert_diff, node2[1] + hoz_diff)
        else:
            if node2[0] > node1[0]:
                # print("3")
                antinode1 = (node1[0] - vert_diff, node1[1] + hoz_diff)
                antinode2 = (node2[0] + vert_diff, node2[1] - hoz_diff)
            else:
                # print("4")
                antinode1 = (node1[0] + vert_diff, node1[1] + hoz_diff)
                antinode2 = (node2[0] - vert_diff, node2[1] - hoz_diff)

    # print(antinode1, antinode2)
    return antinode1, antinode2


assert set(find_antinode_locations((0, 2), (0, 3))) == {(0, 1), (0, 4)}
assert set(find_antinode_locations((0, 3), (0, 2))) == {(0, 1), (0, 4)}
assert set(find_antinode_locations((2, 1), (4, 1))) == {(0, 1), (6, 1)}
assert set(find_antinode_locations((4, 1), (2, 1))) == {(0, 1), (6, 1)}
assert set(find_antinode_locations((3, 3), (4, 4))) == {(2, 2), (5, 5)}
assert set(find_antinode_locations((4, 4), (3, 3))) == {(2, 2), (5, 5)}
assert set(find_antinode_locations((3, 3), (4, 2))) == {(2, 4), (5, 1)}
assert set(find_antinode_locations((4, 2), (3, 3))) == {(2, 4), (5, 1)}

board = []
antinodes = set()
nodes: dict[str, list] = dict()

with open("data.txt") as f:
    for line in f:
        board.append(line.strip())

    for i, row in enumerate(board):
        for j, char in enumerate(row):
            if char != ".":
                nodes.setdefault(char, []).append((i, j))

for node in nodes:
    for location in nodes[node]:
        for other_loc in nodes[node]:
            antinode1, antinode2 = find_antinode_locations(location, other_loc)

            if antinode1 == ():
                continue

            if (
                antinode1[0] >= 0
                and antinode1[0] < len(board)
                and antinode1[1] >= 0
                and antinode1[1] < len(board[0])
            ):
                antinodes.add(antinode1)

            if (
                antinode2[0] >= 0
                and antinode2[0] < len(board)
                and antinode2[1] >= 0
                and antinode2[1] < len(board[0])
            ):
                antinodes.add(antinode2)

print(antinodes)
print(len(antinodes))
