import sys


def tokensize(s):
    tokens = []
    num = ""
    for char in s:
        if char.isnumeric():
            num += char
        else:
            if len(num) > 0:
                tokens.append(int(num))
                num = ""
            if not char.isspace():
                tokens.append(char)
    if len(num) > 0:
        tokens.append(int(num))
    return tokens


expressions = [tokensize(line) for line in sys.stdin]


def compute1(expression):
    value = 0
    op = "+"
    while op != ")":
        e = expression.pop(0)
        if not isinstance(e, int):
            assert e == "("
            e = compute1(expression)

        if op == "+":
            value += e
        elif op == "*":
            value *= e

        if len(expression) == 0:
            op = ")"
        else:
            op = expression.pop(0)
    return value


def compute2(expression):
    return 0


print("PART1")
print(sum(compute1(list(e)) for e in expressions))

print("PART2")
print(sum(compute2(list(e)) for e in expressions))
