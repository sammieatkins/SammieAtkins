# Information prompts.
child_price = float(input("What is the price of the child meal? "))
adult_price = float(input("What is the price of the adult meal? "))
child_num = int(input("How many child meals? "))
adult_num = int(input("How many adult meals? "))
sales_tax_rate = float(input("What is the sales tax rate? "))

# Subtotal.
subtotal = child_price * child_num + adult_price * adult_num
print(f"Subtotal: {subtotal:.2f}.")

# Calculations. 
sales_tax = sales_tax_rate / 100 * subtotal
print(f"Sales tax: {sales_tax:.2f}")

total_price = sales_tax + subtotal
print(f"Your total is {total_price:.2f}.")

# Add creativity. (Tip)
tip_percentage = float(input("Please enter tip percentage: "))
if tip_percentage >= 20:
    print("Thank you!! :) ")
elif tip_percentage == 0:
    print("How rude :( ")
else:
    print("Thank you :)")
tip = tip_percentage / 100 * subtotal

# Total with tip.
total_tip = total_price + tip
print(f"Your total is now {total_tip:.2f}")

# Payment & Change.
payment = float(input("What is the payment amount? "))
change = payment - total_tip
print(f"Your change is {change:.2f}.")
if tip_percentage >= 1:
    print("Thanks for dining with us :)")
elif tip_percentage ==0:
    print("Goodbye.")