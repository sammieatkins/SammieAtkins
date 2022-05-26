youngest = 999

people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]
for line in people:
    person = line.split()
    name = person[0]
    age = int(person[1])
    if age < youngest:
        youngest = age
        youngest_name = name
print(f"The youngest person is {youngest_name} with an age of {youngest}.")