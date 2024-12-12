input = open('input').read().strip().split()
print(input)
input = [int(i) for i in input]

cache = {}
def compute(n , t):
    strn = str(n)
    if (n, t) in cache:
        return cache[(n, t)]
    if t == 0:
        ret = 1
    elif n == 0:
        ret = compute(1, t - 1)
    elif len(strn) % 2 == 0:
        half = len(str(strn)) // 2
        l, r = int(strn[:half]), int(strn[half:])
        ret = compute(l, t-1) + compute(r, t - 1)
    else:
        ret = compute(n*2024, t-1)
    cache[(n, t)] = ret
    return ret
res = 0
for d in input:
    res += compute(d, 75)

print(res)