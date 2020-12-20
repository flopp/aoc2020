import copy
import math
import re
import sys


class Tile:
    def __init__(self, rows):
        self._rows = rows

    def print(self, rotation=0):
        for y in range(self.height(rotation)):
            row = ""
            for x in range(self.width(rotation)):
                row += self.get(rotation, x, y)
            print(row)

    def count(self, char):
        return sum(row.count(char) for row in self._rows)

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
            return self._rows[-(x + 1)][y]
        if rotation == 2:
            return self._rows[-(y + 1)][-(x + 1)]
        if rotation == 3:
            return self._rows[x][-(y + 1)]
        return self.get(rotation - 4, -(x + 1), y)

    def set(self, rotation, x, y, char):
        if rotation == 0:
            self._rows[y][x] = char
        elif rotation == 1:
            self._rows[-(x + 1)][y] = char
        elif rotation == 2:
            self._rows[-(y + 1)][-(x + 1)] = char
        elif rotation == 3:
            self._rows[x][-(y + 1)] = char
        else:
            self.set(rotation - 4, -(x + 1), y, char)

    def t(self, rotation):
        return "".join([self.get(rotation, x, 0) for x in range(self.width(rotation))])

    def b(self, rotation):
        return "".join([self.get(rotation, x, -1) for x in range(self.width(rotation))])

    def l(self, rotation):
        return "".join([self.get(rotation, 0, y) for y in range(self.height(rotation))])

    def r(self, rotation):
        return "".join(
            [self.get(rotation, -1, y) for y in range(self.height(rotation))]
        )


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
        tile_rows.append(list(m[1]))
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
print(square[0][0] * square[size - 1][0] * square[(size - 1) * size][0] * square[-1][0])

print("PART2")
tile_size = tiles[square[0][0]].width(0)
grid_size = size * (tile_size - 2)
grid = Tile([["."] * grid_size for y in range(grid_size)])
for y in range(size):
    for x in range(size):
        tile_id, rotation = square[y * size + x]
        tile = tiles[tile_id]
        
        for yy in range(tile_size - 2):
            for xx in range(tile_size - 2):
                grid.set(
                    0,
                    xx + (tile_size - 2) * x,
                    yy + (tile_size - 2) * y,
                    tile.get(rotation, xx + 1, yy + 1),
                )

monster_lines = ["                  # ", "#    ##    ##    ###", " #  #  #  #  #  #   "]
monster = Tile([list(line) for line in monster_lines])
monster_w = monster.width(0)
monster_h = monster.height(0)
monster_xy = []
for y in range(monster_h):
    for x in range(monster_w):
        if monster.get(0, x, y) == "#":
            monster_xy.append((x, y))

for rotation in range(8):
    count = 0
    for y in range(grid_size - monster_h):
        for x in range(grid_size - monster_w):
            for (xx, yy) in monster_xy:
                if grid.get(rotation, x + xx, y + yy) != "#":
                    break
            else:
                for (xx, yy) in monster_xy:
                    grid.set(rotation, x + xx, y + yy, "O")
                count += 1
    if count > 0:
        grid.print(rotation)
        print(count)
        print(grid.count("#"))
        break
