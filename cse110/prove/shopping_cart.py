choice = 0
groceries = []
groceries_price = []
item = ""
item_price = -1
total = 0
user_remove = None

while choice != "5":
    # Menu.
    print("Menu:")
    print("1. Add a new item")
    print("2. Display cart contents")
    print("3. Remove an item")
    print("4. Compute total")
    print("5. Quit")
    print("Please ONLY type the number of the menu item.")

    choice = input("Please enter an action: ")  
    print() 
    # CHOICE 1: Add a new item.
    if choice == "1":
        item = input("What item would you like to add? ")
        groceries.append(item)
        item_price = float(input(f"What is the price of '{item}'? "))
        groceries_price.append(item_price)
        # groceries_price.append(item_price)
        print(f"'{item.title()}' has been added to the cart. ")
        print()

    # CHOICE 2: Display cart contents.
    elif choice == "2":
        print("The contents of your shopping cart are:")
        #  print(f"{name.title()} - ${balance:.2f}")
        for i in range(len(groceries)):
            item = groceries[i]
            price = groceries_price[i]
            print(f"{i + 1}. {item.title()} - ${price:.2f}")
        print()

# FIX AHHH: Needs to have catch for if they enter a number bigger than the list. 
    # CHOICE 3: Remove an item.
    elif choice == "3":
        while user_remove != -1:
            print("Which item would you like to remove?")
            print()
            print("The contents of your shopping cart are:")
            for i in range(len(groceries)):
                item = groceries[i]
                price = groceries_price[i]
                print(f"{i + 1}. {item.title()} - ${price:.2f}")
            print()           

            user_remove = int(input("Enter item number here: (-1 to return to menu) "))      
            # can put -1 at end of input statement instead of:
            index_remove = user_remove - 1

            if user_remove > len(groceries):
                print("Sorry, that is not a valid item number. ")
            elif user_remove < -1:
                print("Sorry, that is not a valid item number. ")  
            elif user_remove == -1:
                break
            else:
                confirm_remove = input(f"Are you sure you want to remove {user_remove} from your shopping list (y/n)? ")
                if confirm_remove.lower() == "y":
                    removed_item = groceries.pop(index_remove)
                    groceries_price.pop(index_remove)
                    print(f"{removed_item.title()} has been removed.")
                    break
                else:
                    print()
        print()

    # CHOICE 4: Compute total. 
    elif choice == "4":
        for price in groceries_price:
            if price > 0:
                total += price
        print(f"Total: ${total:.2f}.")
        print()
    
    # ELSE: Error message.
    elif choice != "5":
        print(f"'{choice}' is not a menu opiton. Please try again.") 
        print()

# Ending statement.
print("Thank you. Goodbye.")
print()


