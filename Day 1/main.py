# Part 1
import collections

input = open("input", "r")
l1, l2 = [], []
for line in input:
    a, b = line.split()
    l1.append(int(a))
    l2.append(int(b))

l1.sort()
l2.sort()
d = 0
for a, b in zip(l1, l2):
    d += abs(a - b)
print(d)

# Part 2

count_l2 = collections.Counter(l2)
ss = 0
for n in l1:
    ss += n * count_l2[n]

print(ss)