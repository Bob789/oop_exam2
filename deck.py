import random
from typing import List
from card import Card
from card_rank import CardRank
from card_suit import CardSuit
from errors import DeckCheatingError
from abstract_deck_card import AbstractDeck


def fair_deck(func):
    """
    Decorator to check for duplicate cards returned by the decorated function
    :param func: The function to be decorated (e.g., a method that deals cards)
    :return: The result of the original function if no duplicates are found
             raises DeckCheatingError otherwise
    """

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, list):
            if len(result) != len(set(result)):
                raise DeckCheatingError("Duplicate cards detected")
        return result

    return wrapper


class Deck(AbstractDeck):
    def __init__(self, shuffle=True):
        """Initialize Cards"""
        self._cards: List[Card] = [Card(rank, suit) for suit in CardSuit for rank in CardRank]
        if shuffle:
            self.shuffle()

    @property
    def cards(self) -> List[Card]:
        return self._cards

    def draw(self, card: Card):
        """Removes the given card from the deck if it exists"""
        if card in self._cards:
            self._cards.remove(card)
            return card
        else:
            raise ValueError(f"Card {card} not found in deck")

    def shuffle(self):
        random.shuffle(self._cards)

    def add_card(self, card: Card):
        if not card in self._cards:
            self._cards.append(card)
            return card
        else:
            raise ValueError(f"Card {card} is already in the deck")

    @fair_deck
    def deal(self):
        """Splits the deck into two hands of equal size and returns them"""
        mid = len(self._cards) // 2
        return self._cards[:mid], self._cards[mid:]

    def __len__(self):
        return len(self._cards)

    def __str__(self):
        if len(self._cards) <= 10:
            return ", ".join(str(card) for card in self._cards)
        else:
            lines = []
            row_len = len(self._cards) // 4
            for i in range(0, len(self._cards), row_len):
                line = ", ".join(str(card) for card in self._cards[i:i + row_len])
                lines.append(line)
            return "\n".join(lines)

    def __repr__(self):
        return "\n".join(str(card) for card in self._cards)

    def __max__(self):
        return max(self._cards)

    def __min__(self):
        return min(self._cards)

    def __getitem__(self, index):
        return self._cards[index]

    def __iter__(self):
        self._current = 0
        return self

    def __next__(self):
        if self._current >= len(self._cards):
            raise StopIteration
        card = self._cards[self._current]
        self._current += 1
        return card
