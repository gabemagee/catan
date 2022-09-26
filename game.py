import math
import random
from enum import Enum
from typing import List

from board import Board
from board import Tile
from player import Player


class Game:

    def __init__(self, players: List[Player]) -> None:
        self.players = players
        self.firstPlayerIndex = players.index(self.determine_first_player(players))
        self.board = Board()
        self.desert = None  # TODO
        self.bandit = Game.Bandit(self.desert)
        print(self.turnCycle())

    def turnCycle(self):
        turn = self.takeTurn(self.players[self.firstPlayerIndex])
        nextPlayerIndex = (self.firstPlayerIndex + 1) % len(self.players)
        # while turn:
        #     turn = ! Game.takeTurn(self, self.players[nextPlayerIndex])
        #     nextPlayerIndex = (nextPlayerIndex + 1) % len(self.players)
        return (nextPlayerIndex - 1) % len(self.players)

    def rollDice(self, num_dice=2, faces=6):
        # Non-deterministic
        sum = 0
        for i in range(0, num_dice):
            sum += random.randint(1, faces)
        return sum

    def determine_first_player(self, players):
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
        return Game.determine_first_player(self, leader)

    def take_turn(self, active_player: Player):
        # reveal knights
        if active_player.revealKnightsChoice():
            self.banditAttack(active_player, False)
        # roll dice
        val = self.rollDice()
        if val == 7:
            self.banditDiscard()
            self.banditAttack(active_player)
        else:
            self.board.distribute_resources_from_die_roll(numeral=val)
        # trading step
        active_player.trade_step()
        # building and buying step
        active_player.build_or_buy_step()
        return self.isWon()  # return True if game was won?

    def banditDiscard(self):
        for player in self.players:
            if player.total_number_of_resources > 7:
                player.discard_choice(math.ceil(player.total_number_of_resources / 2))

    def placeBandit(self, activePlayer, tile: Tile):
        players = list(
            set([city.player for city in tile.cities] + [settlement.player for settlement in tile.settlements])
        )
        # have active player decide on which player to pick resource from
        pass

    def banditAttack(self, active_player: Player, rolled=True):
        tile = active_player.banditTileChoice()
        self.placeBandit(active_player, tile)
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

    class DevelopmentType(Enum):
        pass


def main():
    players = []
    for color in ["a", "b", "c", "d"]:
        players.append(Player(color))
    G = Game(players)


main()
