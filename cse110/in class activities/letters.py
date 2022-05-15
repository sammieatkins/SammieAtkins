word = "building"

guess = ""
while guess != "?":
    # Right click, "rename symbol" to change variable name
    guess = input("Please type a letter (or ? to quit): ")
    guess = guess.lower()

    # in - is letter in word at all
    if guess in word:
        print(f"The word contains the letter {guess}.")
    else:
        print(f"The letter {guess} is not found in the word.")

    for letter in word:
        if letter.lower() == guess:
            # How to make one line - end=""
            print(letter.upper(), end=" ")
        else:
            print("_", end=" ")
   
print()

# Questions