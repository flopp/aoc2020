import sys


def run(start, turns):
    turns_spoken1 = [-1] * turns
    turns_spoken2 = [-1] * turns
    spoken = 0
    for turn, spoken in enumerate(start, 1):
        turns_spoken1[spoken] = turn
    for turn in range(len(start) + 1, turns + 1):
        last = turns_spoken2[spoken]
        spoken = 0 if last == -1 else turn - 1 - last
        turns_spoken2[spoken] = turns_spoken1[spoken]
        turns_spoken1[spoken] = turn
    return spoken


start_configurations = [[int(x) for x in line.strip().split(",")] for line in sys.stdin]

print("PART1")
for start in start_configurations:
    print(run(start, 2020))

print("PART2")
for start in start_configurations:
    print(run(start, 30_000_000))
