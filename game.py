from player import Player
from deck import Deck


class Game:
    def __init__(self, name1="Player 1", name2="Player 2"):
        self.deck = Deck()
        hand1, hand2 = self.deck.deal()

        # Each player get name and cards(hand)
        self.player1 = Player(name1, hand1)
        self.player2 = Player(name2, hand2)

    def play(self):
        round_num = 1
        rounds_played = 0
        continue_game = True

        # Play war game 3 turn
        while self.player1.hand and self.player2.hand and continue_game:
            print(f"\n--- Round {round_num} ---")
            pc1 = self.player1.draw_random_card()
            pc2 = self.player2.draw_random_card()
            print(f"{self.player1.name} plays: {pc1}")
            print(f"{self.player2.name} plays: {pc2}")

            # pc1 -> player1 card we compare cards
            if pc1 > pc2:
                print(f"{self.player1.name} wins the round")
                self.player1.hand.extend([pc1, pc2])
            elif pc1 < pc2:
                print(f"{self.player2.name} wins the round")
                self.player2.hand.extend([pc1, pc2])

            round_num += 1
            rounds_played += 1

            if rounds_played == 3:
                if rounds_played == 3:
                    print("|" + "+" * 25 + "|")
                    print(f"{self.player1.name}'s hand:")
                    for card in self.player1.hand:
                        print(card)

                    print("|" + "+" * 25 + "|")
                    print(f"{self.player2.name}'s hand:")
                    for card in self.player2.hand:
                        print(card)

                answer = input("\nDo you want to play 3 more rounds? (yes/no): ").strip().lower()
                if answer != 'yes':
                    continue_game = False
                else:
                    rounds_played = 0  # reset the 3 turn counter

        # Game ended
        print("\nGame Over!")
        print(f"{self.player1.name} has {len(self.player1.hand)} cards")
        print(f"{self.player2.name} has {len(self.player2.hand)} cards")

        if len(self.player1.hand) > len(self.player2.hand):
            print(f"{self.player1.name} wins the game")
        elif len(self.player1.hand) < len(self.player2.hand):
            print(f"{self.player2.name} wins the game")
