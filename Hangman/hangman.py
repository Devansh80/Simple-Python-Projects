import random

# List of words to choose from
word_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"]

# Select a random word from the list
word = random.choice(word_list)

# Set up the game board
board = ["_"] * len(word)

# Set up the game loop
max_guesses = 6
num_guesses = 0
guessed_letters = []

# Function to print the game board
def print_board():
    print(" ".join(board))

# Function to handle a guess from the user
def make_guess():
    global num_guesses
    global guessed_letters
    
    guess = input("Guess a letter: ").lower()
    
    # Check if the letter has already been guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        return
    
    guessed_letters.append(guess)
    
    # Check if the letter is in the word
    if guess in word:
        print("Correct!")
        for i in range(len(word)):
            if word[i] == guess:
                board[i] = guess
    else:
        print("Incorrect.")
        num_guesses += 1

# Main game loop
while "_" in board and num_guesses < max_guesses:
    print_board()
    print(f"Guesses left: {max_guesses - num_guesses}")
    print(f"Guessed letters: {' '.join(guessed_letters)}")
    make_guess()

# Check if the game is won or lost
if "_" not in board:
    print_board()
    print("Congratulations, you won!")
else:
    print("Sorry, you lost.")
    print(f"The word was {word}.")

