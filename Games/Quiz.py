import random


def play_quiz():
    # Set up the game
    questions = [
        ("What is the capital of France?", "Paris"),
        ("What is the capital of Italy?", "Rome"),
        ("What is the capital of Spain?", "Madrid"),
        ("What is the capital of Germany?", "Berlin"),
        ("What is the capital of Japan?", "Tokyo")
    ]
    random.shuffle(questions)

    # Game loop
    score = 0
    for question, answer in questions:
        # Present the question to the player
        print(question)
        # Get the player's answer
        player_answer = input("Your answer: ")
        # Check if the player's answer is correct
        if player_answer.lower() == answer.lower():
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is", answer)

    # The quiz is over
    print("Quiz complete! You scored", score, "out of", len(questions))


# Start the game
play_quiz()
