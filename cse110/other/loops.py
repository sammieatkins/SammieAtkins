# Section 1.
# Ask for positive number.
number = float(input("Please type a positive number: "))
# Loop if they enter a negative number.
while number <0:
    print("Sorry, that is a negative number. Please try again.")
    number = float(input("Please type a positive number: "))
# Print when they enter a positive number.
print(f"The number is: {number}")

# Section 2.
# Ask for candy.
candy = input("May I have a piece of candy? ")
# Repeat until they say yes.
if candy.lower() == "yes":
    print("Thank you.")
else:
    while candy.lower() == "no":
        candy = input("May I have a piece of candy? ")
