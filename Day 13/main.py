from sympy import symbols, Eq, solve
input = open('input').read().strip().split("\n\n")
res1 = 0
res2 = 0
count_a, count_b = symbols('count_a count_b', integer=True)
ans = []

def calc(part2 = False):
    out = 0
    for block in input:
        
        lines = block.split("\n")
        aX, aY = lines[0].split(",")
        bX, bY = lines[1].split(",")
        pX, pY = lines[2].split(",")
        x_a, y_a = tuple(map(int, (aX[len("Button A: X+"):] , aY[len(" Y+"):])))
        x_b, y_b = tuple(map(int, (bX[len("Button B: X+"):] , bY[len(" Y+"):])))
        x_p, y_p = tuple(map(int, (pX[len("Prize: X="):] , pY[len(" Y="):])))
        if part2:
            x_p, y_p = 10000000000000 + x_p, 10000000000000+ y_p
        min_cost = float('inf')
        eq1 = Eq(count_a * x_a + count_b * x_b, x_p)
        eq2 = Eq(count_a * y_a + count_b * y_b, y_p)
        
        sols = solve((eq1, eq2), (count_a, count_b), dict=True)
        possib_answers = [(s[count_a], s[count_b]) for s in sols if s[count_a] >= 0 and s[count_b] >= 0]
        found = False
        for a, b in possib_answers:
            tot = 3 * a + b
            if tot < min_cost:
                min_cost = tot
                found = True
        if found:
            out+= min_cost
    return out
    
res1 = calc()
res2 = calc(part2=True)
print(res1)
print(res2)

    