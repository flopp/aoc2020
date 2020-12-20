import math
import re
import sys


class Tile:
    def __init__(self, rows):
        self._rows = rows
        self._edge0 = self._rows[0]
        self._edge1 = self._rows[-1]
        self._edge2 = "".join([row[0] for row in self._rows])
        self._edge3 = "".join([row[-1] for row in self._rows])
        self._edge4 = self._edge0[::-1]
        self._edge5 = self._edge1[::-1]
        self._edge6 = self._edge2[::-1]
        self._edge7 = self._edge3[::-1]
    
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
        if rotation == 4:
            return self.get(rotation - 4, y, -(x+1))

    def t(self, rotation):
        return [
            self._edge0,
            self._edge6,
            self._edge5,
            self._edge3,
            self._edge4,
            self._edge2,
            self._edge1,
            self._edge7,
        ][rotation]

    def b(self, rotation):
        return [
            self._edge1,
            self._edge7,
            self._edge4,
            self._edge2,
            self._edge5,
            self._edge3,
            self._edge0,
            self._edge6,
        ][rotation]

    def l(self, rotation):
        return [
            self._edge2,
            self._edge1,
            self._edge7,
            self._edge4,
            self._edge3,
            self._edge0,
            self._edge6,
            self._edge5,
        ][rotation]

    def r(self, rotation):
        return [
            self._edge3,
            self._edge0,
            self._edge6,
            self._edge5,
            self._edge2,
            self._edge1,
            self._edge7,
            self._edge4,
        ][rotation]


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
print(square[0][0] * square[size - 1][0] * square[(size - 1) * size][0] * square[-1][0])

print("PART2")
sea_monster = ["                  #", "#    ##    ##    ###", " #  #  #  #  #  #   "]
