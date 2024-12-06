from collections import defaultdict, deque

input = open("input", "r").read()
rules, orders = input.split('\n\n')

adj_before = defaultdict(set)
adj_after = defaultdict(set)
res = 0
res2 = 0
for line in rules.split('\n'):
    u, v = line.split('|')
    u, v = int(u), int(v)
    adj_before[v].add(u)
    adj_after[u].add(v)

for order in orders.split('\n'):
    int_order = [int(o) for o in order.split(',')]
    valid = True
    out = []

    for i, src in enumerate(int_order):
        for j, dst in enumerate(int_order):
            if i < j and dst in adj_before[src]:
                valid = False
    if valid:
        res += int_order[len(int_order)//2]
    else:
        q = deque()
        indegree = {v: len(adj_before[v] & set(int_order)) for v in int_order}
        for v in int_order:
            if indegree[v] == 0:
                q.append(v)
        while q:
            node = q.popleft()
            if node not in int_order:
                continue
            out.append(node)
            for nei in adj_after[node]:
                if nei in indegree:
                    indegree[nei] -= 1
                    if indegree[nei] == 0:
                        q.append(nei)
        res2 += out[len(out)//2]


print(res)
print(res2)
