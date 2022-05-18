## add while loop eventually
choice = 0
groceries = []
groceries_price = []
item = ""

while choice != 5:
    # Menu.
    print("Menu:")
    print("1. Add a new item")
    print("2. Display cart contents")
    print("3. Remove an item")
    print("4. Compute total")
    print("5. Quit")
    print("Please ONLY type the number of the menu item.")

    choice = int(input("Please enter an action: "))    
    # Add a new item.
    if choice == 1:
        item = input("What item would you like to add? ")
        groceries.append(item)
        # item_price = input(f"What is the price of '{item}'? ")
        # groceries_price.append(item_price)
        print(f"'{item.capitalize()}' has been added to the cart. ")
        print()
    elif choice == 2:
        print("The contents of your shopping cart are:")
        for item in groceries:
            print(item)
print(groceries)
print("Thank you. Goodbye.")

