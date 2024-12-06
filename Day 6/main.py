input = open("input", "r").read()
input = input.split('\n')
res = 0
ROWS, COLS = len(input), len(input[0])
board = [["."] * COLS for _ in range(COLS)]
for r in range(ROWS):
    for c in range(COLS):
        if input[r][c] in "^":
            start = (r, c)
        board[r][c] = input[r][c]


def check(check_cycles=False):
    row, col = start[0], start[1]
    d = 0  # 1 UP, 2 RIGHT, 3 DOWN, 4 LEFT
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    out2 = set()

    while True:
        if 0 <= row < ROWS and 0 <= col < COLS and board[row][col] != "#":
            res1.append((row, col))
            if check_cycles:
                if (row, col, d) in out2:
                    return True
                else:
                    out2.add((row, col, d))
            row, col = row + directions[d][0], col + directions[d][1]
        elif board[row][col] == "#":
            row, col = row - directions[d][0], col - directions[d][1]
            d += 1
            d = d % 4
            row, col = row + directions[d][0], col + directions[d][1]
            res1.append((row, col))

        if row < 0 or row == ROWS or col < 0 or col == COLS:
            break

    return False


res1 = []
check()
print(len(set(res1)))
res2 = 0
for r in range(ROWS):
    for c in range(COLS):
        if board[r][c] == ".":
            board[r][c] = "#"
            if check(True):
                res2 += 1

            board[r][c] = "."
print(res2)

# def display(row, col):
#
#     for r in range(ROWS):
#         for c in range(COLS):
#             if r == row and c == col:
#                 board[r][c] = "^"
#             if input[r][c] == "#":
#                 board[r][c] = "#"
#
#     for r in board:
#         for c in r:
#             print(c, end="")
#         print("")
#     print("\n")
