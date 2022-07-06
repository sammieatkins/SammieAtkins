"""
Open the provinces.txt file for reading.
Read the contents of the file into a list where each line of text in the file is stored in a separate element in the list.
Print the entire list.

Remove the first element from the list.
Remove the last element from the list.
Replace all occurrences of "AB" in the list with "Alberta".
Count the number of elements that are "Alberta" and print that number.
"""
def main():
    provinces_list = read_list("provinces.txt")
    print(provinces_list)
    provinces_list.pop(0)
    provinces_list.pop()
    for i in range(len(provinces_list)):
        if provinces_list[i] == "AB":
            provinces_list[i] = "Alberta"
    alberta_count = provinces_list.count("Alberta")
    print(f"Alberta occurs {alberta_count} times in the modified list")
    

def read_list(filename):
    """Read the contents of a text file into a list
    and return the list that contains the lines of text.

    Parameter filename: the name of the text file to read
    Return: a list of strings
    """
    with open(filename, "rt") as provinces_file:
        provinces = []
        for line in provinces_file:
            clean_line = line.strip()
            provinces.append(clean_line)
    return provinces

if __name__ == "__main__":
    main()