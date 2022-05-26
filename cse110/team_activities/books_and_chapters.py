most_chapters = 0
most_chapters_book = ""
user_scripture = -1
scripture_options = ["1. Old Testament","2. New Testament","3. Book of Mormon","4. Doctrine and Covenants","5. Pearl of Great Price","6. Nevermind :)"]

while user_scripture != 6:
    for item in scripture_options:
        menu = item.split(",")
        print(menu)
    
    user_scripture = int(input("Which book of scripture would you like to learn more about? "))

    with open("books_and_chapters.txt") as file:
        for line in file:
            line = line.strip()
            parts = line.split(":")

            book = parts[0]
            chapters = int(parts[1])
            scripture = parts[2]

            if scripture == user_scripture:
                print(f"Scripture: {scripture}, Book: {book}, Chapters: {chapters}")
                if chapters > most_chapters:
                    most_chapters = chapters

                    most_chapters_book = book

    print(f"The book with the most chapters is {most_chapters_book.title()} with {most_chapters} chapters.")
#print thank you