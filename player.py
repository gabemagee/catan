import os
from enum import Enum
import hexlib
import random


class Player:

    def __init__(self, color, ai=False) -> None:
        self.resource_cards = []
        self.developmentCards = []
        self.color = color
        self.settlements = []
        self.cities = []
        self.victory_points = 0
        self.ai = ai  # boolean
        # might be better to do class inheritance

    def getAllPossibleActions(self):
        pass

    # returns boolean

    def revealKnightsChoice(self):
        pass

    def buyDevelopmentChoice(self):
        pass

    def receiveTradeChoice(self, resource_a, number_a, resource_b, number_b):
        pass

    def revealDevelopmentChoice(self):
        pass

    def buildCityChoice(self):
        pass

    def bBuildSettlementChoice(self, ):
        pass

    def buildRoadChoice(self):
        pass

    # returns location

    def whereToPlaceBandit(self):
        pass

    def whereToBuildCity(self):
        pass

    def whereToBuildSettlement(self, ):
        pass

    def whereToBuildRoad(self):
        pass

    # complicated choices

    def fourForOneTradeChoice(self, resourceA):
        pass  # return resource that you want

    def portTradeChoice(self, port):
        pass  # return resource you want

    def whichDevToRevealChoice(self):
        pass  # return dev card

    def whichPlayerToTrade(self):
        pass  # return player

    # actions

    def discard_choice(self, number_of_cards_to_discard):
        pass

    def proposePlayerTrade(self, otherPlayer, tradeA, tradeB):
        otherPlayer.receiveTrade(tradeA, tradeB)

        # helper

    def add_victory_points(self):
        self.victory_points = self.victory_points + 1


class AI_player(Player):
    pass


class Human_Player(Player):
    pass
