names = []
balances = []
name = ""
total = 0
highest_balance = 0
highest_name = ""

while name.lower() != "quit":
    name = input("What is the name of this account? ")

    if name != "quit":
        names.append(name)
        balance = float(input("What is the balance of this account? "))
        balances.append(balance)
    print()
    
print("Account Information:")
for i in range(len(names)):
    name = names[i]        
    balance = balances[i]
    print(f"{name.title()} - ${balance:.2f}")
    
    total += balance
    average = total / len(balances)

print(f"Total: ${total:.2f}")
print(f"Average: ${average:.2f}")

largest = 0
for i in range(len(balances)):
    if balance > largest:
        largest = balance
    highest_name = names[i]
    highest_balance = balances[i]
print(f"Highest balance: {highest_name} - ${highest_balance}")





