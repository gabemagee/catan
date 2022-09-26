import random
from enum import Enum
from typing import Dict
from typing import Optional
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


class Board:
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

        def get_neighbors(self, board):
            neighbors = []
            for i in range(6):
                neighbor = board.get_tile_by_hex(hexlib.hex_neighbor(self.hex, i))
                if neighbor is not None:
                    neighbors.append(neighbor)
            return neighbors

    class City:

        def __init__(self, player, tile_one, tile_two: Optional[Tile] = None, tile_three: Optional[Tile] = None):
            self.player = player
            self.tile_one = tile_one
            self.tile_two = tile_two
            self.tile_three = tile_three

    class Settlement:

        def __init__(self, player, tile_one, tile_two: Optional[Tile] = None, tile_three: Optional[Tile] = None):
            self.player = player
            self.tile_one = tile_one
            self.tile_two = tile_two
            self.tile_three = tile_three

    class Road:

        def __init__(self, player, tile_one: Tile, tile_two: Tile = None) -> None:
            self.player = player
            self.tile_one = tile_one
            self.tile_two = tile_two

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
