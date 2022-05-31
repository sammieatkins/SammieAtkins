# Functions.
def display_regular(message):
    print(message)
def display_uppercase(message):
    message_upper = message.upper()
    print(message_upper)
def display_lowercase(message):
    message_lower = message.lower()
    print(message_lower)

# Input
message = input("What is your message? ")
display_regular(message)
display_uppercase(message)
display_lowercase(message)