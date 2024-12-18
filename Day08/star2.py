def node_in_bounds(node, board):
    return (
        node[0] >= 0
        and node[0] < len(board)
        and node[1] >= 0
        and node[1] < len(board[0])
    )


def find_antinode_locations(
    node1: tuple[int, int], node2: tuple[int, int], board
):
    hoz_diff = abs(node2[1] - node1[1])
    vert_diff = abs(node2[0] - node1[0])
    same_hoz = hoz_diff == 0
    same_vert = vert_diff == 0

    antinodes = set()
    antinodes.update({node1, node2})

    if same_hoz and same_vert:
        pass
    elif same_hoz:
        # print("same hoz")
        if node1[0] > node2[0]:
            node1, node2 = node2, node1
        antinode1 = (node1[0] - vert_diff, node1[1])
        antinode2 = (node2[0] + vert_diff, node2[1])

        counter = 2
        while node_in_bounds(antinode1, board):
            antinodes.add(antinode1)
            antinode1 = (node1[0] - vert_diff * counter, node1[1])
            counter += 1

        counter = 2
        while node_in_bounds(antinode2, board):
            antinodes.add(antinode2)
            antinode2 = (node1[0] + vert_diff * counter, node1[1])
            counter += 1

    elif same_vert:
        # print("same vert")
        if node1[1] > node2[1]:
            node1, node2 = node2, node1
        antinode1 = (node1[0], node1[1] - hoz_diff)
        antinode2 = (node2[0], node2[1] + hoz_diff)

        counter = 2
        while node_in_bounds(antinode1, board):
            antinodes.add(antinode1)
            antinode1 = (node1[0], node1[1] - hoz_diff * counter)
            counter += 1

        counter = 2
        while node_in_bounds(antinode2, board):
            antinodes.add(antinode2)
            antinode2 = (node2[0], node2[1] + hoz_diff * counter)
            counter += 1
    else:
        if node2[1] > node1[1]:
            if node2[0] > node1[0]:
                # print("1")
                antinode1 = (node1[0] - vert_diff, node1[1] - hoz_diff)
                antinode2 = (node2[0] + vert_diff, node2[1] + hoz_diff)

                counter = 2
                while node_in_bounds(antinode1, board):
                    antinodes.add(antinode1)
                    antinode1 = (
                        node1[0] - vert_diff * counter,
                        node1[1] - hoz_diff * counter,
                    )
                    counter += 1

                counter = 2
                while node_in_bounds(antinode2, board):
                    antinodes.add(antinode2)
                    antinode2 = (
                        node1[0] + vert_diff * counter,
                        node1[1] + hoz_diff * counter,
                    )
                    counter += 1
            else:
                # print("2")
                antinode1 = (node1[0] + vert_diff, node1[1] - hoz_diff)
                antinode2 = (node2[0] - vert_diff, node2[1] + hoz_diff)

                counter = 2
                while node_in_bounds(antinode1, board):
                    print(f"added {antinode1}")
                    antinodes.add(antinode1)
                    antinode1 = (
                        node1[0] + vert_diff * counter,
                        node1[1] - hoz_diff * counter,
                    )
                    counter += 1

                counter = 2
                while node_in_bounds(antinode2, board):
                    print(f"added {antinode2}")
                    antinodes.add(antinode2)
                    antinode2 = (
                        node1[0] - vert_diff * counter,
                        node1[1] + hoz_diff * counter,
                    )
                    counter += 1
        else:
            if node2[0] > node1[0]:
                # print("3")
                antinode1 = (node1[0] - vert_diff, node1[1] + hoz_diff)
                antinode2 = (node2[0] + vert_diff, node2[1] - hoz_diff)

                counter = 2
                while node_in_bounds(antinode1, board):
                    print(f"added {antinode1}")
                    antinodes.add(antinode1)
                    antinode1 = (
                        node1[0] - vert_diff * counter,
                        node1[1] + hoz_diff * counter,
                    )
                    counter += 1

                counter = 2
                while node_in_bounds(antinode2, board):
                    print(f"added {antinode2}")
                    antinodes.add(antinode2)
                    antinode2 = (
                        node1[0] + vert_diff * counter,
                        node1[1] - hoz_diff * counter,
                    )
                    counter += 1
            else:
                # print("4")
                antinode1 = (node1[0] + vert_diff, node1[1] + hoz_diff)
                antinode2 = (node2[0] - vert_diff, node2[1] - hoz_diff)

                counter = 2
                while node_in_bounds(antinode1, board):
                    antinodes.add(antinode1)
                    antinode1 = (
                        node1[0] + vert_diff * counter,
                        node1[1] + hoz_diff * counter,
                    )
                    counter += 1

                counter = 2
                while node_in_bounds(antinode2, board):
                    antinodes.add(antinode2)
                    antinode2 = (
                        node1[0] - vert_diff * counter,
                        node1[1] - hoz_diff * counter,
                    )
                    counter += 1

    # print(antinode1, antinode2)
    return antinodes


# assert set(find_antinode_locations((0, 2), (0, 3))) == {(0, 1), (0, 4)}
# assert set(find_antinode_locations((0, 3), (0, 2))) == {(0, 1), (0, 4)}
# assert set(find_antinode_locations((2, 1), (4, 1))) == {(0, 1), (6, 1)}
# assert set(find_antinode_locations((4, 1), (2, 1))) == {(0, 1), (6, 1)}
# assert set(find_antinode_locations((3, 3), (4, 4))) == {(2, 2), (5, 5)}
# assert set(find_antinode_locations((4, 4), (3, 3))) == {(2, 2), (5, 5)}
# assert set(find_antinode_locations((3, 3), (4, 2))) == {(2, 4), (5, 1)}
# assert set(find_antinode_locations((4, 2), (3, 3))) == {(2, 4), (5, 1)}

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
            antinodes.update(
                find_antinode_locations(location, other_loc, board)
            )

print(antinodes)
print(len(antinodes))
