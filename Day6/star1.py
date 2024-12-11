board = []
guard_row = -1
guard_col = -1
num_spaces = 0


def check_up():
    global guard_row, num_spaces
    if guard_row == 0:
        return True

    next_space = board[guard_row - 1][guard_col]

    if next_space == "." or next_space == "X":
        if next_space == ".":
            num_spaces += 1
        board[guard_row - 1][guard_col] = "^"
        board[guard_row][guard_col] = "X"
        guard_row -= 1
    elif next_space == "#":
        board[guard_row][guard_col] = ">"


def check_right():
    global guard_col, num_spaces
    if guard_col == len(board[0]) - 1:
        return True

    next_space = board[guard_row][guard_col + 1]

    if next_space == "." or next_space == "X":
        if next_space == ".":
            num_spaces += 1
        board[guard_row][guard_col + 1] = ">"
        board[guard_row][guard_col] = "X"
        guard_col += 1
    elif next_space == "#":
        board[guard_row][guard_col] = "v"


def check_down():
    global guard_row, num_spaces
    if guard_row == len(board) - 1:
        return True

    next_space = board[guard_row + 1][guard_col]

    if next_space == "." or next_space == "X":
        if next_space == ".":
            num_spaces += 1
        board[guard_row + 1][guard_col] = "v"
        board[guard_row][guard_col] = "X"
        guard_row += 1
    elif next_space == "#":
        board[guard_row][guard_col] = "<"


def check_left():
    global guard_col, num_spaces
    if guard_col == 0:
        return True

    next_space = board[guard_row][guard_col - 1]

    if next_space == "." or next_space == "X":
        if next_space == ".":
            num_spaces += 1
        board[guard_row][guard_col - 1] = "<"
        board[guard_row][guard_col] = "X"
        guard_col -= 1
    elif next_space == "#":
        board[guard_row][guard_col] = "^"


with open("data.txt") as f:
    for row, line in enumerate(f):
        board_line = list(line.strip())
        if guard_col == -1:
            for col, space in enumerate(board_line):
                if space == "^":
                    guard_row = row
                    guard_col = col
        board.append(board_line)

done = False

while not done:
    guard_character = board[guard_row][guard_col]

    if guard_character == "^":
        done = check_up()
    elif guard_character == ">":
        done = check_right()
    elif guard_character == "v":
        done = check_down()
    elif guard_character == "<":
        done = check_left()

print(num_spaces + 1)
