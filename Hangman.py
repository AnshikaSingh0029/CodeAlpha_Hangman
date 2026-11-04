import random

# List of 5 predefined words
words = ["apple", "mango", "python", "school", "computer"]

# Randomly select a word
word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Maximum incorrect attempts
attempts = 6

print("================================")
print("       WELCOME TO HANGMAN")
print("================================")

# Game loop
while attempts > 0:

    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"

    print("\nWord:", " ".join(display_word))
    print("Remaining attempts:", attempts)

    # Check winning condition
    if "_" not in display_word:
        print("\nCongratulations! You won!")
        break

    # Take input from player
    guess = input("Guess a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter!")
        continue

    # Check repeated guesses
    if guess in guessed_letters:
        print("You already guessed this letter!")
        continue

    guessed_letters.append(guess)

    # Check correct or incorrect guess
    if guess in word:
        print("Correct guess!")
    else:
        attempts -= 1
        print("Wrong guess!")

# Losing condition
if attempts == 0:
    print("\nGame Over!")
    print("The correct word was:", word)

print("\nThanks for playing Hangman!")
