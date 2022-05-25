# Pre-defined variables
order = []
choice = -1

while choice != 4:
    print("Menu:")
    print("1 - Drink")
    print("2 - Sandwich")
    print("3 - Dessert")
    print("4 - Quit")

    choice = int(input("Please select an item from the menu: "))

    if choice == 1:
        drink = input("What type of drink would you like? ")
        size = input("What size? ")
        drink_order = f"{size.capitalize()} {drink.title()}"
        order.append(drink_order)
    elif choice == 2:
        order.append("Sandwich")
    elif choice == 3:
        order.append("Dessert")

print("The contents of your order are: ")
for item in order:
    print(item)

# Option to use multi-line strings:
# print("""
# 1- Drink
# 2 - Sandwich
# 3 - Dessert
# 4 - Quit
# """)

# append is one 
# order.append("Dr. Pepper Cream Soda")
# order.append("BLT")

# .append is not only option. also .remove could be used for prove assignment this week. 