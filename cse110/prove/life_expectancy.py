highest_life_expectancy = float(0)
life_expectancy = float(0)
lowest_life_expectancy = float(1000)
header = ""
with open("life-expectancy.csv") as file:
    for line in file:
        line = line.strip()
        item = line.split(",")
        print(item)
        header = next(file)
        life_expectancy = float(item[3])
        if life_expectancy > highest_life_expectancy:
            highest_life_expectancy = life_expectancy
            print(f"The highest life expectancy is {highest_life_expectancy:.2f}")
        if life_expectancy < lowest_life_expectancy:
            lowest_life_expectancy = life_expectancy
            print(f"The lowest life expectancy is {lowest_life_expectancy:.2f}")


