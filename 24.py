import sys

directions_list = []
for line in sys.stdin:
    directions = []
    last = None
    for char in line.strip():
        if last == None:
            if char in ['e', 'w']:
                directions.append(char)
            else:
                last = char
        else:
            directions.append(last + char)
            last = None
    directions_list.append(directions)

def go(x, y, d):
    if d == 'e':
        return x + 1, y
    elif d == 'w':
        return x - 1, y
    elif d == 'ne':
        return x + (y % 2), y - 1
    elif d == 'se':
        return x + (y % 2), y + 1
    elif d == 'sw':
        return x - 1 + (y % 2), y + 1
    else:
        # d == 'nw'
        return x - 1 + (y % 2), y - 1

def flip(black, x, y):
    if (x, y) in black:
        black.remove((x, y))
    else:
        black.add((x, y))

def neighbors(x, y):
    for d in ['e', 'w', 'ne', 'se', 'sw', 'nw']:
        yield go(x, y, d)

def black_neighbors(black, x, y):
    return sum(((nx, ny) in black) for (nx, ny) in neighbors(x, y))

def white_with_black_neighbor(black):
    seen = set()
    for (x, y) in black:
        for wx, wy in neighbors(x, y):
            if (wx, wy) in black or (wx, wy) in seen:
                continue
            seen.add((wx, wy))
            yield wx, wy

print("PART1")
black = set()
for directions in directions_list:
    x, y = 0, 0
    for d in directions:
        x, y = go(x, y, d)
    flip(black, x, y)
print(len(black))

print("PART2")
for _ in range(100):
    black2 = set()
    for (x, y) in black:
        if 0 < black_neighbors(black, x, y) <= 2:
            black2.add((x, y))
    for (x, y) in white_with_black_neighbor(black):
        if black_neighbors(black, x, y) == 2:
            black2.add((x, y))
    black = black2
print(len(black))
