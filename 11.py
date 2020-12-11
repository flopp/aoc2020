import sys

grid = [[char for char in line.strip()] for line in sys.stdin]

def sim(g):
    g2 = []
    w = len(g[0])
    h = len(g)
    for y in range(h):
        r2 = []
        for x in range(w):
            current = g[y][x]
            if current == '.':
                r2.append('.')
                continue
            around = 0
            for y2 in range (max(0, y-1), min(h, y+2)):
                for x2 in range (max(0, x-1), min(w, x+2)):
                    #print(f'y={y2}/{h} x={x2}/{w}')
                    if y2 == y and x2 == x:
                        continue
                    around += (g[y2][x2] == '#')
            if current == 'L' and around == 0:
                r2.append('#')
            elif current == '#' and around >= 4:
                r2.append('L')
            else:
                r2.append(current)
        g2.append(r2)
    return g2


print("PART1")
while True:
    new_grid = sim(grid)
    if new_grid == grid:
        break
    grid = new_grid
print(sum(r.count('#') for r in grid))


