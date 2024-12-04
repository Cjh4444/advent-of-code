import re

board = []


def horizontal_xmas(board):
    temp = []
    for line in board:
        temp.extend(re.findall("XMAS", line))
        temp.extend(re.findall("SAMX", line))
    return len(temp)


def vertical_xmas(board):
    count = 0
    for l1, l2, l3, l4 in zip(board, board[1:], board[2:], board[3:]):
        for c1, c2, c3, c4 in zip(l1, l2, l3, l4):
            if (c1 == "X" and c2 == "M" and c3 == "A" and c4 == "S") or (
                c1 == "S" and c2 == "A" and c3 == "M" and c4 == "X"
            ):
                count += 1
    return count


def diagonal_xmas(board):
    count = 0
    for l1, l2, l3, l4 in zip(board, board[1:], board[2:], board[3:]):
        for c1, c2, c3, c4 in zip(l1, l2[1:], l3[2:], l4[3:]):
            if (c1 == "X" and c2 == "M" and c3 == "A" and c4 == "S") or (
                c1 == "S" and c2 == "A" and c3 == "M" and c4 == "X"
            ):
                count += 1
        for c1, c2, c3, c4 in zip(l1[3:], l2[2:], l3[1:], l4):
            if (c1 == "X" and c2 == "M" and c3 == "A" and c4 == "S") or (
                c1 == "S" and c2 == "A" and c3 == "M" and c4 == "X"
            ):
                count += 1
    return count


with open("data.txt") as f:
    for line in f:
        board.append(line.strip())

print(horizontal_xmas(board) + vertical_xmas(board) + diagonal_xmas(board))
