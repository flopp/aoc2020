import sys

adapters = sorted([int(line) for line in sys.stdin])

print("PART1")
diff = [0, 0, 0, 1]
last = 0
for rating in adapters:
    diff[rating - last] += 1
    last = rating
print(diff[1] * diff[3])

print("PART2")


def arrangements(joltage, adapters, arrangements_from):
    if joltage in arrangements_from:
        return arrangements_from[joltage]
    if joltage not in adapters:
        return 0
    arrangements_from[joltage] = sum(
        arrangements(joltage + d, adapters, arrangements_from) for d in range(1, 4)
    )
    return arrangements_from[joltage]


print(arrangements(0, set(adapters).union({0}), {max(adapters) + 3: 1}))
