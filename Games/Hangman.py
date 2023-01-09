import random


def draw_hangman(lives):
    """
    Draws the hangman drawing based on the number of lives remaining.
    """
    if lives == 6:
        print("""
       _____
      |     |
      |
      |
      |
      |
    __|__
        """)
    elif lives == 5:
        print("""
       _____
      |     |
      |     O
      |
      |
      |
    __|__
        """)
    elif lives == 4:
        print("""
       _____
      |     |
      |     O
      |     |
      |
      |
    __|__
        """)
    elif lives == 3:
        print("""
       _____
      |     |
      |     O
      |    /|
      |
      |
    __|__
        """)
    elif lives == 2:
        print("""
       _____
      |     |
      |     O
      |    /|\\
      |
      |
    __|__
        """)
    elif lives == 1:
        print("""
       _____
      |     |
      |     O
      |    /|\\
      |    /
      |
    __|__
        """)
    elif lives == 0:
        print("""
       _____
      |     |
      |     O
      |    /|\\
      |    / \\
      |
    __|__
        """)


def play_hangman():
    # Set up the game
    word_list = ['mango', 'apple', 'banana', 'apricot', 'pineapple']
    word = random.choice(word_list)
    word_letters = set(word)
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    used_letters = set()
    lives = 6

    # Game loop
    while len(word_letters) > 0 and lives > 0:
        # Print the current state of the game
        draw_hangman(lives)
        print("You have", lives, "lives left")
        print("Used letters:", " ".join(used_letters))
        print("Word:", " ".join(letter if letter in used_letters else "_" for letter in word))

        # Get the player's next guess
        guess = input("Enter a letter: ").lower()

        if guess in alphabet - used_letters:
            used_letters.add(guess)

            if guess in word_letters:
                word_letters.remove(guess)
            else:
                lives -= 1
        elif guess in used_letters:
            print("You have already used that letter. Choose another.")
        else:
            print("Invalid input. Enter a letter a-z.")

    # The game is over
    if lives == 0:
        print("You lost! The word was", word)
    else:
        print("Congratulations! You won! The word was", word)


# Start the game
play_hangman()
