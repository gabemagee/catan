import math
import os
from enum import Enum
import hexlib
import random

class Direction(Enum):
    RIGHT=0
    UPPER_RIGHT=1
    UPPER_LEFT=2
    LEFT=3
    LOWER_LEFT=4
    LOWER_RIGHT=5

class Board():

        def __init__(self, diameter = 5):
            self.diameter = diameter

        def getAllTilesWithNumeral(self, numeral):
            return []

        def getTileByHex(self, hex):
            return None
        
        class Grid():

            def __init__(self, diameter):
                self.diameter = diameter
                self.hexes = {{{}}}
                min = -(round(diameter / 2))
                max = math.ceil(diameter / 2)
                for i in range(min, max):
                    for j in range(min, max):
                        for k in range(min, max):
                            self.hexes[i][j][k] = self.Hex(i,j,k)

            def get_hex(self, x, y, z):
                return self.hexes[x][y][z] 

            class Hex():

                def __init__(self, x, y, z):
                    self.hex = hexlib.Hex(x,y,z)

                def getX(self):
                    return self.hex.q

                def getY(self):
                    return self.hex.r

                def getZ(self):
                    return self.hex.s

                def get_neighbor(self, direction: Direction):
                    assert (direction.value < 6 and direction.value > -1)
                    return hexlib.hex_neighbor(self.hex, direction.value)

                def is_neighbor(self, otherHex):
                    return hexlib.is_neighbor(self.hex, otherHex.hex) != -1

            class Vertex():

                def __init__(self, hex_a, hex_b, hex_c) -> None:
                    self.hexes = [hex_a, hex_b, hex_c]

            class Border():

                def __init__(self, hex_a, hex_b) -> None:
                    self.hexes = [hex_a, hex_b]

        class Tile():

            def __init__(self, resourceType, hex, numeral):
                self.resourceType = resourceType
                self.hex = hex
                self.numeral = numeral

            def getNeighbors(self):
                pass

            def getSettlements(self):
                pass

            def getCities(self):
                pass

        class City():

            def __init__(self, vertex, player):
                self.vertex = vertex
                self.player = player

        class Settlement():

            def __init__(self, vertex, player):
                self.vertex = vertex
                self.player = player

        class Road():

            def __init__(self, border) -> None:
                pass    

        class Port():

            def __init__(self, tileA, tileB) -> None:
                pass 
        
        class Bandit():

            def __init__(self) -> None:
                pass
