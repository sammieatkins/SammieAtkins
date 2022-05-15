# Make random words
# Print a welcome message.
print("Welcome to the word guessing game!!")

# Define word.
secret_word = "goose"

# Calculate number of guesses.
number_guesses = 1

# Print the hint. Your hint is:
print("Your hint is: ", end=" ")
for letter in secret_word:
    print("_", end=" ")
print()
print()

# Prompt for guess.
guess = input("What is your guess? ")

while guess.lower() != secret_word:
    print("Your hint is: ", end=" ")
    for i, letter in enumerate(guess):
        if letter == secret_word[i]:
            print(letter.upper(), end=" ")
        elif letter in secret_word:
            print(letter.lower(), end=" ")
        else:
            print("_", end=" ")
        
    number_guesses = number_guesses + 1
    print()
    guess = input("What is your guess? ")
    

# Print congratulations message
print("Congratulations, you guessed it!!")

# Display number of guesses.
print(f"It took you {number_guesses} guesses :)")