# Variables. 
life_expectancy = float(0)
header = ""
year = 0
avg_year = 0
avg_life = 0
total = 0
country = ""

max_life = float(0)
max_country = ""
max_year = 0

min_life = float(1000)
min_country = ""
min_year = 999999

user_max_life = float(0)
user_max_country = ""
user_max_year = 0

user_min_life = float(1000)
user_min_country = ""
user_min_year = 999999

# Menu.
print()
print("You can search by:")
print("1. Year")
print("2. Country")
print()

# User choices. 
choice = int(input("Enter number of menu item: "))
print()

if choice == 1:
    print()
    user_year = input("Enter the year of interest: ")
    print()
elif choice == 2:
    user_country = input("Enter the country of interest: ")
    print()
else:
    print("That's not a menu item. Please try again.")
    print()

with open("life-expectancy.csv") as file:
    header = next(file)
    for line in file:
        line = line.strip()
        item = line.split(",")
        # print(item)

        life_expectancy = float(item[3])

        # Overall life expectancy data.
        if life_expectancy > max_life:
            max_life = life_expectancy
            max_country = item[0]
            max_year = item[2]

        if life_expectancy < min_life:
            min_life = life_expectancy
            min_country = item[0]
            min_year = item[2]
        
        # Choice 1 - YEAR. 
        if choice == 1:
            # User year life expectancy data.
            year = item[2]
            if year == user_year:
                avg_year += 1
                total += life_expectancy
                if life_expectancy > user_max_life:
                    user_max_life = life_expectancy
                    user_max_country = item[0]
                if life_expectancy < user_min_life:
                    user_min_life = life_expectancy
                    user_min_country = item[0]

        # Choice 2 - COUNTRY.
        elif choice == 2:
            # User country life expectancy data. 
            country = item[0]
            if country == user_country:
                avg_year += 1
                total += life_expectancy
                if life_expectancy > user_max_life:
                    user_max_life = life_expectancy
                    user_max_country = item[0]
                if life_expectancy < user_min_life:
                    user_min_life = life_expectancy
                    user_min_country = item[0]
    
    avg_life = total / avg_year

    print(f"The overall max life expectancy is: {max_life:.2f} from {max_country} in {max_year}")
    print(f"The overall min life expectancy is: {min_life:.2f} from {min_country} in {min_year}")
    print()

    if choice == 1:
        print(f"For the year {user_year}:")
        print(f"The average life expectancy across all countries was {avg_life:.2f}")
        print(f"The max life expectancy was in {user_max_country} with {user_max_life:.2f}")
        print(f"The min life expectancy was in {user_min_country} with {user_min_life:.2f}")
        print()
    if choice == 2:
        print(f"For the country {user_country}:")
        print(f"The average life expectancy across all countries was {avg_life:.2f}")
        print(f"The max life expectancy was in {user_max_country} with {user_max_life:.2f}")
        print(f"The min life expectancy was in {user_min_country} with {user_min_life:.2f}")
        print()
    


