import re

input = open("input", "r").read()

# Part 1
res = 0
pattern = re.compile(r"mul[(][0-9][0-9]?[0-9]?,[0-9][0-9]?[0-9]?[)]")

itr = pattern.finditer(input)
for match in itr:
    vals = eval(match.group()[3:])
    res += int(vals[0]) * int(vals[1])
print(res)

# Part 2

pattern = re.compile(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)")
itr = pattern.finditer(input)
res = 0
dont = False
for match in itr:
    command = match.group()
    if "don't()" in command:
        dont = True
    elif "do()" in command:
        dont = False
    if dont:
        continue
    else:
        a, b = (eval(match.group()[3:]))
        res += a * b
print(res)












