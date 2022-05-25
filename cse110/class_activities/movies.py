user_rating = input("What rating do you want to see? ")

with open("movies.csv") as movies_file:
    for line in movies_file:
        line = line.strip()
        values = line.split(",")

        title = values[0]
        year = int(values[1])
        runtime = float(values[2])
        rating = values[3]

        if rating.upper() == user_rating.upper():
                print(f"{title} ({year}) - Rated {rating}")
        