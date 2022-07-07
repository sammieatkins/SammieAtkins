def main():
    user_input = get_input()
    print(f"The value is {user_input}")

def get_input():
    user_input = 1
    try:
        user_input = int(input("Please enter a number from 1-100: "))
        
        if user_input < 1 or user_input > 100:
            raise ValueError("Your number was outside the valid range.")
    except ValueError:
        print("Sorry, that is not a valid number.")
    return user_input

main()