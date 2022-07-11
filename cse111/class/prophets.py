def main():
    # last_name = get_last_name("Burton, Scott H.")
    # print(last_name)
    
    # first_name = get_first_name("Burton, Scott H.")
    # print(first_name)
    names = get_names()
    # no parentheses for get_last_name bc we don't want it to run
    # last_names = convert_names(names, get_last_name)
    # print_list(last_names)

    # upper_last_names = convert_names(last_names, convert_to_uppercase)
    # print_list(upper_last_names)

    # does same thing as convert_names() function
    # result_list = map(get_last_name, names)

    # MAP
    # does same thing as convert_to_uppercase() function. can do function in-line. for single use functions
    result_list = map(lambda name: name.upper(), names)
    # to use later:
    # uppercase = lambda name: name.upper()

    # FILTER
    result_list= filter(has_period, names)
    result_list = filter(lambda name: len(name) > 15, names)

    # SORT
    # by default
    result_list = sorted(names)
    # by first name
    result_list = sorted(names, key=get_first_name)
    # by length small to big
    result_list = sorted(names, key=lambda name: len(name))
    # by length big to small
    result_list = sorted(names, key=lambda name: len(name), reverse=True)

    # result_list = map(convert_to_uppercase, map(get_first_name, names))

    print_list(result_list)

def has_period(name):
    if "." in name:
        return True
    else:
        return False

def convert_to_uppercase(name):
    return name.upper()

def convert_names(name_list, conversion_function):
    last_name_list = []

    for name in name_list:
        last_name = conversion_function(name)
        last_name_list.append(last_name)

    return last_name_list

def get_first_name(name):
    # name will be something like: "Smith, Joseph F."
    parts_of_name = name.split(",")
    given_names = parts_of_name[1]

    parts_of_given_names = given_names.split()
    first_name = parts_of_given_names[0]
    # given_names = given_names.strip()

    return first_name

def get_last_name(name):
    # name will be something like: "Smith, Joseph F."
    parts_of_name = name.split(",")
    last_name = parts_of_name[0]
    return last_name

def print_list(the_list):
    for item in the_list:
        print(item)

def get_names():
    names = [
        "Smith, Joseph",
        "Young, Brigham",
        "Taylor, John",
        "Woodruf, Wilford",
        "Snow, Lorenzo",
        "Smith, Joseph F.",
        "Grant, Heber J.",
        "Smith, George Albert"
    ]
    return names

if __name__ == "__main__":
    main()