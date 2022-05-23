with open("hr_system.txt") as file:
    for line in file:
        line = line.strip()
        parts = line.split(" ")
        name = parts [0]
        id = parts [1]
        title = parts [2]
        salary = float(parts [3])
        pay = salary / 26
        if title.lower() == "engineer":
            bonus = pay + 1000
            print(f"{name} (ID: {id}), Title: {title} - ${bonus:,.2f}")
        else:
            print(f"{name} (ID: {id}), Title: {title} - ${pay:,.2f}")
