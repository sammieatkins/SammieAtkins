# Randomize word for above and beyond
# Define word.
secret = "goose"

# Prompt for guess.
guess = input("What is your guess? ")

# Calculate guesses
number_guesses = 1

# Loop if guess is incorrect.
while guess.lower() != secret:
    print("Incorrect.")
    number_guesses = number_guesses + 1
    guess = input("What is your guess? ")

print("Congratulations, you guessed it!!")

# Display number of guesses.
print(f"You guessed it in {number_guesses} guesses :)")