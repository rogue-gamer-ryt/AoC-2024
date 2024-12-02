input = open("input", "r")
levels = []
for line in input:
    levels.append(line.strip().split(" "))

# Part 1
res = 0
for lev in levels:
    increasing, decreasing, valid = False, False, True
    for i in range(len(lev) - 1):
        a, b = int(lev[i]), int(lev[i + 1])
        if abs(a - b) not in {1, 2, 3}:
            valid = False
            break
        if a > b:
            decreasing = True
        elif a < b:
            increasing = True

        if increasing and decreasing:
            valid = False
            break
    if valid:
        res += 1
print(res)


# Part 2
def check(lev):
    count = 0

    for i in range(len(lev) - 1):
        a, b = int(lev[i]), int(lev[i + 1])
        if a > b and abs(a - b) < 4:
            count += 1

    if count == len(lev) - 1:
        return True

    count = 0
    for i in range(len(lev) - 1):
        a, b = int(lev[i]), int(lev[i + 1])
        if a < b and abs(a - b) < 4:
            count += 1

    if count == len(lev) - 1:
        return True

    return False


res = 0

for lev in levels:
    if check(lev):
        res += 1
    else:
        for i in range(len(lev)):
            if check(lev[:i] + lev[i + 1:]):
                res += 1
                break
print(res)
