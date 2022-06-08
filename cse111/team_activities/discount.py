from datetime import datetime

new_total = 0
sales_tax = 0

current_date_and_time = datetime.now()
day_of_week = current_date_and_time.weekday()
# print(day_of_week)

subtotal = float(input("Please enter the subtotal: "))

# check day of week
    # could put both if statements in the same line, but put () around or statements
if day_of_week == 1 or day_of_week == 2:
    if subtotal >= 50:
        #calculate
        discount = subtotal * .1
        new_total = subtotal - discount
        sales_tax = new_total * .06
        total = new_total + sales_tax
        # update subtotal -=
        # display
        print(f"Discount amount: {discount:.2f}")
        print(f"Sales tax: {sales_tax:.2f}")
        print(f"Total: {total:.2f}")

else:
    sales_tax = subtotal * .06
    print(f"Sales tax: {sales_tax:.2f}")
    total = subtotal + sales_tax
