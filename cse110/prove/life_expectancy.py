highest_life_expectancy = float(0)
life_expectancy = float(0)
lowest_life_expectancy = float(1000)
header = ""
with open("life-expectancy.csv") as file:
    header = next(file)
    for line in file:
        line = line.strip()
        item = line.split(",")
        print(item)
        life_expectancy = float(item[3])
        if life_expectancy > highest_life_expectancy:
            highest_life_expectancy = life_expectancy
        if life_expectancy < lowest_life_expectancy:
            lowest_life_expectancy = life_expectancy
    print(f"The highest life expectancy is {highest_life_expectancy:.2f}")
    print(f"The lowest life expectancy is {lowest_life_expectancy:.2f}")
    


# max_country, max_year
# to calculate average - keep track of COUNT of years (+=)
