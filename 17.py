import sys

cubes3 = set()
cubes4 = set()
for y, line in enumerate(sys.stdin):
    for x, char in enumerate(line):
        if char == "#":
            cubes3.add((x, y, 0))
            cubes4.add((x, y, 0, 0))


def simulate(cubes, neighbors):
    positions = set()
    for cube in cubes:
        for neighbor in neighbors(cube):
            positions.add(neighbor)
    next_cubes = set()
    for cube in positions:
        active = cube in cubes
        count = sum(1 for x in neighbors(cube) if x in cubes) - active
        if (active and (2 <= count <= 3)) or (count == 3):
            next_cubes.add(cube)
    return next_cubes


print("PART1")


def neighbors3(cube):
    x, y, z = cube
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            for dz in range(-1, 2):
                yield x + dx, y + dy, z + dz


for cycle in range(6):
    cubes3 = simulate(cubes3, neighbors3)
print(len(cubes3))


print("PART2")


def neighbors4(cube):
    x, y, z, w = cube
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            for dz in range(-1, 2):
                for dw in range(-1, 2):
                    yield x + dx, y + dy, z + dz, w + dw


for cycle in range(6):
    cubes4 = simulate(cubes4, neighbors4)
print(len(cubes4))
