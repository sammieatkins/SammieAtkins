def calculate_tip(total, tip_percent):
    # returns tip amount
    tip_amount = total * tip_percent / 100
    return tip_amount

def add_tax(subtotal, tax_percent):
    tax_amount = subtotal * tax_percent / 100
    total = subtotal + tax_amount
    return total

# could do a while loop to make them put the number in the right format (not decimal form below 1)
# percent = float(input("What is the tip percent? "))

total_meal = float(input("What is the price of the meal? "))

tax_total = add_tax(total_meal, 6.00)
print(f"The total after tax is: ${tax_total:.2f}")

for percent in range(15, 26, 1):
    tip_amount = calculate_tip(tax_total, percent)
    print(f"At {percent}% tip would be: ${tip_amount:.2f}")
    # print(percent)



# # testing
# tip_amount = calculate_tip(total_meal, percent)
# print(tip_amount)