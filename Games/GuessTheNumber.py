import random

print("Welcome to the number guessing game!")

# Generate a random number between 1 and 100
secret_num = random.randint(1, 100)

while True:
    # Get a guess from the player
    guess = int(input("Enter your guess (1-100): "))

    # If the guess is too high
    if guess > secret_num:
        print("Your guess is too high. Try again.")
    # If the guess is too low
    elif guess < secret_num:
        print("Your guess is too low. Try again.")
    # If the guess is correct
    else:
        print("Congratulations! You guessed the correct number.")
        break
