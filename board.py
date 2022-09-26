import math
import os
from enum import Enum
import hexlib
import random
from typing import Optional
from abc import ABC, abstractmethod


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

    def __init__(self, resource: ResourceType, hex: hexlib.Hex, numeral: int):
        self.resource: ResourceType = resource
        self.hex = hex
        self.numeral = numeral

    def getNeighbors(self):
        pass

    def getSettlements(self):
        pass

    def getCities(self):
        pass


class Board:

    def __init__(self):
        # 19 tile game
        self.diameter = 5
        self.side_length = 3
        self.max_factor = self.side_length - 1

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
                    tile = Tile(resource, hexlib.Hex(q, r, s), numeral)
                    tiles[q][r][s] = tile
                    tiles_by_numeral[numeral] = tiles_by_numeral.get(numeral, []) + [tile]
        self.tiles = tiles
        self.tiles_by_numeral = tiles_by_numeral

    def get_all_tiles_with_numeral(self, numeral: int):
        if numeral < 2 or numeral > 12 or numeral == 7:
            raise Exception
        return self.tiles_by_numeral[numeral]

    def get_tile_by_hex(self, hex: hexlib.Hex) -> Tile:
        return self.tiles[hex.q][hex.r][hex.s]

    class City:

        def __init__(self, vertex, player):
            self.vertex = vertex
            self.player = player

    class Settlement:

        def __init__(self, vertex, player):
            self.vertex = vertex
            self.player = player

    class Road:

        def __init__(self, border) -> None:
            pass

    class Port:

        def __init__(self, tileA, tileB) -> None:
            pass

    class Bandit:

        def __init__(self) -> None:
            pass
