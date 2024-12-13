def find_zeros(board):
    zeros = set()
    for r_idx, row in enumerate(board):
        for c_idx, space in enumerate(row):
            if space == "0":
                zeros.add((r_idx, c_idx))

    return zeros


def score_from_start(coords, board, already_found: set):
    # print(f"{coords=}")
    possible_paths = []

    if board[coords[0]][coords[1]] == "9" and coords not in already_found:
        already_found.add(coords)
        return 1

    if coords[0] + 1 < len(board):
        if board[coords[0] + 1][coords[1]] == str(
            int(board[coords[0]][coords[1]]) + 1
        ):
            possible_paths.append((coords[0] + 1, coords[1]))

    if coords[0] - 1 >= 0:
        if board[coords[0] - 1][coords[1]] == str(
            int(board[coords[0]][coords[1]]) + 1
        ):
            possible_paths.append((coords[0] - 1, coords[1]))

    if coords[1] + 1 < len(board[0]):
        if board[coords[0]][coords[1] + 1] == str(
            int(board[coords[0]][coords[1]]) + 1
        ):
            possible_paths.append((coords[0], coords[1] + 1))

    if coords[1] - 1 >= 0:
        if board[coords[0]][coords[1] - 1] == str(
            int(board[coords[0]][coords[1]]) + 1
        ):
            possible_paths.append((coords[0], coords[1] - 1))

    # print(possible_paths)
    if len(possible_paths) == 0:
        return 0

    total = 0

    for path in possible_paths:
        total += score_from_start(path, board, already_found)

    return total


board = []

with open("data.txt") as f:
    for line in f:
        board.append(list(line.strip()))

    zeros = find_zeros(board)

    total = 0
    for coord in zeros:
        total += score_from_start(coord, board, set())

    print(total)
