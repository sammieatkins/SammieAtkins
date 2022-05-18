friends = []
friend = ""
while friend != "end":
    friend = input("Type the name of a friend: ")
    if friend != "end":
        friends.append(friend)

print()
print("Your friends are:")

for name in friends:
    print(name.capitalize())
    