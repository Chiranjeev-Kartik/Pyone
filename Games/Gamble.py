import random


def play_gambling_game():
    # Set up the game
    balance = 1000
    bet = 0
    min_bet = 100
    max_bet = 1000

    # Game loop
    while balance > 0:
        print("Your current balance is", balance)
        # Get the player's bet
        bet = int(input("Enter your bet (min: %d, max: %d): " % (min_bet, max_bet)))
        if bet < min_bet or bet > max_bet:
            print("Invalid bet. Try again.")
            continue

        # Spin the wheel
        winnings = random.randint(-bet, bet)

        # Update the balance
        balance += winnings
        if balance < 0:
            balance = 0

        # Print the result
        if winnings > 0:
            print("You won\n", winnings, "credits!")
        elif winnings == 0:
            print("It's a tie!")
        else:
            print("You lost\n", -winnings, "credits!")
    print('You lost all of your money.')

# Start the game
play_gambling_game()
