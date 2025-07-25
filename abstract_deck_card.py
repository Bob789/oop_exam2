from abc import ABC, abstractmethod


class AbstractDeck(ABC):
    @abstractmethod
    def shuffle(self):
        pass

    @abstractmethod
    def draw(self):
        pass


class AbstractCard(ABC):
    @abstractmethod
    def get_display_name(self):
        pass
