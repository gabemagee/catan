import random
from enum import Enum
from typing import Dict
from typing import Optional
from typing import Sequence

import hexlib


class Direction(Enum):
    RIGHT = 0
    UPPER_RIGHT = 1
    UPPER_LEFT = 2
    LEFT = 3
    LOWER_LEFT = 4
    LOWER_RIGHT = 5


class ResourceType(Enum):
    DESERT = 0
    CLAY = 1
    ORE = 2
    SHEEP = 3
    WHEAT = 4
    WOOD = 5


# Possible Resources for a 19 tile game
RESOURCES = [ResourceType.DESERT] + [ResourceType.CLAY] * 3 + [ResourceType.ORE] * 3 + [ResourceType.SHEEP] * 4 + [
    ResourceType.WHEAT] * 4 + [ResourceType.WOOD] * 4
NUMERALS = [2, 3, 3, 4, 4, 5, 5, 6, 6, 8, 8, 9, 9, 10, 10, 11, 11, 12]


class Tile:
    resource: ResourceType
    hex: hexlib.Hex
    numeral: int
    board: "Board"

    def __init__(self, resource: ResourceType, hex: hexlib.Hex, numeral: int, board: "Board"):
        self.resource: ResourceType = resource
        self.hex = hex
        self.numeral = numeral
        self.board = board
        self.settlements = []
        self.cities = []
        self.roads = []

    @property
    def neighbors(self) -> Sequence["Tile"]:
        neighbors = []
        for i in range(6):
            neighbor = self.board.get_tile_by_hex(hexlib.hex_neighbor(self.hex, i))
            if neighbor is not None:
                neighbors.append(neighbor)
        return neighbors

    def is_neighbors(self, other_tile: "Tile") -> bool:
        return other_tile in self.neighbors


class City:

    def __init__(self, player, q, r, s):
        self.player = player
        self.q = q
        self.r = r
        self.s = s

    def is_touching_tile(self, tile: Tile) -> bool:
        return self.q == tile.hex.q or self.r == tile.hex.r or self.s == tile.hex.s


class Settlement:

    def __init__(self, player, q, r, s):
        self.player = player
        self.q = q
        self.r = r
        self.s = s

    def is_touching_tile(self, tile: Tile) -> bool:
        return self.q == tile.hex.q or self.r == tile.hex.r or self.s == tile.hex.s


class Road:

    def __init__(self, player, q_1, r_1, s_1, q_2, r_2, s_2) -> None:
        self.player = player
        self.coords_one = (q_1, r_1, s_1)
        self.coords_two = (q_2, r_2, s_2)


class Harbor:
    class HarborType(Enum):
        WILDCARD = 0
        CLAY = 1
        ORE = 2
        SHEEP = 3
        WHEAT = 4
        WOOD = 5

    def __init__(self, location, harbor_type: HarborType) -> None:
        self.location = location
        self.harbor_type = harbor_type


class Bandit:

    def __init__(self, tile) -> None:
        self.tile = tile

    def move(self, tile) -> None:
        self.tile = tile


class Board:
    tiles_by_numeral: Dict[int, Tile]
    tiles: Dict[int, Dict[int, Dict[int, Tile]]]
    diameter: int
    side_length: int
    max_factor: int

    def __init__(self):
        # 19 tile game
        self.diameter = 5
        self.side_length = 3
        self.max_factor = self.side_length - 1
        self.cities = []
        self.settlements = []
        self.populate_tiles()

    def populate_tiles(self):
        available_resources = RESOURCES.copy()
        numerals = NUMERALS.copy()
        random.shuffle(available_resources)
        random.shuffle(numerals)
        tiles = {}
        tiles_by_numeral = {}
        for q in range(-self.max_factor, self.max_factor):
            tiles[q] = {}
            for r in range(-self.max_factor, self.max_factor):
                tiles[q][r] = {}
                for s in range(-self.max_factor, self.max_factor):
                    resource = available_resources.pop()
                    numeral = 0
                    if resource != ResourceType.DESERT:
                        numeral = numerals.pop()
                    tile = Board.Tile(resource, hexlib.Hex(q, r, s), numeral, self)
                    tiles[q][r][s] = tile
                    tiles_by_numeral[numeral] = tiles_by_numeral.get(numeral, []) + [tile]
        self.tiles = tiles
        self.tiles_by_numeral = tiles_by_numeral

    def get_tiles_with_numeral(self, numeral: int):
        if numeral < 2 or numeral > 12 or numeral == 7:
            raise ValueError("Not a valid numeral")
        return self.tiles_by_numeral[numeral]

    def get_tile_by_hex(self, hex: hexlib.Hex) -> Optional[Tile]:
        try:
            return self.tiles[hex.q][hex.r][hex.s]
        except KeyError:
            return None

    def add_settlement(self, player, q, r, s) -> Settlement:
        settlement = Settlement(player, q, r, s)
        self.settlements.append(settlement)
        return settlement

    def upgrade_settlement_to_city(self, settlement) -> City:
        city = City(settlement.player, settlement.q, settlement.r, settlement.s)
        self.cities.append(city)
        self.settlements.remove(settlement)
        del settlement
        return city

