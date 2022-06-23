def main():
    total = 0
    display_welcome()

    question_one = input("I feel that I am a person of worth, at least on an equal plane with others. ")
    value = get_positive(question_one)
    total += value

    question_two = input("I feel that I have a number of good qualities. ")
    value = get_positive(question_two)
    total += value

def display_welcome():
    """
    Displays the welcome message introducing the quiz. 
    """
    print("""This program is an implementation of the Rosenberg
        Self-Esteem Scale. This program will show you ten
        statements that you could possibly apply to yourself.
        Please rate how much you agree with each of the
        statements by responding with one of these four letters:

        D means you strongly disagree with the statement.
        d means you disagree with the statement.
        a means you agree with the statement.
        A means you strongly agree with the statement.""")

def get_positive(answer):
    """
    Calculates points based on answer with the positive scale. (Strongly Disagree: 0, Disagree: 1, Agree: 2, Strongly Agree: 3)
    Parameter:
        answer: answer to question in format "D", "d", "a", "A"
    Returns:
        points
    """
    if answer == "D":
        point = 0
    elif answer == "d":
        point = 1
    elif answer == "a":
        point = 2
    elif answer == "A":
        point = 3
    return point

