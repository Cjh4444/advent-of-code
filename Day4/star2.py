import re

board = []


def xmas_pieces(board):
    count = 0
    for l1, l2, l3 in zip(board, board[1:], board[2:]):
        for i in range(len(l1) - 2):
            TL_BR_MAS = (
                (l1[i] == "M") and (l2[i + 1] == "A") and (l3[i + 2] == "S")
            )
            TR_BL_MAS = (
                (l1[i + 2] == "M") and (l2[i + 1] == "A") and (l3[i] == "S")
            )
            BL_TR_MAS = (
                (l3[i] == "M") and (l2[i + 1] == "A") and (l1[i + 2] == "S")
            )
            BR_TL_MAS = (
                (l3[i + 2] == "M") and (l2[i + 1] == "A") and (l1[i] == "S")
            )

            if sum([TL_BR_MAS, TR_BL_MAS, BL_TR_MAS, BR_TL_MAS]) >= 2:
                count += 1
    return count


with open("data.txt") as f:
    for line in f:
        board.append(line.strip())

print(xmas_pieces(board))
