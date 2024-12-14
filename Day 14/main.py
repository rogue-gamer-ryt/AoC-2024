from collections import Counter
import math

input = open('input').read().strip().split("\n")
ROWS = 103
COLS = 101

board = [[0] * COLS for _ in range(ROWS)]

pos = []
vel = []

def valid(x, y):
    if x < 0:
        x = COLS + x
    if x >= COLS:
        x = x % COLS

    if y < 0:
        y = ROWS + y
    if y >= ROWS:
        y = y % ROWS
    
    return x, y

def calc_quad():
    res1 = 1
    out = 0
    for row in range(math.floor(ROWS / 2)):
        for col in range(math.floor(COLS / 2)):
            out += board[row][col]
    if out > 0:
        res1 *= out

    out = 0
    for row in range(math.floor(ROWS / 2) + 1, ROWS):
        for col in range(math.floor(COLS / 2) + 1, COLS):
            out += board[row][col]
    if out > 0:
        res1 *= out

    out = 0        
    for row in range(math.floor(ROWS / 2)):
        for col in range(math.floor(COLS / 2) + 1, COLS):
            out += board[row][col]
    if out > 0:
        res1 *= out
            
    out = 0
    for row in range(math.floor(ROWS / 2) + 1, ROWS):
        for col in range(math.floor(COLS / 2)):
            out += board[row][col]
    if out > 0:
        res1 *= out

    print(res1)

for line in input:
    p, v = line.split()[0][len('p='):], line.split()[1][len('v='):]
    x, y = tuple(map(int, p.split(',')))
    vx, vy = tuple(map(int, v.split(',')))
    board[y][x] += 1
    pos.append((x, y))
    vel.append((vx, vy))

def display():
    for row in board:
        print("".join(map(str, row)).replace("0", ".").replace("1", "*"))

def solve(part1):
    s = 1
    while True:
        for i, (vx, vy) in enumerate(vel):
            x, y = pos[i]
            board[y][x] -= 1
            new_x, new_y = x + vx, y + vy
            new_x, new_y = valid(new_x, new_y)
            board[new_y][new_x] += 1
            pos[i] = (new_x, new_y)
        if part1 and s == 100:
            calc_quad()
        if max(Counter(pos).values()) == 1:
            res2 = s
            print(res2)
            break 
        s += 1

solve(part1=True)
display()