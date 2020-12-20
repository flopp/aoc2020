import math
import re
import sys


class Tile:
    def __init__(self, rows):
        self._rows = rows
    
    def print(self):
        for row in self._rows:
            print(''.join(row))

    def width(self, rotation):
        if rotation in [0, 2, 4, 6]:
            return len(self._rows[0])
        else:
            return len(self._rows)
    
    def height(self, rotation):
        if rotation in [0, 2, 4, 6]:
            return len(self._rows)
        else:
            return len(self._rows[0])
    
    def get(self, rotation, x, y):
        if rotation == 0:
            return self._rows[y][x]
        if rotation == 1:
            return self._rows[-(x+1)][y]
        if rotation == 2:
            return self._rows[-(y+1)][-(x+1)]
        if rotation == 3:
            return self._rows[x][-(y+1)]
        return self.get(rotation - 4, -(x+1), y)
    
    def set(self, rotation, x, y, char):
        if rotation == 0:
            self._rows[y][x] = char
        elif rotation == 1:
            self._rows[-(x+1)][y] = char
        elif rotation == 2:
            self._rows[-(y+1)][-(x+1)] = char
        elif rotation == 3:
            self._rows[x][-(y+1)] = char
        else:
            self.set(rotation - 4, -(x+1), y, value)

    def t(self, rotation):
        return ''.join([self.get(rotation, x, 0) for x in range(self.width(rotation))])

    def b(self, rotation):
        return ''.join([self.get(rotation, x, -1) for x in range(self.width(rotation))])

    def l(self, rotation):
        return ''.join([self.get(rotation, 0, y) for y in range(self.height(rotation))])

    def r(self, rotation):
        return ''.join([self.get(rotation, -1, y) for y in range(self.height(rotation))])

    def insert(self, tile, rotation, x, y):
        for yy in range(tile.height(rotation)):
            for xx in range(tile.width(rotation)):
                self.set(0, xx + x, yy + y, tile.get(rotation, xx, yy))



re_tile = re.compile(r"^Tile (\d+):$")
re_row = re.compile(r"^([#\.]+)$")

tiles = {}
tile_id = None
tile_rows = []
for line in sys.stdin:
    if m := re_tile.match(line):
        if tile_id is not None:
            tiles[tile_id] = Tile(tile_rows)
        tile_id = int(m[1])
        tile_rows = []
    elif m := re_row.match(line):
        tile_rows.append(m[1])
if tile_id is not None:
    tiles[tile_id] = Tile(tile_rows)


def find_top_left(tiles):
    edges = {}
    for tile_id, tile in tiles.items():
        for rotation in range(8):
            edge = tile.t(rotation)
            if edge in edges:
                edges[edge].append((tile_id, rotation))
            else:
                edges[edge] = [(tile_id, rotation)]
    candidates = []
    for tile_id, tile in tiles.items():
        for rotation in range(8):
            if len(edges[tile.t(rotation)]) == 1 and len(edges[tile.l(rotation)]) == 1:
                candidates.append((tile_id, rotation))
    assert len(candidates) == 8
    return candidates[0]


def find_edge_t(tiles, remaining, edge):
    for tile1 in remaining:
        tile = tiles[tile1]
        for rotation1 in range(8):
            if tile.t(rotation1) == edge:
                return tile1, rotation1


def find_edge_l(tiles, remaining, edge):
    for tile1 in remaining:
        tile = tiles[tile1]
        for rotation1 in range(8):
            if tile.l(rotation1) == edge:
                return tile1, rotation1


size = int(math.sqrt(len(tiles)))
square = []
remaining = set(tiles.keys())

for y in range(size):
    for x in range(size):
        if x == 0 and y == 0:
            tile1, rotation1 = find_top_left(tiles)
        elif x == 0:
            tile0, rotation0 = square[-size]
            edge0 = tiles[tile0].b(rotation0)
            tile1, rotation1 = find_edge_t(tiles, remaining, edge0)
        else:
            tile0, rotation0 = square[-1]
            edge0 = tiles[tile0].r(rotation0)
            tile1, rotation1 = find_edge_l(tiles, remaining, edge0)
        square.append((tile1, rotation1))
        remaining.remove(tile1)

print("PART1")
print(square[0][0] * square[size-1][0] * square[(size-1)*size][0] * square[-1][0])

print("PART2")
tile_size = tiles[square[0][0]].width(0)
rows = []
for y in range(2 + size * (tile_size - 2)):
    rows.append(['.'] * (2 + size * (tile_size - 2)))
grid = Tile(rows)
for y in range(size):
    if y == 0:
        sy = 0
        h = tile_size - 1
    elif y == size - 1:
        sy = 1
        h = tile_size - 1
    else:
        sy = 1
        h = tile_size - 2
    for x in range(size):
        tile_id, rotation = square[y * size + x]
        tile = tiles[tile_id]
        if x == 0:
            sx = 0
            w = tile_size - 1
        elif x == size - 1:
            sx = 1
            w = tile_size - 1
        else:
            sx = 1
            w = tile_size - 2
        for yy in range(h):
            for xx in range(w):
                grid.set(0, xx + x * w, yy + y * h, tile.get(rotation, xx + sx, yy + sy))
grid.print()
