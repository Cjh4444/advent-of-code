import all_spots

board = []
guard_row = -1
guard_col = -1


def check_up(board):
    global guard_row
    if guard_row == 0:
        return True

    next_space = board[guard_row - 1][guard_col]

    if next_space == ".":
        board[guard_row - 1][guard_col] = "^"
        board[guard_row][guard_col] = "."
        guard_row -= 1
    elif next_space == "#":
        board[guard_row][guard_col] = ">"


def check_right(board):
    global guard_col
    if guard_col == len(board[0]) - 1:
        return True

    next_space = board[guard_row][guard_col + 1]

    if next_space == ".":
        board[guard_row][guard_col + 1] = ">"
        board[guard_row][guard_col] = "."
        guard_col += 1
    elif next_space == "#":
        board[guard_row][guard_col] = "v"


def check_down(board):
    global guard_row
    if guard_row == len(board) - 1:
        return True

    next_space = board[guard_row + 1][guard_col]

    if next_space == ".":
        board[guard_row + 1][guard_col] = "v"
        board[guard_row][guard_col] = "."
        guard_row += 1
    elif next_space == "#":
        board[guard_row][guard_col] = "<"


def check_left(board):
    global guard_col
    if guard_col == 0:
        return True

    next_space = board[guard_row][guard_col - 1]

    if next_space == ".":
        board[guard_row][guard_col - 1] = "<"
        board[guard_row][guard_col] = "."
        guard_col -= 1
    elif next_space == "#":
        board[guard_row][guard_col] = "^"


def print_board():
    for i in board:
        print("".join(i))
    print()


with open("data.txt") as f:
    for row, line in enumerate(f):
        board_line = list(line.strip())
        if guard_col == -1:
            for col, space in enumerate(board_line):
                if space == "^":
                    guard_row = row
                    guard_col = col
        board.append(board_line)

original_row = guard_row
original_col = guard_col

num_loops = 0
for i in range(len(board)):
    for j in range(len(board[0])):
        print(f"doing ({i},{j})")

        if (
            board[i][j] == "#"
            or board[i][j] == "^"
            or (i, j) not in all_spots.all_spots
        ):
            continue

        board[i][j] = "#"

        done = False

        num_moves = 0
        while not done:
            guard_character = board[guard_row][guard_col]

            if guard_character == "^":
                done = check_up(board)
            elif guard_character == ">":
                done = check_right(board)
            elif guard_character == "v":
                done = check_down(board)
            elif guard_character == "<":
                done = check_left(board)
            num_moves += 1
            if num_moves > 100000:
                num_loops += 1
                print(f"    ({i},{j}) is probably a loop")
                num_moves = 0
                break

        board[i][j] = "."
        board[guard_row][guard_col] = "."

        guard_row = original_row
        guard_col = original_col
        board[guard_row][guard_col] = "^"

print(num_loops)
