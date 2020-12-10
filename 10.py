import sys

adapters = sorted([int(line) for line in sys.stdin])

print("PART1")
diff = [0, 0, 0, 1]
last = 0
for rating in adapters:
    diff[rating - last] += 1
    last = rating
print(diff[1] * diff[3])

