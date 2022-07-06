import csv
I_NUMBER_INDEX = 0
NAME_INDEX = 1

def main():
    students_dict = read_dict("students.csv", I_NUMBER_INDEX)
    # User I-number input
    user_i_number = input("Please enter an I-Number (xxxxxxxxx): ")
    # Find name
    message = find_name(students_dict, user_i_number)
    # Print name
    print(message)

#next(reader)

def read_dict(filename, key_column_index):
    """
    Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    students_dict = {}
    with open(filename) as file:
        reader = csv.reader(file)
        next(reader)
        for row_list in reader:
            if len(row_list) != 0:
                key = row_list[key_column_index]
                students_dict[key] = row_list

    return students_dict

def find_name(students_dict, i_number):
    """
    If the I-number is in the students_dict, it will return the student name. Otherwise, it will return "No such student". 
    Parameters:
        students_dict: dictionary with students' i-
    """
    if i_number in students_dict:
        # gets name
        message = students_dict[i_number][NAME_INDEX]
    else:
        message = "No such student"

    return message

if __name__ == "__main__":
    main()

# get_i_number() to test if i_number is valid