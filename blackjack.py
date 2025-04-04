import random
import time

class Casino:
    def __init__(self):
        # Creating a deck with 4 sets of cards
        self.deck = ['A',2,3,4,5,6,7,8,9,10,'J','K','Q'] * 4
        self.playerHand = []  # Player's hand
        self.dealerHand = []  # Dealer's hand
        self.playerIn = True  # Flag to track if player is still playing
        self.dealerIn = True  # Flag to track if dealer is still playing

        # Welcome message and game start countdown
        print("---------------------------------------------------------WELCOME TO BLACKJACK-------------------------------------------------------------")
        print('\nBe ready while the dealer is shuffling the cards.')
        time.sleep(1)
        print('The game starts in: ')
        time.sleep(1)
        for sec in [3,2,1]:
            print(sec, end=' ', flush=True)
            time.sleep(0.5)

    def InputHandling(self, options_list):
        """Handles user input to ensure valid choices"""
        while True:
            try:
                Input = int(input(": "))
                if Input not in options_list:
                    print("Invalid input! Please try again.")
                else:
                    break
            except ValueError:
                print(f'Please enter only {options_list} as per the choices')

        return Input

    def carddist(self, turn):
        """Distributes a random card to the given hand (turn)"""
        card = random.choice(self.deck)
        turn.append(card)
        self.deck.remove(card)

    def totalscore(self, turn):
        """Calculates the total score of a hand, handling Ace values"""
        total = 0
        aces = 0  # Track number of Aces

        for card in turn:
            if isinstance(card, int):  # Numbered cards
                total += card
            elif card in ['J', 'K', 'Q']:  # Face cards are worth 10 points
                total += 10
            else:  # Ace
                total += 11
                aces += 1

        # Adjust Ace value if total exceeds 21
        while total > 21 and aces > 0:
            total -= 10
            aces -= 1

        return total
    
    def show_cards(self, turn):
        """Displays cards with a delay for a realistic effect"""
        for card in turn:
            time.sleep(0.4)
            print(card, end=' ', flush=True)
            time.sleep(0.4)

    def playing(self):
        """Handles the gameplay, including player and dealer turns"""
        # Initial card distribution (2 cards each)
        for _ in range(2):
            self.carddist(self.playerHand)
            self.carddist(self.dealerHand)

        # Show dealer's first card and hide the second
        print("\nDealer's cards: ", end='')
        time.sleep(0.4)
        print(self.dealerHand[0], end=' ', flush=True)
        print("and", end=' ', flush=True)
        time.sleep(0.4)
        print('X', flush=True)
        time.sleep(0.4)
        
        # Player's turn
        while self.playerIn:
            print("Your cards: ", end='')
            self.show_cards(self.playerHand)
            print(f"total = {self.totalscore(self.playerHand)}")
            
            print('Enter 1 - Hit (Take one more card) or 2 - Stay (Stop taking cards)', end='')
            stayORhit = self.InputHandling([1, 2])

            if stayORhit == 1:
                self.carddist(self.playerHand)
            else:
                self.playerIn = False

            # Check if player goes over 21 (Bust)
            if self.totalscore(self.playerHand) > 21:
                print("\nYou have", end=' ')
                self.show_cards(self.playerHand)
                print(f"for a total of {self.totalscore(self.playerHand)}")
                print("Dealer has", end=' ')
                self.show_cards(self.dealerHand)
                print(f"for a total of {self.totalscore(self.dealerHand)}")
                print(f"It's a Bust! Dealer wins!!\n")
                return
            
            # Check if player got a Blackjack
            elif self.totalscore(self.playerHand) == 21 and self.totalscore(self.dealerHand) != 21:
                print("\nYou have", end=' ')
                self.show_cards(self.playerHand)
                print(f"for a total of {self.totalscore(self.playerHand)}")
                print("Dealer has", end=' ')
                self.show_cards(self.dealerHand)
                print(f"for a total of {self.totalscore(self.dealerHand)}")
                print('Blackjack! You win!!\n')
                return

        # Dealer's turn (must draw until total is 16 or higher)
        while self.totalscore(self.dealerHand) <= 16:
            self.carddist(self.dealerHand)

        # Show final results
        print("\nYou have", end=' ')
        self.show_cards(self.playerHand)
        print(f"for a total of {self.totalscore(self.playerHand)}")
        print("Dealer has", end=' ')
        self.show_cards(self.dealerHand)
        print(f"for a total of {self.totalscore(self.dealerHand)}")

        # Determine the winner
        if self.totalscore(self.dealerHand) > 21:
            print(f"It's a Bust! You win!!\n")
        elif self.totalscore(self.dealerHand) == 21:
            print('Blackjack! Dealer wins!!\n')
        elif 21 - self.totalscore(self.playerHand) < 21 - self.totalscore(self.dealerHand):
            print("\nYou are closer to 21! You win!!\n")
        elif 21 - self.totalscore(self.playerHand) > 21 - self.totalscore(self.dealerHand):
            print(f"\nDealer is closer! Dealer wins\n")
        else:
            print("It's a draw!!")

# Main game loop
while True:
    c = Casino()
    c.playing()
    print('Enter 1 to play again or 2 to stop', end='')
    play_again = c.InputHandling([1, 2])
    if play_again == 2:
        print('Thanks for Playing! Have a great day!!\n')
        break
