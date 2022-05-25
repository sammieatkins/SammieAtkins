print("Enter a list of numbers, type 0 when finished.")
user_number = 1
# empty list
numbers = []
sum = 0 
avg = 0
largest_number = 0
while user_number != 0:
    user_number = int(input("Enter number: "))
    if user_number != 0:
        numbers.append(user_number)
print(numbers)
for number in numbers:
    sum += number
    avg = sum / len(numbers)
for number in numbers:
    if number > largest_number:
        largest_number = number
print(f"The sum is {sum}")
print(f"The average is {avg}")
print(f"The largest number is {largest_number}")
