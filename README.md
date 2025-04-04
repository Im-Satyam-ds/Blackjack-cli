# Blackjack - CLI Casino Game
A simple command-line Blackjack game built with Python. Play against the dealer, make strategic
decisions, and try to get as close to 21 as possible without going over!
## How to Play
- Blackjack Rules:
 - Each player is dealt two cards at the start.
 - The goal is to get as close to 21 as possible without exceeding it (Bust).
 - Numbered cards have their face value, J, Q, and K are worth 10, and Ace is worth 11 (or 1 if
needed).
 - The dealer must draw cards until their total is at least 17.
 - The player can choose to Hit (draw a card) or Stay (keep their hand as is).
 - A natural Blackjack (21 with two cards) wins instantly unless the dealer also has one.
 - The closest to 21 wins!
## Installation & Running the Game
1. Clone the repository:
 git clone https://github.com/your-username/blackjack-cli.git
2. Navigate to the folder:
 cd blackjack-cli
3. Run the script:
 python blackjack.py
## Gameplay Preview
---------------------------------------------------------WELCOME TO
Blackjack - CLI Casino Game
BLACKJACK-------------------------------------------------------------
Be ready while the dealer is shuffling the cards.
The game starts in:
3 2 1
Dealer's cards: 9 and X
Your cards: 5 7
Total = 12
Enter 1 - Hit (Take one more card) or 2 - Stay (Stop taking cards):
## Features
- Realistic game flow with a countdown
- Handles Aces dynamically (11 or 1 depending on hand value)
- Includes dealer logic (Dealer must hit until reaching at least 17)
- Clear win/loss conditions
- Simple & fun gameplay!
## Requirements
- Python 3.x
- No external libraries required
## Future Improvements
- Implement a betting system
- Add multiplayer mode
- GUI version using Tkinter
## License
Blackjack - CLI Casino Game
This project is open-source and free to use!
Made with ❤️ by Satyam
