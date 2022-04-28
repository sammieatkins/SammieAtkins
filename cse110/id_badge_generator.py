# Prompt user for information.
first_name = input("What is your first name? ")
last_name = input("What is your last name? ")
email = input("What is your email address? ")
phone_number = input("What is your phone number? ")
job = input("What is your job title? ")
id_number = input("What is your ID number? ")

# Display user's information.
print("------------------------------------------")
print(f"{last_name.upper()}, {first_name}")
print(f"{job}".capitalize())
print(f"ID: {id_number}")
print()
print(email.lower())
print(phone_number)
print("------------------------------------------")