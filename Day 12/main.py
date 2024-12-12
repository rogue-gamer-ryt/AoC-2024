from collections import deque
input = open('input').read().strip().split()
grid = [[c for c in row] for row in input]
ROWS, COLS = len(grid), len(grid[0])
visited = set()
dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
diag = [(1, -1), (-1, -1), (-1, 1), (1, 1)]
    

def bfs(r, c, val):
    count_area = 0
    group = set()
    q = deque([])
    q.append([r, c])
    out1 = 0
    out2 = 0
    while q:
        r, c = q.popleft()
        if r < 0 or r == ROWS or c < 0 or c == COLS or grid[r][c] != val or (r, c) in visited:
            continue

        count_area += 1
        visited.add((r,c))
        group.add((r, c))

        for dr, dc in dirs:
            row, col = r + dr, c + dc
            q.append((row, col))
    
    for r, c in group:
        for dr, dc in dirs:
            if ((r + dr), (c + dc)) not in group:
                out1 += 1

    for r, c in group:
        for r1, c1, r2, c2, r3, c3 in [(r+1,c,r,c-1,r+1,c-1),(r-1,c,r,c-1,r-1,c-1),(r,c+1,r-1,c,r-1,c+1),(r,c-1,r-1,c,r-1,c-1)]:
            if (r1, c1) not in group and not ((r2, c2) in group and (r3, c3) not in group):
                out2 += 1
           


    return count_area, out1, out2

res1 = 0
res2 = 0
for r in range(ROWS):
    for c in range(COLS):
        if (r,c) not in visited:
            count_area, perimeter, perimeter2 = bfs(r, c, grid[r][c])
            res1 += (count_area * perimeter)
            res2 += (count_area * perimeter2)
print(res1)
print(res2)

