import fileinput
import itertools
import math

expenses = [int(line) for line in fileinput.input()]

print("PART1")
print([math.prod(c) for c in itertools.combinations(expenses, 2) if sum(c) == 2020][0])

print("PART2")
print([math.prod(c) for c in itertools.combinations(expenses, 3) if sum(c) == 2020][0])
