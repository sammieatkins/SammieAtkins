word = "commitment"
favorite_letter = input("What is your favorite letter? ")
# favorite_letter = "m"
for letter in word:
    if letter == favorite_letter:
        print(favorite_letter.upper())
    else:
        print(letter)
    # for letter in favorite_letter:
    #         print(letter, end="")