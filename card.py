from card_rank import CardRank
from card_suit import CardSuit
from abstract_deck_card import AbstractCard


class Card(AbstractCard):
    def __init__(self, rank: CardRank, suit: CardSuit):
        self._suit = suit
        self._rank = rank

    @property
    def suit(self) -> CardSuit:
        return self._suit

    @property
    def rank(self) -> CardSuit:
        return self._rank

    @suit.setter
    def suit(self, suit):
        self._suit = suit

    @rank.setter
    def rank(self, rank):
        self._rank = rank

    def get_display_name(self) -> str:
        return f"{self._rank.name.title()} of {self._suit.name.title()}"

    def __str__(self):
        return f"{self._rank.name.title()} of {self._suit.name.title()}"

    def __repr__(self):
        return f"Card({self._rank.name}, {self._suit.name})"

    def __eq__(self, other):
        return self._rank == other._rank and self._suit == other._suit

    def __hash__(self):
        return hash((self._rank, self._suit))

    def __lt__(self, other):
        if self._rank.value != other._rank.value:
            return self._rank.value < other._rank.value
        return self._suit.value < other._suit.value

    def __gt__(self, other):
        if self._rank.value != other._rank.value:
            return self._rank.value > other._rank.value
        return self._suit.value > other._suit.value
