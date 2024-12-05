input = open("input", "r").readlines()

lines = [lin.rstrip() for lin in input]
ROWS, COLS = len(lines), len(lines[0])
res = 0

# Part 1
directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
for r, line in enumerate(lines):
    for c, chr in enumerate(line):
        if chr == "X":
            for dr, dc in directions:
                if (r + dr * 3) < 0 or (r + dr * 3) >= ROWS or (c + dc * 3) < 0 or (c + dc * 3) >= COLS:
                    continue

                if (
                        (lines[r + dr][c + dc] == "M") and
                        (lines[r + dr * 2][c + dc * 2] == "A") and
                        (lines[r + dr * 3][c + dc * 3] == "S")
                ):
                    res += 1

print(res)
# Part 2
res = 0
for r, line in enumerate(lines):
    for c, chr in enumerate(line):
        if chr == "A":
            if r == 0 or r == ROWS - 1 or c == 0 or c == COLS - 1:
                continue
            top_left = lines[r - 1][c - 1]
            top_right = lines[r - 1][c + 1]
            bottom_left = lines[r + 1][c - 1]
            bottom_right = lines[r + 1][c + 1]

            if top_left == "M" and bottom_right == "S":
                if top_right == "S" and bottom_left == "M":
                    res += 1
                elif top_right == "M" and bottom_left == "S":
                    res += 1

            elif top_left == "S" and bottom_right == "M":
                if top_right == "S" and bottom_left == "M":
                    res += 1
                elif top_right == "M" and bottom_left == "S":
                    res += 1


print(res)
