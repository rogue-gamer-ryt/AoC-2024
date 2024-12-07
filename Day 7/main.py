from itertools import product

input = open("input", "r").readlines()

res1 = 0
res2 = 0


def _eval(numbers, ops):
    result = numbers[0]
    exp = []

    for i, op in enumerate(ops):
        if op == '+':
            result += numbers[i + 1]
        elif op == '*':
            result *= numbers[i + 1]
        elif op == "|":
            exp.append(result)
            result = int("".join([str(result), str(numbers[i + 1])]))
    return result


for line in input:
    out, dig_str = line.strip().split(':')
    out = int(out)
    nums = [int(d) for d in dig_str.split()]
    all_operators_1 = product("+*", repeat=len(nums) - 1)
    all_operators_2 = product("+*|", repeat=len(nums) - 1)
    seen = set()

    for operators in all_operators_1:
        if _eval(nums, operators) == out:
            res1 += out
            seen.add(tuple(nums))
            break
    for operators in all_operators_2:
        if tuple(nums) in seen:
            break
        if _eval(nums, operators) == out:
            res2 += out
            break
print(f"Result1 = {res1}")
print(f"Result2 = {res1 + res2}")
