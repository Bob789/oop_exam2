import random


class Player:
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def draw_random_card(self):
        """Draws and removes a random card from hand"""
        if not self.hand:
            return None
        index = random.randint(0, len(self.hand) - 1)
        return self.hand.pop(index)
