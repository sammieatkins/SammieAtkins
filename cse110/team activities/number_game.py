import random
number = random.randint(1, 20)
print(number)
guess = int(input("What is your guess? "))
again = "yes"
while again.lower() == "yes":
    while number != guess:
        if number < guess:
            print("Lower")
        elif number > guess:
            print("Higher")
        guess = int(input("What is your guess? "))

    print("You guessed it!!")
    
    again = input("Do you want to play again (yes/no)? ")

   
