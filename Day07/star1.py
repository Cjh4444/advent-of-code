from collections import deque


def in_board(board, pos):
    return pos[0] in range(0, len(board)) and pos[1] in range(0, len(board[pos[0]]))


def traverse(board: list[list[str]]):
    stack: deque[tuple[int, int]] = deque()

    stack.append((1, board[0].index("S")))

    count = 0
    while stack:
        pos = stack.pop()
        space = board[pos[0]][pos[1]]

        if space == "|":
            continue
        elif space == ".":
            board[pos[0]][pos[1]] = "|"
            new_pos = (pos[0] + 1, pos[1])
            if in_board(board, new_pos):
                stack.append(new_pos)
        elif space == "^":
            count += 1
            new_positions = [(pos[0], pos[1] - 1), (pos[0], pos[1] + 1)]
            for new_pos in new_positions:
                if in_board(board, new_pos):
                    stack.append(new_pos)
    return count


def print_board(board):
    for line in board:
        for char in line:
            print(char, end="")
        print()


def process(file):
    with open(file) as f:
        board = [list(line.strip()) for line in f]
        count = traverse(board)
        print(count)
        return count


assert process("test.txt") == 21
process("data.txt")
