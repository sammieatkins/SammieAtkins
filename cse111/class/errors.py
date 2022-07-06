
def get_numeric_data(prompt_text):
    good_number = False
    number = 0

    while good_number == False:
        try:
            number = int(input(prompt_text))
            print(f"You entered {number}")
            result = 100 / number
            print(f"100 divided by yours is: {result}")
            good_number = True
        except ValueError as error_message:
            print("That is not a valid number.")
            print(f"The error message was {error_message}")
        except ZeroDivisionError:
            print("That is a number, but would cause division by zero. Please try again. :)")
        # not recommended because sometimes you want to see the default error
        except:
            print("Something else bad happened, but I don't know what...")
    return number
num1 = get_numeric_data("Please enter a number: ")
# num2 = get_numeric_data("Please enter a second number: ")
print("End of program")