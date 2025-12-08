def in_board(board, pos):
    return pos[0] in range(0, len(board)) and pos[1] in range(0, len(board[pos[0]]))


def traverse(board: list[list[str]]):
    return traverse_from_point(board, (1, board[0].index("S")))


def traverse_from_point(board, start, cache={}) -> int:
    if start in cache:
        return cache[start]

    if not in_board(board, start):
        if start[0] == len(board):
            return 1
        return 0

    space = board[start[0]][start[1]]

    if space == ".":
        cache[start] = traverse_from_point(board, (start[0] + 1, start[1]))
    elif space == "^":
        cache[start] = traverse_from_point(
            board, (start[0], start[1] - 1)
        ) + traverse_from_point(board, (start[0], start[1] + 1))

    return cache[start]


def process(file):
    with open(file) as f:
        board = [list(line.strip()) for line in f]
        count = traverse(board)
        print(count)
        return count


assert process("test.txt") == 40
process("data.txt")
