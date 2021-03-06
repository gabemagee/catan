import math
import os
from enum import Enum
from typing import List
import hexlib
import random
from board import Board
from player import Player

BOARD_WIDTH = 5
MAX_NUM_PLAYERS = 4
    
class Game():

    def __init__(self, players : List[Player]) -> None:
        self.players = players 
        self.firstPlayerIndex = players.index(self.determineFirstPlayer(players))
        self.board = Board()
        self.desert = None #TODO
        self.bandit = Game.Bandit(self.desert)
        print(self.turnCycle())

    def turnCycle(self):    
        turn = self.takeTurn(self.players[self.firstPlayerIndex])
        nextPlayerIndex = (self.firstPlayerIndex + 1) % len(self.players)
        # while turn:
        #     turn = ! Game.takeTurn(self, self.players[nextPlayerIndex])
        #     nextPlayerIndex = (nextPlayerIndex + 1) % len(self.players)
        return (nextPlayerIndex - 1) % len(self.players)


    def rollDice(self, num_dice = 2, faces = 6):
        # Non-deterministic
        sum = 0
        for i in range(0,num_dice):
            sum += random.randint(1, faces)
        return sum

    def determineFirstPlayer(self, players):
        # Non-deterministic
        if len(players) == 1:
            return players[0]
        leader = [None]
        highRoll = 1
        for player in players:
            res = self.rollDice()
            if res > highRoll:
                highRoll = res
                leader = [player]
            elif res == highRoll:
                leader = leader + [player]
        return Game.determineFirstPlayer(self, leader)
            
    def takeTurn(self, player : Player):
        #non-deterministic
        #reveal knights
        if player.revealKnightsChoice():
            self.banditAttack(player, False)
        #roll dice
        val = self.rollDice()
        if val == 7:
            self.banditDiscard()
            self.banditAttack(player)
        else:
            for tile in self.board.getAllTilesWithNumeral(val):
                pass #TODO: give player resources
        #build or buy
        return self.isWon()# return True if game was won?

    def banditDiscard(self):
        for player in self.players:
            if len(player.resource_cards) > 7:
                player.discard_choice(math.ceil(len(player.resource_cards) / 2))

    def placeBandit(self, activePlayer, tile):
        pass

    

    def banditAttack(self, activePlayer : Player, rolled=True):
        tile = activePlayer.banditTileChoice()
        self.placeBandit(activePlayer, tile)
        pass

    def isWon(self):
        for player in self.players:
            return player.victory_points > 9
        return True

    class Bandit():

        def __init__(self, location):
            self.location = location

        def move(self, dest):
            self.location = dest

    class DevelopmentCard():

        def __init__(self) -> None:
            pass

    class DevelopmentCardDeck():

        def __init__(self) -> None:
            self.cards = [Game.DevelopmentCard()]

        def shuffle(self):
            random.shuffle(self.cards)

        def draw(self):
            return self.cards.pop()

    class ResourceType(Enum):
        DESERT=0
        CLAY=1
        ORE=2
        SHEEP=3
        WHEAT=4
        WOOD=5

    class DevelopmentType(Enum):
        pass

def main():
    players = []
    for color in ["a","b", "c", "d"]:
        players.append(Player(color))
    G = Game(players)

main()