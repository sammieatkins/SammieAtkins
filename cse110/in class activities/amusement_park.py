# can_ride = False

# age1 = int(input("What is the age of the first rider? "))
# height1 = int(input("What is the height of the first rider? "))

# if age1 >= 12 and age1 < 18:
#     golden1 = input("Does this rider have a golden passport (yes/no)? ")
#     golden1 = golden1.lower()

# is_second_rider = input("Is there a second rider? (yes/no)? ")
# is_second_rider = is_second_rider.lower()

# if is_second_rider == "yes":
#     age2 = int(input("What is the age of the second rider? "))
#     height2 = int(input("What is the height of the second rider? "))
    
#     if age2 >= 12 and age2 < 18:
#         golden2 = input("Does this rider have a golden passport (yes/no)? ")
#         golden2 = golden2.lower()

#     if height1 < 36 or height2 <36:
#         can_ride = False
#     else:
#         if age1 >= 18 or age2 >= 18:
#             can_ride = True

# # Stretch 1
#     if age1 < 18 and age2 < 18:
#         if age1 >= 12 and age2 >= 12:
#             if height1 >= 52 and height2 >= 52:
#                 can_ride = True

# else:
#     if age1 >= 18 and height1 >= 62:
#         can_ride = True
#     else:
#         can_ride = False

# if can_ride:
#     print("Welcome to the ride. Please be safe and have fun!")
# else:
#     print("Sorry, you may not ride.")   

# # Stretch 2
# if age1 == 12-17 or age2 == 12-17:
#     golden_passport = input("Do you have a golden passport (yes/no)? ")
#     golden_passport = golden_passport.lower()
#     if golden_passport == "yes":
#         can_ride = True
#     else:
#         can_ride = False






can_ride = False

# Rider 1 Inputs.
age1 = int(input("What is the age of the first rider? "))
height1 = int(input("What is the height of the first rider? "))

# Rider 2?
is_second_rider = input("Is there a second rider? (yes/no)? ")
is_second_rider = is_second_rider.lower()

# Rider 2 Inputs and Rules.
if is_second_rider == "yes":
     age2 = int(input("What is the age of the second rider? "))
     height2 = int(input("What is the height of the second rider? "))
     
     # Rule 1
     if height1 or height2 < 36:
         can_ride = False
     elif age1 >= 12 and age2 >= 12:
         if height1 >= 52 and height2 >= 52:
             can_ride = True
         else:
             can_ride = False
     else:
         if age1 >= 18 or age2 >= 18:
             can_ride = True
         else:
            can_ride = False

# Rider 1 Rules.
else:
    if height1 >= 62 and age1 >= 18:
        can_ride = True
    else:
        can_ride = False
    

# Ending Print Statement. 
if can_ride:
    print("Welcome to the ride. Please be safe and have fun!!")
else:
    print("Sorry, you may not ride.")