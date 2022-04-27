# Ask for the number of passengers
riders = int(input("How many riders in your party? "))

# Ask for how many can fit in the ride
capacity = int(input("How many can fit in the car? "))

# Calculate the number of cars we will have
cars = riders / capacity

# Display the result
# print(f"The capacity of the ride is: {capacity}")
print(f"You will need {cars} cars. ")

full_cars = riders // capacity
print(f"There are {full_cars} full cars.")

left_over_riders = riders % capacity
print(f"There are {left_over_riders} riders left over.")

print(f"You will have {full_cars} full cars with {left_over_riders} people left over.")