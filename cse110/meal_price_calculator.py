# Information prompts.
child_price = float(input("What is the price of the child meal? "))
adult_price = float(input("What is the price of the adult meal? "))
child_num = int(input("How many child meals? "))
adult_num = int(input("How many adult meals? "))
sales_tax_rate = float(input("What is the sales tax rate? "))

# Calculations.
subtotal = child_price * child_num + adult_price * adult_num
print(f"Subtotal: {subtotal}.")

sales_tax = sales_tax_rate / 100 * subtotal
print(f"Sales tax: {sales_tax}")

total_price = sales_tax + subtotal
print(f"Your total is {total_price}. :)")

# Payment & Change.
payment = float(input("What is the payment amount? "))
change = payment - total_price
print(f"Your change is {change}.")

# Add creativity. 
