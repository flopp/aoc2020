import sys

grid = [[char for char in line.strip()] for line in sys.stdin]
directions = [
    (-1, -1),
    (-1, 0),
    (-1, +1),
    (0, -1),
    (0, +1),
    (+1, -1),
    (+1, 0),
    (+1, +1),
]


def look_part1(g, x, y, w, h):
    global directions
    around = 0
    for dy, dx in directions:
        y2 = y + dy
        x2 = x + dx
        if (0 <= y2 < h) and (0 <= x2 < w):
            around += g[y2][x2] == "#"
    return around


def look_part2(g, x, y, w, h):
    global directions
    around = 0
    for dy, dx in directions:
        y2 = y
        x2 = x
        while True:
            y2 += dy
            x2 += dx
            if (0 <= y2 < h) and (0 <= x2 < w):
                c = g[y2][x2]
                if c == "#":
                    around += 1
                    break
                if c == "L":
                    break
            else:
                break
    return around


def sim(g, look, sensitivity):
    changed = True
    w = len(g[0])
    h = len(g)
    while changed:
        changed = False
        g2 = []
        for y, r in enumerate(g):
            r2 = list(r)
            for x, c in enumerate(r):
                if c == "L":
                    if look(g, x, y, w, h) == 0:
                        r2[x] = "#"
                        changed = True
                elif c == "#":
                    if look(g, x, y, w, h) >= sensitivity:
                        r2[x] = "L"
                        changed = True
            g2.append(r2)
        g = g2
    return sum(r.count("#") for r in g)


print("PART1")
print(sim(grid, look_part1, 4))

print("PART2")
print(sim(grid, look_part2, 5))
