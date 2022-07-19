import pytest
import csv
from books import find_author, count_books_read

def test_find_author():
    book = ["1","The Silly Goose","Sammie Atkins","2022-07-18 10:30:22"]
    last_name = find_author(book)
    assert last_name == "ATKINS"

    book = ["2","The Silliest Goose","Sammie J. Atkins","2022-07-18 10:41:22"]
    last_name = find_author(book)
    assert last_name == "ATKINS"

    book = ["3","The Sillier Goose","Sammie J. Atkins ","2022-07-18 10:41:22"]
    last_name = find_author(book)
    assert last_name == "ATKINS"

def test_count_books_read():
    books_list = []
    with open("test_books.csv") as file:
        reader = csv.reader(file)
        next(reader)
        for line in reader:
            books_list.append(line)
    books_read = count_books_read(books_list)
    assert books_read == 2
    

pytest.main(["-v", "--tb=line", "-rN", __file__])