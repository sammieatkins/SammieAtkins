import pytest
import csv
from books import find_author, count_books_read, make_list

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
    books_list = make_list("test_books.csv")
    books_read = count_books_read(books_list)
    assert books_read == 3
    

pytest.main(["-v", "--tb=line", "-rN", __file__])