from deck import Deck
from card_suit import CardSuit
from card_rank import CardRank
from card import Card
from game import Game

# Initialize the deck outside main for access in functions
deck = Deck()


def one():
    """Starts an automatic card war game between 2 players"""
    print("You selected 1. Automatic card war game between 2 players")
    g1 = Game
    game = Game("Eli", "Avi")
    game.play()
    print()


def two():
    """Shuffles the deck"""
    print("You selected 2. Shuffle")
    deck.shuffle()
    print("Deck shuffled.")


def three():
    """
    Prompts the user to draw a specific card from the deck
    :return: Nane
    """
    print("You selected 3. Draw card")
    print("Please type the card you want to draw (e.g., ACE HEARTS):")
    card_to_remove = input("-> ").strip().upper()
    parts = card_to_remove.split()
    if len(parts) != 2:
        print("Invalid input. Please type: rank suit (e.g., ACE HEARTS)")
        return
    rank_str, suit_str = parts

    try:
        rank = CardRank[rank_str]
        suit = CardSuit[suit_str]
        card = Card(rank, suit)
        card_to_remove = deck.draw(card)
        print(f"Drawn card: {card_to_remove}")
    except KeyError:
        print("Invalid rank or suit name.")
    except ValueError as e:
        print(e)


def four():
    """Adds a card to the deck"""
    print("You selected 4. Add card")

    print("Please type the card you want to add to deck (e.g., ACE HEARTS):")
    card_to_add = input("-> ").strip().upper()
    parts = card_to_add.split()
    if len(parts) != 2:
        print("Invalid input. Please type: rank suit (e.g., ACE HEARTS)")
        return
    rank_str, suit_str = parts
    try:
        rank = CardRank[rank_str]
        suit = CardSuit[suit_str]
        card = Card(rank, suit)
        card_to_add = deck.add_card(card)
        print(f"Adding card: {card_to_add}")
    except KeyError:
        print("Invalid rank or suit name.")
    except ValueError as e:
        print(e)


def five():
    """Prints the number of cards remaining in the deck"""
    print("You selected 5. Length of deck")
    print(f"Deck contains {len(deck.cards)} cards.")


def six():
    """Displays the current state of the deck"""
    print("You selected 6. Display deck")
    print(deck)


def seven():
    """Handles exit"""
    print("You selected 7. Exit")
    print(" Bye")


def eight():
    """Print Min, Max cards according (suit)"""
    print()
    print("You selected 8. Min ,Max")
    print(f"Lowest card: {min(deck)}")
    print(f"Highest card: {max(deck)}")
    print()


def nine():
    """For use future"""
    print("You selected 9")


def default():
    """Handles invalid menu selections"""
    print("You selected a value out of range")


def show_menu():
    """Displays the main menu."""
    print()
    print("-" + "Select number from menu".center(25) + "-")
    print("|" + "+" * 25 + "|")
    print("|" + "Menu".center(25) + "|")
    print("-" * 27)
    print("1. Automatic card war game between 2 players")
    print("-" * 27)
    print("2. Shuffle")
    print("-" * 27)
    print("3. Draw card")
    print("-" * 27)
    print("4. Add card")
    print("-" * 27)
    print("5. Len Deck")
    print("-" * 27)
    print("6. Display Deck")
    print("-" * 27)
    print("7. Exit")
    print("-" * 27)
    print("8. Min ,Max")
    print("|" + "+" * 25 + "|")
    print()


# Menu action map
menu_actions = {
    '1': one,
    '2': two,
    '3': three,
    '4': four,
    '5': five,
    '6': six,
    '7': seven,
    '8': eight,
    '9': nine
}


def main():
    """
    Main function that displays the menu and handles user interactions
    :return: Nane
    """
    running = True
    while running:
        show_menu()
        choice = input("Please enter your choice from the menu: ").strip()
        if choice == '7':
            seven()
            running = False
        else:
            menu_actions.get(choice, default)()


# start the program
if __name__ == "__main__":
    main()
