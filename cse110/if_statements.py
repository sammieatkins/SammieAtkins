# Numbers.
first_number = float(input("What is the first number? "))
second_number = float(input("What is the second number? "))

if first_number > second_number:
    print("The first number is greater.")
else:
    print("The first number is not greater.")

if first_number == second_number:
    print("The numbers are equal.")
else:
    print("The numbers are not equal.")

if second_number > first_number:
    print("The second number is greater.")
else:
    print("The second number is not greater.")

# Favorite animal. 
user_fav_animal = input("What is your favorite animal? ")

if user_fav_animal.lower() == "turtle":
    print("That's my favorite animal too!")
else:
    print("That is not my favorite animal :(")