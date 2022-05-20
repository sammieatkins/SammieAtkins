from types import new_class


items = []
item = ""

print()
print("Please enter the items of the shopping list (type: quit to finish):")
while item != "quit":
    item = input("Item: ")
    if item != "quit":
        items.append(item)

print()
print("The shopping list is: ")
for item in items:
    print(item.title())

print()
print("The shopping list with indexes is:")
for i in range(len(items)):
    item = items[i]
    print(f"{i}. {item.title()}")
print()

replaced_item = int(input("Which item would you like to change? "))
new_item = input("What is the new item? ")
items[replaced_item] = new_item
print()

print("The shopping list with indexes is:")
for i in range(len(items)):
    item = items[i]
    print(f"{i}. {item.title()}")

print()