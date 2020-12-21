from collections import Counter
from math import sqrt
import numpy as np


class Tile(list):
    def __init__(self, tile_id, tile):
        super().__init__(tile)
        self.id = tile_id
        self.tile = tile

    def left(self):
        return ''.join(row[0] for row in self)

    def right(self):
        return ''.join(row[-1] for row in self)

    def up(self):
        return self[0]

    def down(self):
        return self[-1]

    def flip_y(self):
        return Tile(self.id, self.tile[::-1])

    def rotate(self):
        n = len(self)
        return Tile(self.id, [''.join(self.tile[n - j - 1][i] for j in range(n)) for i in range(n)])


def parse_tiles(data):
    tiles = []
    for block in data.strip().split('\n\n'):
        lines = block.split('\n')
        tile_id = int(lines[0].split()[1][:-1])
        tile = lines[1:]
        tiles.append(Tile(tile_id, tile))
    return tiles


def reverse(s):
    return s[::-1]


def count_edges(tiles):
    cnt = Counter()
    for tile in tiles:
        cnt.update([
            tile.left(), reverse(tile.left()),
            tile.right(), reverse(tile.right()),
            tile.up(), reverse(tile.up()),
            tile.down(), reverse(tile.down())
        ])
    return cnt


def find_corners(tiles):
    cnt = count_edges(tiles)
    corners = []
    for tile in tiles:
        not_paired = 0
        for edge in [tile.left(), tile.right(), tile.up(), tile.down()]:
            not_paired += cnt.get(edge) == 1
        if not_paired == 2:
            corners.append(tile)
    return corners


def part1(data):
    tiles = parse_tiles(data)
    corners = find_corners(tiles)
    return np.product([corner.id for corner in corners])


def build_edge_index(tiles):
    index = {}
    for tile in tiles:
        for edge in [tile.left(), reverse(tile.left()), tile.right(), reverse(tile.right()),
                     tile.up(), reverse(tile.up()), tile.down(), reverse(tile.down())]:
            index[edge] = index.get(edge, []) + [tile.id]
    return index


def find_orientation(tile, func):
    for flip_y in range(2):
        if flip_y:
            tile = tile.flip_y()
        for _ in range(4):
            if func(tile):
                return tile
            tile = tile.rotate()
    return None


def concat_tiles(sea_tiles):
    full = []
    for tiles_row in sea_tiles:
        for i in range(1, len(tiles_row[0]) - 1):
            full.append(''.join(tile[i][1:-1] for tile in tiles_row))
    return Tile(0, full)


def find_monsters(sea):
    n = len(sea)
    monsters = []
    deltas = ((0, 0), (0, 5), (0, 6), (0, 11), (0, 12), (0, 17), (0, 18), (0, 19),
              (-1, 18), (1, 1), (1, 4), (1, 7), (1, 10), (1, 13), (1, 16))
    for i in range(1, n - 1):
        for j in range(n - 19):
            valid = True
            for di, dj in deltas:
                if sea[i + di][j + dj] != '#':
                    valid = False
                    break
            if valid:
                monsters.append((i, j))
    return monsters


def part2(data):
    tiles = parse_tiles(data)
    cnt = count_edges(tiles)
    corners = find_corners(tiles)
    tile_index = {tile.id: tile for tile in tiles}
    edge_index = build_edge_index(tiles)

    N = int(sqrt(len(tiles)))
    sea = [[None] * N for _ in range(N)]
    used = set()
    for i in range(N):
        for j in range(N):
            if i == 0 and j == 0:
                sea[i][j] = find_orientation(
                    corners[0],
                    lambda tile: cnt.get(tile.left()) == 1 and cnt.get(tile.up()) == 1
                )
            elif i == 0:
                ids = edge_index[sea[i][j - 1].right()]
                tile_id = ids[0] if ids[0] not in used else ids[1]
                sea[i][j] = find_orientation(
                    tile_index[tile_id],
                    lambda tile: cnt.get(tile.up()) == 1 and tile.left() == sea[i][j-1].right()
                )
            elif j == 0:
                ids = edge_index[sea[i - 1][j].down()]
                tile_id = ids[0] if ids[0] not in used else ids[1]
                sea[i][j] = find_orientation(
                    tile_index[tile_id],
                    lambda tile: cnt.get(tile.left()) == 1 and tile.up() == sea[i-1][j].down()
                )
            else:
                ids = edge_index[sea[i - 1][j].down()]
                tile_id = ids[0] if ids[0] not in used else ids[1]
                sea[i][j] = find_orientation(
                    tile_index[tile_id],
                    lambda tile: tile.left() == sea[i][j-1].right() and tile.up() == sea[i-1][j].down()
                )
            used.add(sea[i][j].id)

    sea = concat_tiles(sea)
    sea_oriented = find_orientation(sea, lambda sea: len(find_monsters(sea)) > 0)
    monsters = find_monsters(sea_oriented)
    cnt_sharp = ''.join(sea_oriented).count('#')
    return cnt_sharp - len(monsters) * 15
