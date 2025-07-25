class DeckCheatingError(Exception):
    """Custom exception raised when duplicate cards are detected in the deck"""

    def __init__(self, message="Duplicate cards detected in the deck"):
        super().__init__(message)
