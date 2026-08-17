import random

def hangman():
    words = ["apple", "python", "house", "banana", "school"]
    word = random.choice(words)
    attempts = 6
    guessed_letters = set()

    print("Welcome to Hangman!")
    print("_ " * len(word))

    while attempts > 0:
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("Already guessed!")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Correct!")
        else:
            attempts -= 1
            print(f"Wrong! Chances left: {attempts}")

        # Show current progress
        display = [letter if letter in guessed_letters else "_" for letter in word]
        print(" ".join(display))

        if "_" not in display:
            print("You win! The word was:", word)
            break

    if attempts == 0:
        print("You lose! The word was:", word)

hangman()
