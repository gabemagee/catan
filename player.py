from board import ResourceType


class Player:

    def __init__(self, color) -> None:
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

    def add_victory_points(self):
        self.victory_points = self.victory_points + 1


class AIPlayer(Player):
    pass


class HumanPlayer(Player):
    pass


class RandomPlayer(Player):
    pass
