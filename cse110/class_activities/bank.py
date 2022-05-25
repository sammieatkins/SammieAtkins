# Ask the amount they have in their account.
balance = float(input("How much is in your account? "))

# Do you want to make another purchase.
additional_purchase = "yes"
# Check if difference is negative.
while additional_purchase.lower() == "yes":
    # Ask them how much the charge is.
    charge = float(input("What is the charge amount? "))
    # Calculate the difference.
    difference = balance - charge
    while difference < 0:
        # If so, say card declined.
        print("Card declined.")
        # Ask to try another charge amount.
        charge = float(input("What is the charge amount? "))
    # Repeat the calculation and check.
        difference = balance - charge
    # Update the balance.
    balance -= charge
    # Display remaining balance. 
    print(f"Your remaining balance is ${balance:.2f}.")
    additional_purchase = input("Do you want to make another purchase (yes/no)? ")

