from collections import defaultdict

input = open("input", "r").readlines()
board = []
for line in input:
    line = line.strip()
    board.append(list(line))

res = 0
ROWS, COLS = len(board), len(board[0])
antennas = defaultdict(list)
for row, line in enumerate(board):
    for col, cell in enumerate(line):
        if cell != ".":
            antennas[cell].append((row, col))

out1 = set()
seen = set()
for antenna in antennas.values():
    if len(antenna) > 1:
        for a1 in antenna:
            for a2 in antenna:

                if a1 == a2:
                    continue
                if (a1, a2) in seen or (a2, a2) in seen:
                    continue
                seen.add((a1, a2))

                dr = a1[0] - a2[0]
                dc = a1[1] - a2[1]

                anti_node_1 = (a1[0] + dr, a1[1] + dc)
                anti_node_2 = (a2[0] - dr, a2[1] - dc)

                if (
                        0 <= anti_node_1[0] < ROWS
                        and 0 <= anti_node_1[1] < COLS
                ):
                    out1.add(anti_node_1)

                if (
                        0 <= anti_node_2[0] < ROWS
                        and 0 <= anti_node_2[1] < COLS
                ):
                    out1.add(anti_node_2)
res1 = len(out1)

out2 = set()
seen = set()

for antenna in antennas.values():
    if len(antenna) > 1:
        for a1 in antenna:
            for a2 in antenna:
                if a1 == a2:
                    continue

                if (a1, a2) in seen or (a2, a1) in seen:
                    continue

                seen.add((a1, a2))

                dr = a1[1] - a2[1]
                dc = a1[0] - a2[0]

                for prev in [a1, a2]:
                    for sign in [-1, 1]:
                        while True:
                            new_node = (
                                prev[0] + (sign * dc),
                                prev[1] + (sign * dr),
                            )

                            if (
                                    0 <= new_node[0] < ROWS
                                    and 0 <= new_node[1] < COLS
                            ):
                                out2.add(new_node)
                            else:
                                break

                            prev = new_node

res2 = len(out2)

print(f"Result 1: {res1}")
print(f"Result 2: {res2}")




