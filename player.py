from board import ResourceType


class Player:

    def __init__(self, color, game) -> None:
        self.game = game
        self.resources = {resource: 0 for resource in ResourceType}
        self.color = color
        self.settlements = []
        self.cities = []
        self.developmentCards = []
        self.victory_points = 0
        # might be better to do class inheritance

    @property
    def total_number_of_resources(self) -> int:
        count = 0
        for resource_type in self.resources:
            count = count + self.resources[resource_type]
        return count

    def build_or_buy_step(self):
        pass

    def trade_step(self):
        pass

    def getAllPossibleActions(self):
        pass

    def build_settlement(self, tile_one, tile_two, tile_three):
        self.game.board

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

    def banditTileChoice(self):
        pass

    # actions

    def discard_choice(self, number_of_cards_to_discard):
        pass

    def proposePlayerTrade(self, otherPlayer, tradeA, tradeB):
        otherPlayer.receiveTrade(tradeA, tradeB)

        # helper

    def add_victory_points(self):
        self.victory_points = self.victory_points + 1


class AIPlayer(Player):
    pass


class HumanPlayer(Player):
    pass


class RandomPlayer(Player):
    pass
